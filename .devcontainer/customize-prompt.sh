#!/bin/bash
# Define colors
BLUE="\[\033[01;34m\]"
GREEN="\[\033[01;32m\]"
RESET="\[\033[00m\]"

# Customize the PS1 (Prompt String 1)
# This example shows: [user@codespace] [directory] (branch)
# export PS1="${GREEN}\u@\h${RESET}:${BLUE}\w${RESET}\$ "
export PS1="${GREEN}\W \$ ${RESET}"
