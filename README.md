# tmux-powerline segment toggler for tmux

[![GitHub](https://img.shields.io/github/license/aloyr/tmux-powerline-toggler)](https://opensource.org/licenses/MIT)

Show a menu with tmux-powerline segments, and allows you to toggle them on and off.

This is just a first draft and assumes the user has configured a custom theme on `~/.config/tmux/themes`

## Installation
### Requirements
* macOS
* tmux >= 3.0
* python >= 3.0
* tmux-powerline

### With Tmux Plugin Manager
Add the plugin in `.tmux.conf`:
```
set -g @plugin 'aloyr/tmux-powerline-toggler'
```
Press `prefix + I` to fetch the plugin and source it. Done.

### Manual
Clone the repo somewhere. Add `run-shell` in the end of `.tmux.conf`:

```
run-shell PATH_TO_REPO/tmux-powerline-toggler.tmux
```
NOTE: this line should be placed after `set-option -g status-right ...`.

Press `prefix + :` and type `source-file ~/.tmux.conf`. Done.

## Usage
Press tmux `prefix + C-t` (for example, `C-b C-t`) and you will see a list of powerline segments.

