#include "LCD.h"

int main() {
    LCD_Init();  // Initialize LCD
    FillScreen(0xFF);  // Fill the screen with white
    return 0;
}