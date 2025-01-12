#include "LCD.h"

int main() {
    wiringPiSetup();  // Initialize WiringPi

    ER5517Basic lcd;
    lcd.SPIInit();    // Initialize SPI
    lcd.LCD_Init();   // Initialize the LCD

    lcd.FillScreen(White);  // Fill the screen with white
    lcd.DrawCircle_Fill(240, 240, 50, Red);  // Draw a red circle in the center

    return 0;
}