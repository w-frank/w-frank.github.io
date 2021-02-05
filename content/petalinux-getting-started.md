Title: Getting Started with Embedded Linux - PetaLinux
Date: 2021-02-05 17:04
Modified: 2021-02-05 17:04
Category: Linux
Tags: linux, programming, electronics, zynq
Slug: petalinux-1
Authors: Will Frank
Summary: How to get up and running with PetaLinux, the embedded Linux development tool-chain for Xilinx processing systems.

PetaLinux is an embedded Linux development tool-chain for Xilinx processing systems. 
This includes Versal, Zynq UltraScale+ MPSoC, Zynq-7000 SoCs, and MicroBlaze.
It offers a full Linux distribution which includes the Linux OS as well as a
complete configuration, build and deployment environment for Xilinx silicon. 
This guide will walk through the steps required for an initial setup for 
PetaLinux and the implementation of a pre-built design on a Xilinx Zynq based 
board such as the Avnet Zedboard.

## Download PetaLinux Installer

First, you will need to download the installer for [installer for PetaLinux](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools.html). 
The version must be the same as the Vivado and SDK installation you have on your 
development system. At the time of writing, the latest version is 2020.2 which
is used in this guide. The download may take a while. 

## Download PetaLinux Dependencies
There are a variety of dependences that are required for PetaLinux to operate.
Many of the packages may already be installed on your computer, but some may not.
A full list of the dependences is given in the Package List on the [PetaLinux 2020.2 - Product Update Release Notes](https://www.xilinx.com/support/answers/75775.html) page.

Downloading these is the same as any other Linux package that you can get through
apt-get. When you make the following function call you 
can simply enter each module's name in the same line with spaces between.
```shell
sudo apt-get install tofrodos iproute gawk (etc)
```

## Configure Linux Shell to Bash
The PetaLinux tools require you to use bash as your Linux shell rather than
dash, which is typically the default if you're using Ubuntu. To configure this, 
use the following command:
```shell
sudo dpkg-reconfigure dash
```
When prompted to use dash as default shell, select no.

## Installing PetaLinux

Once the download has completed, make a new directory in which you would like the
PetaLinux tools to be installed. My Xilinx tools are in `/tools/Xilinx`, so I'm
going to install the PetaLinux tools in the same location. In a terminal, 
change directory (cd) into the directory the installer was downloaded into 
(most likely Downloads). Before running the PetaLinux installer, you will need 
to change the default user permissions on the PetaLinux installer file. The
following is adequate:

```shell
sudo chmod 755 petalinux-v2020.2-final-installer.run
```

Using 755 you are specifying the following permissions:

    7 --> u=rwx (4+2+1 for owner)
    5 --> g=rx (4+1 for group)
    5 --> o=rx (4+1 for others)

Now run the installer with a specified path to the PetaLinux directory you have
just created.

```shell
cd /tools/Xilinx
mkdir PetaLinux
cd ~/Downloads
./petalinux-v2020.2-final-installer.run --dir /tools/Xilinx/PetaLinux
```

## Configure Source Settings

The tools for PetaLinux to use within the terminal need to be sourced. This 
includes the settings64.sh and the settings.sh files in your Vivado and
PetaLinux installation directories, respectively. To avoid needing to type the 
source commands into the terminal every time, you can add a couple of lines to
the .bashrc script. This is a shell script that Bash runs whenever it is started
interactively. To modify this system wide, use a text editor to open your
.bashrc file. For Ubuntu this will be bash.bash.rc in the /etc directory
```shell
sudo gedit /etc/bash.bashrc
```
Once you have the script open, add the two commands for sourcing the appropriate
files at the bottom. Note that the path indicated here is where my installation
directories are and so your specific file paths may be different.
```shell
source /tools/Xilinx/PetaLinux/petalinux-v2020.2-final/settings.sh
```
After adding the line, save and close the editor.

## Create New Project
The petalinux-create command is used to create a new PetaLinux project:
```shell
petalinux-create --type project --template <CPU_TYPE> --name <PROJECT_NAME>
```
The parameters are as follows:
--template <CPU_TYPE> - the supported CPU types are zynqMP, zynq and microblaze
--name <PROJECT_NAME> - the name of the project you are building

This command will create a new PetaLinux project folder from a default template.
Later steps customise these settings to match the hardware (FPGA) project.

## Create a Project - Board Support Package
Creating a new project from an existing Board Support Package (BSP) is the
simplest way to get started with PetaLinux. It provides you with an already
functioning and bootable Linux image to start playing with. There are several
BSPs available from Xilinx. Once you have your chosen BSP downloaded, open a 
terminal and change directory to the location where you would like to create
your new PetaLinux project directory and enter the follow command:
```shell
petalinux-create -t project -s <path to BSP>
```

## Import Hardware Configuration

```shell
 petalinux-config --get-hw-description=<path-to-directory-that-contains-hardware-description-file>
```

## Configure, Build and Package
This step is reasonably straight forward from a user perspective. However, it
does require accepting some background 'magic' if you are not familar with the
process of compiling a Linux image from scratch. At the end of the configuration
and build process in PetaLinux you will have a kernel, file system, first and
second stage bootloader and a device tree compiled and ready to be deployed to
your hardware target. To run the configuration on the BSP package you downloaded
change directory to the one that was made with the petalinux-create command, and
type the following:
```shell
petalinux-config
```
This will initalise a configuration menu for your PetaLinux project. Make sure 
your terminal window is at least its default dimensions or the menu will fail to
launch. There are a variety of boot options available depending on your
application. Since the setup and operation of each of the different boot options
is a bit involved, it will not be covered here.
The configuration process will continue on (this will take some time).

Once the configuration is complete, you will need to build your image by
entering the following command:
```shell
petalinux-build
```
The execution of this command will also take a few minutes to complete. Once it
is finished, enter the following command:
```shell
petalinux-package --boot --force --fsbl ./images/linux/zynq_fsbl.elf --fpga 
./images/linux/download.bit --u-boot
```
After this completes you should have your BOOT.bin and U-boot files ready to go.
## Prepare Bootable SD card 
The SD card you use will need to have two partitions on it. An 8 GB card is
recommended. The first partition (BOOT) is formatted as a File Allocation Table 
(FAT) of 1 GB, and the second partition (rootfs) is formatted as an ext4 for the
remaining space on the card. The BOOT partition is where the BOOT.bin and
image.ub will be stored. The rootfs partition is where the file system for the
Linux image will be. You can use a utility such as fdisk or gparted to format 
your SD card as required. Xilinx provide a useful [tutorial](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18842385/How+to+format+SD+card+for+SD+boot)
using fdisk.

Copy the BOOT.bin and image.ub files into the first partition on your SD card.
You can do this from your PetaLinux project root direvtory with the following
commands:
```shell
cp images/linux/BOOT.bin /media/will/BOOT
cp images/linux/image.ub /media/will/BOOT
```
Once the boot files have been copied into the BOOT partition of your SD card,
copy the root file system into the second rootfs partition. This can be done
with the following command:
```shell
cp images/linux/rootfc.cpio /media/will/rootfs
```
Once the root file system and boot files have been copied to the two partitions
of your SD card, you can now unmount and eject your SD card and load it into 
your board.