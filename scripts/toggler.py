import os
import sys
import time
from subprocess import Popen, PIPE

def get_theme_file():
    script = '/'.join(os.path.realpath(sys.argv[0]).split('/')[:-1]) + '/find_theme.sh'
    with Popen(script, stdout=PIPE) as p:
        (data, _) = p.communicate()
    return data.strip()

def get_segments()-> list:
    data = get_theme_file()
    with open(data.strip(), 'r') as f:
        lines = f.readlines()
        ok_to_read = False
        segments = []
        for line in lines:
            found_left = line.strip().find('TMUX_POWERLINE_LEFT_STATUS_SEGMENTS') == 0
            found_right = line.strip().find('TMUX_POWERLINE_RIGHT_STATUS_SEGMENTS') == 0
            found_end = line.strip().find(')') == 0
            if not ok_to_read and (found_left or found_right):
                ok_to_read = True
                continue
            if ok_to_read and found_end:
                ok_to_read = False
                continue
            if ok_to_read:
                segments.append(line.strip().split()[0].replace('"','').replace('#','.'))
    return segments

def make_menu(items: list)-> None:
    cmd = [
            'tmux',
            'menu', '-T', 'Segments',
            '-x', 'R', '-y', 'S',
            '']

    for item in items:
        cmd.append(item)
        cmd.append('')
        run_param = "run -b 'printf " + item + " | pbcopy'"
        cmd.append(run_param)

    cmd.append('quit')
    cmd.append('q')
    run_param = "run -b 'printf none | pbcopy'"
    cmd.append(run_param)

    p = Popen(cmd, stdout=PIPE)
    (data, err) = p.communicate()

def toggle_item(item):
    if len(item) < 1:
        return
    theme_file_name = get_theme_file()
    if item[0] == '.':
        original = '#"' + item[1:]
        new = '"' + item[1:]
    else:
        original = '"' + item
        new = '#"' + item
    with open(theme_file_name, 'r') as f:
        theme_file_data = f.read()
    new_data = theme_file_data.replace(original, new)
    with open(theme_file_name, 'w') as f:
        f.write(new_data)

def main()-> None:
    data = get_segments()
    make_menu(data)
    time.sleep(0.5)
    (selection, err) = Popen(['pbpaste'], stdout=PIPE).communicate()
    Popen(['tmux','display-message','toggle segment: "' + selection.decode().strip() + '"'], stdout=PIPE).communicate()
    if selection.decode().strip() != 'none':
        toggle_item(selection.decode().strip())
        main()

if __name__ == '__main__':
    main()

