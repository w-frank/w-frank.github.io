Title: How to Connect to Xilinx Zynq Boards from Linux
Date: 2021-02-04 13:17
Modified: 2021-02-04 13:17
Category: Linux
Tags: linux, programming, electronics, zynq
Slug: zynq-connection-1
Authors: Will Frank
Summary: Remotely accessing Xilinx Zynq based boards from Linux hosts.

## Using UART port
Connect the host PC (USB) to the UART port on the Zynq board (typically micro USB)
and run:
```shell
# Install minicom
sudo apt update && sudo apt install minicom
minicom –D /dev/ttyUSB0 –b 115200 -8 -o
```
Reboot the board.

## Using direct Ethernet connection
Connect the board to the host using the ethernet port on the host system, or an
ethernet to USB adapter.

Configure on the host:

1. Network Connections > (Select the connection interface to the board) > Edit > IPv4 Settings
2. Change Method to Manual
3. Edit Address to: 192.168.1.1
4. Edit Netmask to: 255.255.255.0
5. Use the menu on the host to disconnect and connect to the interface that you have just configured.

Assign a static IP address on the target board. Edit the file `/etc/network/interfaces`
as follows:
1. Comment out the line related to DHCP configuration:
```shell
# iface eth0 inet dhcp
```
2. Append the relevant network information:
```shell
iface eth0 inet static
address 192.168.1.42
gateway 192.168.1.1
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255
```
3. Restart the network interface:
```shell
sudo ifdown eth0 && sudo ifup eth0
```

Connect to the board by: ssh root@192.168.1.42


