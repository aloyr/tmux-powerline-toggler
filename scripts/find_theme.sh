#!/usr/bin/env bash

export TMUX_POWERLINE_DIR_HOME="${TMUX_PLUGIN_MANAGER_PATH}tmux-powerline"
. "${TMUX_POWERLINE_DIR_HOME}/lib/headers.sh"

. ${TMUX_PLUGIN_MANAGER_PATH}/tmux-powerline/lib/headers.sh
. ${TMUX_POWERLINE_CONFIG_FILE}
echo ${TMUX_POWERLINE_DIR_USER_THEMES}/${TMUX_POWERLINE_THEME}.sh
exit 0

