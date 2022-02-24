Title: Programming Serial Ports on Linux
Date: 2022-01-31 12:00
Modified: 2022-01-31 12:00
Category: Linux
Tags: linux, programming
Slug: linux-serial-programming-1
Authors: Will Frank
Summary: A tutorial on how to program serial ports on Linux machines.

This is a tutorial on how to program the serial ports on your Linux machine.

## Serial Ports on Linux
Traditional hardware serial ports on Linux are names as ttyS* where * can be 1,
2,3,... etc. E.g. ttyS1, ttyS2, ttyS3, ...

In Linux hardware components such as sserial ports are treated as files and are
located ub rge /dev folder in the file system/ If you navigate to the /dev folder
and list the files using the ls command you can see the files corresponding to
various hardware devices:

## Programming the Serial Port
To perform serial I/O in Linux we are going to use the termios API.


