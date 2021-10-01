Title: How to Write a Linux Kernel Module
Date: 2021-01-25 11:42
Modified: 2021-01-25 11:42
Category: Linux
Tags: linux, programming, electronics
Slug: linux-kernel-moduled-1
Authors: Will Frank
Summary: The "Hello World" of Linux Device Driver Programming.

## Introduction
What exactly is a Linux kernel module? Modules are pieces of code that can be 
dynamically loaded and unloaded into the kernel on demand. They extend the 
functionality of the kernel without the need to reboot the system. For example,
one type of module is the device driver, which allow kernel access to hardware
connected to the system. Without modules, the kernel would have to be monolithic,
with new functionality built directly into the kernel image. Not only does this 
lead to larger kernels, but it also has the disadvantage that the kernel must be
rebuilt and restarted every time we want to add new functionality.

## Requirements
In order to compile kernel modules you must have the kernel source installed on
your system or at least the required parts of it. These should always be found 
under `/lib/modules/$(uname -r)/build`.

To install them (as root):
```
# Debian & Ubuntu
$ sudo apt-get install linux-headers-$(uname -r) 
```

## Minimal Hello World Driver
This is the hello world of device driver programming, the simplest module 
possible. In your development directory create a file `hello_world.c` with the 
following contents:

```c
// hello_world.c

#include <linux/init.h>
#include <linux/module.h>

MODULE_LICENSE ("GPL v3.0");

static int __init hello_world_init (void)
{
    printk (KERN_INFO "Hello world: module loaded at 0x%p\n", hello_world_init);
    return 0;
}

static void __exit hello_world_exit (void)
{
    printk (KERN_INFO "Bye world: module unloaded from 0x%p\n", hello_world_exit);
}

module_init (hello_world_init);
module_exit (hello_world_exit);
```

## Compiling
For the purposes of this guide we will use a very simplified makefile. Create
a file called `makefile` containing:
```make
# Minimal Kernel Module Builder

obj-m += hello_world.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

Running `make` should result in something similar to:
```shell
$ make
make -C /lib/modules/5.8.0-38-generic/build M=/home/will/Documents/linux-device-drivers modules
make[1]: Entering directory '/usr/src/linux-headers-5.8.0-38-generic'
  CC [M]  /home/will/Documents/linux-device-drivers/hello_world.o
  MODPOST /home/will/Documents/linux-device-drivers/Module.symvers
  CC [M]  /home/will/Documents/linux-device-drivers/hello_world.mod.o
  LD [M]  /home/will/Documents/linux-device-drivers/hello_world.ko
make[1]: Leaving directory '/usr/src/linux-headers-5.8.0-38-generic'
```

My kernel version (5.8.0-38-generic) will most likely not be the same as yours
and my development path `/home/will/Documents/` will of course be substituted with
your current path (also in `$PWD`). We are now ready to load the module!

## Loading and removing the module
Linux provides the following utilities for loading and removing modules: `insmod`,
`rmmod` and `modprobe`. We will use the first two as they are simpler. To load 
the module, assuming you are in your development directory:
```shell
$ sudo insmod hello_world.ko
```
Following this you will be able to see the message from the module at the end 
of the kernel messages log. To read the kernal log:
```shell
$ dmesg | tail
[11947.850686] ...
[11949.947172] ...
[13193.606932] Hello world: module loaded at 0x00000000d086c253
```
`dmesg` prints the kernel message buffer and since it can be large we filter it
to only show the last 10 messages with `tail`.

You can also check that the module is loaded into the kernel with `lsmod` or by
displaying the content of the `/proc/modules` file:
```shell
$ lsmod
Module                  Size  Used by
hello_world            16384  0
rfcomm                 81920  16
ccm                    20480  9
...                    ...    ...

cat /proc/modules | head
hello_world 16384 0 - Live 0x0000000000000000 (POE)
rfcomm 81920 16 - Live 0x0000000000000000
ccm 20480 9 - Live 0x0000000000000000
...
```

Now, to remove the module:
```shell
$ sudo rmmod hello_world
```
Note that the module is removed by its name `hello_world` not by the file name
`hello_world.ko`. Checking the message log again:
```shell
$ dmesg | tail
[11949.947172] ...
[13193.606932] ...
[13343.190194] ...
[13680.414640] ...
[13682.000494] ...
[13698.974007] ...
[13706.007413] ...
[13707.943905] Hello world: module loaded at 0x000000002087a0cf
[14071.813961] Bye world: module unloaded from 0x00000000b13cd70a

```
At the end of the log, we can see the module printed "Bye world" when it was
removed.