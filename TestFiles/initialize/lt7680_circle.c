#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL 0
#define SPI_SPEED 500000

// Send a command to the LT7680
void send_command(unsigned char command) {
    unsigned char buffer[2] = {0x00, command};
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

// Send data to the LT7680
void send_data(unsigned char data) {
    unsigned char buffer[2] = {0x01, data};
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

// Draw a filled circle on the display
void draw_circle() {
    send_command(0x77);  // Set major radius (low byte)
    send_data(0x32);     // Radius = 50 (low byte)
    send_command(0x78);  // Set major radius (high byte)
    send_data(0x00);     // Radius = 50 (high byte)

    send_command(0x7B);  // Set center X (low byte)
    send_data(0xA0);     // Center X = 160 (low byte)
    send_command(0x7C);  // Set center X (high byte)
    send_data(0x00);     // Center X = 160 (high byte)

    send_command(0x7D);  // Set center Y (low byte)
    send_data(0x78);     // Center Y = 120 (low byte)
    send_command(0x7E);  // Set center Y (high byte)
    send_data(0x00);     // Center Y = 120 (high byte)

    send_command(0x76);  // Start drawing
    send_data(0xC0);     // Draw filled circle
    printf("Circle drawing command sent.\n");
}

int main() {
    if (wiringPiSetup() == -1) {
        printf("WiringPi setup failed.\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed.\n");
        return 1;
    }

    // Draw a circle
    draw_circle();

    return 0;
}
