Requires both Python 3.6 and pygame to run
http://www.pygame.org/wiki/GettingStarted#Pygame%20Installation

The points colored as Red, Green, and Blue form a triangle. 
The minimum distance from the Black point to the extended sides of the triangle are calculated.
The minimum distances form a coordinate, known as a trilinear coordinate.
The trilinear coordinate is then mapped to a color, shown at the top left corner of the screen.

Each point can be dragged.
Pressing Spacebar will print the coordinate in the console as a way to debug.

The following tutorial was interesting and instrumental in making this. 
http://www.petercollingridge.co.uk/pygame-physics-simulation/creating-pygame-window

Refer to the following for the math:
https://en.wikipedia.org/wiki/Trilinear_coordinates
https://en.wikipedia.org/wiki/Equilateral_triangle - the starting shape is an equilateral triangle with the Black point in the geometric center. 
This is so that the starting trilinear point is (255,255,255) = White