#!/bin/bash

# Inspired by https://github.com/snwh/ubuntu-post-install

echo '#-----------------------------------------#'
echo '#     Digenome-toolkit Install Script     #'
echo '#-----------------------------------------#'

show_info() {
echo -e "\033[1;34m$@\033[0m"
}

show_success() {
echo -e "\033[1;32m$@\033[0m"
}

show_error() {
echo -e "\033[1;31m$@\033[m" 1>&2
}

dir="$(dirname "$0")"

function install_digenome {
  if [ $1 = $HOME ]; then
    if [ -e "$HOME/.profile" ]; then
      pf="$HOME/.profile"
    else
      pf="$HOME/.bash_profile"
    fi
    bindir="$HOME/bin"
  else
    pf="/etc/profile.d/digenome-toolkit.sh"
    bindir="/usr/bin"
  fi

  echo "Building 1.find_position_bam.cpp..."
  $dir/build_find_position_bam.sh
  if [ ! -d "$1/digenome-toolkit" ]; then
    mkdir -p "$1/digenome-toolkit"
  fi
  if [ "$1/digenome-toolkit" != "$dir" ]; then
    echo "Copying all required files..."
    cp -fr $dir/* $1/digenome-toolkit/
  fi
  echo "Adding LD_LIBRARY_PATH and DIGENOME_HOME in $pf ..."
  echo "export LD_LIBRARY_PATH=$1/digenome-toolkit/bamtools/lib" >> $pf
  echo "export DIGENOME_HOME=$1/digenome-toolkit" >> $pf
  echo "Creating symlink of digenome-run script in bin directory..."
  if [ ! -d $bindir ]; then
    mkdir $bindir
  fi
  ln -sf "$1/digenome-toolkit/digenome-run" "$bindir/digenome-run"
  source "$pf"
  echo "Done."
}

function main {
  echo ''
  show_info 'What would you like to do? '
  echo ''
  echo '1. Install digenome-toolkit in your home directory?'
  echo '2. Install digenome-toolkit system-wide?'
  echo 'q. Quit?'
  echo ''
  show_info 'Enter your choice :' && read REPLY
  case $REPLY in
    1) install_digenome $HOME;;
    2) install_digenome "/opt";;
    [Qq]* ) echo '' && quit;;
    * ) clear && show_error '\aNot an option, try again.' && main;;
  esac
}

function quit {
  read -p "Are you sure you want to quit? (Y)es, (N)o " REPLY
  case $REPLY in
    [Yy]* ) exit 99;;
    [Nn]* ) clear && main;;
    * ) clear && show_error 'Sorry, try again.' && quit;;
  esac
}

main
