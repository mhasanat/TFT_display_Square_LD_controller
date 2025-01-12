#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL 0
#define SPI_SPEED 500000

// Send a command
void send_command(unsigned char command) {
    unsigned char buffer[2] = {0x00, command};  // 0x00 prefix for commands
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

// Send data
void send_data(unsigned char data) {
    unsigned char buffer[2] = {0x01, data};  // 0x01 prefix for data
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
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

    printf("Initializing display...\n");

    // Turn display on (DPCR Register 0x12)
    send_command(0x12);
    send_data(0x40);  // Bit 6 = 1 to turn on the display

    // Set color depth to 16bpp (MPWCTR Register 0x10)
    send_command(0x10);
    send_data(0x08);  // 16bpp color depth

    // Set resolution: 480x320
    send_command(0x14);  // Horizontal Width (HDWR)
    send_data(0x3F);     // (479 / 8) - 1 for 480 pixels

    send_command(0x1A);  // Vertical Height (low byte)
    send_data(0xDF);     // 320 - 1 (low byte)
    send_command(0x1B);  // Vertical Height (high byte)
    send_data(0x00);     // High byte is 0 for 320 pixels

    printf("Initialization complete!\n");

    return 0;
}
