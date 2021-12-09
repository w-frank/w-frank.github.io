Title: Sending Files Over Serial With Kermit
Date: 2021-12-09 09:08
Modified: 2021-12-09 09:08
Category: Linux
Tags: linux, programming
Slug: sending-files-with-kermit-1
Authors: Will Frank
Summary: A step by step guide to sending files to a remote machine over serial with Kermit and Tera Term.

## Introduction
I recently needed to send a binary FPGA image file from a Windows PC to a device
running embedded Linux that only had a serial console access on a USB port.
Fortunately, the device had kermit installed and I could use 
[Tera Term](https://ttssh2.osdn.jp/index.html.en) to transfer the file.

Kermit is a file transfer/management protocol and a set of communications
software tools. Kermit can be installed on Liunx using standard package
repositories. Versions for Windows and most other platforms are available from 
`http://www.kermitproject.org/current.html`. Tera Term has kermit built in and
can be downloaded from `https://ttssh2.osdn.jp/index.html.en`.

## Running Kermit
Kermit is started on Linux by running
```shell
$ kermit
```
Once started kermit will output something similar to the following and enter the
kermit prompt
```shell
C-Kermit 9.0.304 OPEN SOURCE: Dev.22, 1 May 2017, for Linux
 Copyright (C) 1985, 2017,
  Trustees of Columbia University in the City of New York.
Type ? or HELP for help.
(~/) C-Kermit>
```
## Configure Serial Connection
To display the detected serial ports on the remote Linux machine run the
`dmesg` command and search for serial ports:
```shell
$ dmesg | grep tty
```
In my case the USB console was `\dev\ttyPS0`.

The kermit console can then be used to configure the serial port at
`\dev\ttyPS0` and file settings:
```shell
(~/) C-Kermit> set line \dev\ttyPS0
(~/) C-Kermit> set carrier-watch off
(~/) C-Kermit> set speed 115200
(~/) C-Kermit> set parity none
(~/) C-Kermit> set stop-bits 1
(~/) C-Kermit> set flow-control none
(~/) C-Kermit> set file type bin
```
In my case the port is set to 115200 baud, 8 bits, no parity, 1 stop bit, no
flow control and the file type is binary.

Now, to connect to the Windows host PC run
```shell
(~/) C-Kermit> connect
```
once connected prepare kermit to receive a file:
```shell
(~/) C-Kermit> receive
Return to your local Kermit and give a SEND command.

KERMIT READY TO RECEIVE...
```

## Transfer File Using Tera Term
Open Tera Term and setup the serial connection `Setup > Serial Port...`. Use the
same settings as the remote kermit session above. The relevant port can be found
using the Windows Device Manager. To open the port click `New open`.

To start the file transfer click `File > Transfer > Kermit > Send...` and select
and open the file you wish to send.

## Ending a Kermit Session
Once the file transfer is complete, close the serial port and exit kermit:
```shell
(~/) C-Kermit> close
(~/) C-Kermit> exit
```
The default location for the transferred file is your home directory.
