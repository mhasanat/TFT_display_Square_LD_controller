#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL 0
#define SPI_SPEED 500000  // 500 kHz SPI speed

// Send a command to the LT7680
void send_command(unsigned char command) {
    unsigned char buffer[2] = {0x00, command};  // 0x00 prefix for commands
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

// Send data to the LT7680
void send_data(unsigned char data) {
    unsigned char buffer[2] = {0x01, data};  // 0x01 prefix for data
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

// Draw a circle function
void draw_circle() {
    // Set major radius (50 pixels)
    send_command(0x77);  // Major Radius Low Byte
    send_data(50 & 0xFF);  // Low byte of radius
    send_command(0x78);  // Major Radius High Byte
    send_data((50 >> 8) & 0x1F);  // High byte (only bits 0-4 used)

    // Set minor radius (50 pixels for a circle)
    send_command(0x79);  // Minor Radius Low Byte
    send_data(50 & 0xFF);  // Low byte of radius
    send_command(0x7A);  // Minor Radius High Byte
    send_data((50 >> 8) & 0x1F);  // High byte (only bits 0-4 used)

    // Set center X coordinate (160)
    send_command(0x7B);  // Center X Low Byte
    send_data(160 & 0xFF);
    send_command(0x7C);  // Center X High Byte
    send_data((160 >> 8) & 0x1F);

    // Set center Y coordinate (120)
    send_command(0x7D);  // Center Y Low Byte
    send_data(120 & 0xFF);
    send_command(0x7E);  // Center Y High Byte
    send_data((120 >> 8) & 0x1F);

    // Configure and start drawing
    send_command(0x76);  // Draw Control Register
    send_data(0xC0);  // Start drawing (Bit 7), Fill (Bit 6), Shape (00 for circle/ellipse)

    printf("Circle drawing command sent.\n");
}

int main() {
    // Initialize WiringPi and SPI
    if (wiringPiSetup() == -1) {
        printf("WiringPi setup failed.\n");
        return 1;
    }
    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed.\n");
        return 1;
    }

    printf("Drawing a circle...\n");
    draw_circle();

    printf("Done.\n");
    return 0;
}
