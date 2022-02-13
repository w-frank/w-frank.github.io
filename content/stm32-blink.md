Title: STM32: Blink an LED
Date: 2022-02-13 20:07
Modified: 22022-02-13 20:07
Category: STM32
Tags: STM32, ARM, linux, programming
Slug: stm32-led
Authors: The Hello World! of STM32 embedded programming.

1. Open STM32CubeMX and start a new STM32 project.
2. I'm using the STM32 Discovery board which has an STM32F407VG microcontroller
and 4 onboard LEDs. For this project, I'm using the STM32 Cube Framework with
the HAL libraries.Select STM32F4-DISC1 from the board selector.
3. The STM32F4 Discovery board has the following LEDs available to the user:
| LED    | NAME | PIN  |
| ------ | ---- | ---- |
| Green  | LD4  | PD12 |
| Orange | LD3  | PD13 |
| Red    | LD5  | PD14 |
| Blue   | LD6  | PD15 |

For this tutorial we'll use the green LED. In the MCU pinout viewer, set PD12
to GPIO_Output. Save and generate the code.
4. In the code editor, add the following to the main function in ```main.c```:
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
5. Build the program and download it to the board. You should see the green LED
flashing every 1 second.