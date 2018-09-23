#!/usr/bin/env sh

current_directory=$(pwd)
rsync -av --progress build/* /home/vagrant/poky/rpi-build/ --exclude update-rootfs.sh
