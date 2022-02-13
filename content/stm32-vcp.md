Title: STM32: USB Virtual COM Port (VCP)
Date: 2022-02-13 16:44
Modified: 2022-02-13 16:44
Category: STM32
Tags: STM32, ARM, linux, programming
Slug: stm32-vcp
Authors: Will Frank
Summary: How to configure the USB peripheral of STM32 microcontrollers as a virtual COM port.

Serial communication is useful for interfacing microcontrollers with external
devices or to a host PC for debugging or data transfer. For STM32
devices a USB-UART bridge can be used to communicate with a USB device such as
a PC. However, many of the STM32 development boards have a USB peripheral
on-board. This tutorial covers setting up the STM32F4 Discovery board as a
virtual COM port (VCP).

I'm using the STM32 Discovery board which has an STM32F407VG microcontroller and
an on-board micro USB port. I'm using the STM32 Cube Framework with the HAL
libraries and USB device middleware for this application.

Open STM32 CubeIDE and start a new STM32 project. Select your microcontroller
and/or board. Here I select the STM32F4 Discovery.

Now in the STM32 CubeMX perspective, enable the High Speed External (HSE)
clock and select Ceramic/Crystal Resonator.

Under the Connectivity section select the mode as Device_Only.

Finally, under the Middleware section, select the USB_DEVICE and set the
Class For FS IP as Communication Device Class (Virtual Port Com).

Next, save the CubeMX (.ioc) file to generate the code. Now all the peripherals 
are enabled for the USB communication over VCP. But as the HAL USB stack is
heavy on the memory, the minimum heap size needed has to be changed. This can be
changed by opening the STM32F407VGTX_FLASH.ld linker script file and changing
the line 59 to _Min_Heap_Size = 0x600;.

Lets test this setup with a simple echo application using the USB CDC. First
open the usbd_cdc_if.c file. Find the CDC_Receive_FS function and edit:
```C
static int8_t CDC_Receive_FS(uint8_t* Buf, uint32_t *Len)
{
    /* USER CODE BEGIN 6 */
    USBD_CDC_SetRxBuffer(&hUsbDeviceFS, &Buf[0]);
    USBD_CDC_ReceivePacket(&hUsbDeviceFS);
    CDC_Transmit_FS(Buf,*Len);
    return (USBD_OK);
    /* USER CODE END 6 */
}
```

Now build the project and download the program to the board using the built in
ST-Link.

When connected to your host PC by the micro USB (next to the audio jack on the 
STM32F4 Discovery board), the serial port should show up as */dev/ttyACM1* on
most Linux distributions. Start a serial port terminal, such as gtkterm and open
*ttyACM1*. The baud rate doesn't matter as it's ignored by the progam. On Ubuntu:
```shell
sudo apt-get install gtkterm
sudo gtkterm
```

Type a message in the serial monitor and press send. Then the STM32 device will
echo back the message you typed.

## Controlling a built-in LED using the VCP
The Virtual COM Port (VCP) opens up the possibility of remote control of the
STM32. As a simple example, the built-in LED on the STM32F4 Discovery can be
turned on and off using the VCP. First, open the CubeMX (.ioc ) file again to
generate the code for the LED. In the CubeMX perspective, select the pin for the
LED (which is PD13 for the orange LED of the STMF4 Discovery board) and set as
GPIO_Output. Now save the file to generate the code again. Next change the
CDC_Receive_FS function in the usbd_cdc_if.c file as follows:
```shell
static int8_t CDC_Receive_FS(uint8_t* Buf, uint32_t *Len)
{
    /* USER CODE BEGIN 6 */
    USBD_CDC_SetRxBuffer(&hUsbDeviceFS, &Buf[0]);
    USBD_CDC_ReceivePacket(&hUsbDeviceFS);
    if(Buf[0] == '1')
    {
        HAL_GPIO_WritePin(GPIOD, GPIO_PIN_13, GPIO_PIN_SET);
    }
    else if(Buf[0] == '0')
    {
        HAL_GPIO_WritePin(GPIOD, GPIO_PIN_13, GPIO_PIN_RESET);
    }
    return (USBD_OK);
    /* USER CODE END 6 */
}
```