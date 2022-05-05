Title: STM32: Blink an LED
Date: 2022-02-12 20:07
Modified: 2022-02-12 20:07
Category: STM32
Tags: STM32, ARM, linux, programming
Slug: stm32-led
Authors: Will Frank
Summary: The Hello World of STM32 embedded programming!

Open STM32CubeMX and start a new STM32 project.

I'm using the STM32F4 Discovery board which has an STM32F407VG microcontroller
and 4 onboard LEDs. For this project, I'm using the STM32 Cube Framework with
the HAL libraries. I'm also developing on a PC running Ubuntu 20.04.3.

Select STM32F4-DISC1 from the board selector.

The STM32F4 Discovery board has the following LEDs available to the user:

| <div style="width:75px">LED</div> | <div style="width:75px">NAME</div> | <div style="width:75px">PIN</div> |
| --------------------------------- | ---------------------------------- | --------------------------------- |
| Green                             | LD4                                | PD12                              |
| Orange                            | LD3                                | PD13                              |
| Red                               | LD5                                | PD14                              |
| Blue                              | LD6                                | PD15                              |
<br>

For this tutorial we'll use the green LED (LD4 - port D, pin 12). In the MCU pinout viewer, set PD12
to GPIO_Output. Save and generate the code.

In the code editor, add the following to the main function in ```main.c```:
```C
/* Infinite loop */
/* USER CODE BEGIN WHILE */
while (1)
{
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
  HAL_Delay(500);
/* USER CODE END WHILE */

/* USER CODE BEGIN 3 */

}
/* USER CODE END 3 */
```

Build the program and download it to the board. You should see the green LED
flashing every 1 second.

You probably already guessed it but the ```HAL_Delay()``` function pauses the execution
of the program for a given number of milliseconds (500 ms in the code above).
Adjusting this will speed up or slow down the blinking of the LED.