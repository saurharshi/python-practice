#include <graphics.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;
    int left, top, right, bottom;

    // Initialize the graphics mode
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");

    // Set the coordinates for the rectangle
    left = 150;
    top = 100;
    right = 350;
    bottom = 300;

    // Draw the rectangle
    rectangle(left, top, right, bottom);

    // Hold the output screen
    getch();

    // Close the graphics mode
    closegraph();

    return 0;
}
