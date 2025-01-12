#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL 0
#define SPI_SPEED 500000

void send_command(unsigned char command) {
    unsigned char buffer[2] = {0x00, command};
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

void send_data(unsigned char data) {
    unsigned char buffer[2] = {0x01, data};
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

void initialize_display() {
    send_command(0xFF);  // Example commands based on datasheet
    send_data(0x77);
    send_data(0x01);
    send_data(0x00);
    send_data(0x00);
    send_data(0x13);

    send_command(0x11);  // Exit Sleep Mode
    delay(120);          // Wait 120ms

    send_command(0x29);  // Display ON
    printf("Display initialized.\n");
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

    initialize_display();
    return 0;
}
