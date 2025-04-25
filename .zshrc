# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"
export PATH="$PATH:/$HOME/bin"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='nvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Docker
alias dcu='docker compose up'
alias dcd='docker compose down'
alias dcr='docker compose restart'
alias dcp='docker compose pull'
alias dps='docker ps'

# Git
alias gacp='git add . && git commit -m "cmt" && git push'

# Python
alias pve='python3 -m venv .env && source .env/bin/activate'
alias ave='source /home/user/.env/bin/activate'
alias dve='deactivate'
alias p='python3'
alias python='python3'

# Ansible
alias ap='ansible-playbook'

# Update
alias upup='sudo apt update; sudo apt upgrade -y'
alias fix='sudo apt upgrade --fix-missing'

# Other
alias c='cursor'
alias bat='batcat'
alias fm='ranger'
alias ff='fzf'
alias s='sublime'

# Scripts
alias cdown='~/scripts/cdown'
alias githook='~/scripts/githook.sh'
alias fix-corrupt='~/scripts/fix_zsh_corrupt.sh'

# Work Stack
alias mockitup='cd ~/mockit && docker compose up -d'
alias mockitdown='cd ~/mockit && docker compose down'
alias mockitrst='cd ~/mockit && docker compose restart'

alias slurpitup='cd ~/images && docker compose up -d'
alias slurpitdown='cd ~/images && docker compose down'
alias slurpitrrst='cd ~/images && docker compose restart'

alias netboxup='cd ~/slurpit_netbox && docker compose up -d'
alias netboxdown='cd ~/slurpit_netbox && docker compose down'
alias netboxrst='cd ~/slurpit_netbox && docker compose restart'

alias netpickerup='cd ~/netpicker && docker compose up -d'
alias netpickerdown='cd ~/netpicker && docker compose down'
alias netpickerrst='cd ~/netpicker && docker compose restart'

# Functions
fvim() {
  local file=$(find . -type f | fzf)
  [[ -n "$file" ]] && vim "$file"
}

fcat() {
  local file=$(find . -type f | fzf)
  [[ -n "$file" ]] && cat "$file"
}

fbat() {
  local file=$(find . -type f | fzf)
  [[ -n "$file" ]] && batcat "$file"
}

fcod() {
  local file=$(find . -type f | fzf)
  [[ -n "$file" ]] && cursor "$file"
}

fsub() {
  local file=$(find . -type f | fzf)
  [[ -n "$file" ]] && sublime "$file"
}

fcd() {
  cd "$(find . -type d | fzf)"
}

fpy() {
  local file=$(find . -type f | fzf)
  [[ -n "$file" ]] && python3 "$file"
}

export PATH=$PATH:/snap/bin

# Created by `pipx` on 2025-01-21 08:48:03
export PATH="$PATH:/home/user/.local/bin"

# bun completions
[ -s "/home/user/.bun/_bun" ] && source "/home/user/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
export PATH="$HOME/.bun/bin:$PATH"
