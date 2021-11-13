Title: How to Create your own custom Linux distribution using Yocto
Date: 2021-02-06 06:10
Modified: 2021-02-06 06:10
Category: Linux
Tags: linux, programming, electronics
Slug: yocto-1
Authors: Will Frank
Summary: 

## Prepare the Host
First we will install all the required dependencies on our host system. I am
using Ubuntu. If you are using a different distribution then take a look at the
[Yocto project Quick Start guide](https://www.yoctoproject.org/docs/2.4/yocto-project-qs/yocto-project-qs.html)
to see what dependencies to install.
git clone git://git.yoctoproject.org/poky
sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
    build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
    xz-utils debianutils iputils-ping libsdl1.2-dev xterm
```

## Clone the Yocto Poky
We will now clone the Yocto repoository from the Yocto Project website. Run the
command below, which will download the latest release (the "sumo" branch). We
will create a directory in the home directory to build our Yocto project:
```shell
mkdir ~/Yocto
mkdir ~/Yocto/test-project
cd ~/Yocto/test-project
git clone git://git.yoctoproject.org/poky
```

## Initialise the Build Environment
```shell
cd poky
source oe-init-build-env build
```
## Configuring Yocto
Navigate to the configuration directory
```shell
cd conf
```
