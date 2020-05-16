import pygame

# Initialize the game class
pygame.init()

# Create a canvas on which to display everything
# define width=640, height=480
window = (640,480)

# Let pygame know that we are going to use this canvas
screen = pygame.display.set_mode(window)

# Create a surface with the same size as the window
background = pygame.Surface(window)

# Populate the surface with objects to be displayed
# Draw Rectangle on this background with color Green+Blue
# start from x=20, y=20 and size with x=40, y=40
pygame.draw.rect(background,(0,255,255),(20,20,40,40))

# Draw Rectangle on this background with color Red+Blue
# start from x=120, y=120 and size with x=50, y=50
pygame.draw.rect(background,(255,0,255),(120,120,50,50))


# Blit the surface onto the canvas ####
screen.blit(background,(0,0))

# Update the the display and wait
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

## Following lines for your reference
'''
pygame.draw.rect()
draw a rectangle
rect(surface, color, rect) -> Rect
rect(surface, color, rect, width=0, border_radius=0, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1) -> Rect
Draws a rectangle on the given surface.

Parameters:	
surface (Surface) -- surface to draw on
color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
rect (Rect) -- rectangle to draw, position and dimensions
width (int) --
(optional) used for line thickness or to indicate that the rectangle is to be filled (not to be confused with the width value of the rect parameter)

if width == 0, (default) fill the rectangle
if width > 0, used for line thickness
if width < 0, nothing will be drawn

Note When using width values > 1, the edge lines will grow outside the original boundary of the rect. For more details on how the thickness for edge lines grow, refer to the width notes of the pygame.draw.line()draw a straight line function.
border_radius (int) -- (optional) used for drawing rectangle with rounded corners. The supported range is [0, min(height, width) / 2], with 0 representing a rectangle without rounded corners.
border_top_left_radius (int) -- (optional) used for setting the value of top left border. If you don't set this value, it will use the border_radius value.
border_top_right_radius (int) -- (optional) used for setting the value of top right border. If you don't set this value, it will use the border_radius value.
border_bottom_left_radius (int) -- (optional) used for setting the value of bottom left border. If you don't set this value, it will use the border_radius value.
border_bottom_right_radius (int) --
(optional) used for setting the value of bottom right border. If you don't set this value, it will use the border_radius value.

if border_radius < 1 it will draw rectangle without rounded corners
if any of border radii has the value < 0 it will use value of the border_radius
If sum of radii on the same side of the rectangle is greater than the rect size the radii
will get scaled
Returns:	
a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the position of the given rect parameter and its width and height will be 0

Return type:	
Rect

Note The pygame.Surface.fill()fill Surface with a solid color method works just as well for drawing filled rectangles and can be hardware accelerated on some platforms with both software and hardware display modes.
Changed in pygame 2.0.0: Added support for keyword arguments.

Changed in pygame 2.0.0.dev8: Added support for border radius.

Comments 26
'''

'''
pygame.draw.line()
draw a straight line
line(surface, color, start_pos, end_pos, width) -> Rect
line(surface, color, start_pos, end_pos, width=1) -> Rect
Draws a straight line on the given surface. There are no endcaps. For thick lines the ends are squared off.

Parameters:	
surface (Surface) -- surface to draw on
color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)
end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)
width (int) --
(optional) used for line thickness

if width >= 1, used for line thickness (default is 1)
if width < 1, nothing will be drawn

Note When using width values > 1, lines will grow as follows.
For odd width values, the thickness of each line grows with the original line being in the center.

For even width values, the thickness of each line grows with the original line being offset from the center (as there is no exact center line drawn). As a result, lines with a slope < 1 (horizontal-ish) will have 1 more pixel of thickness below the original line (in the y direction). Lines with a slope >= 1 (vertical-ish) will have 1 more pixel of thickness to the right of the original line (in the x direction).

Returns:	
a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the start_pos parameter value (float values will be truncated) and its width and height will be 0

Return type:	
Rect

Raises:	
TypeError -- if start_pos or end_pos is not a sequence of two numbers

Example :
    pygame.draw.line(Surface, (R,G,B), (x1, y1), (x2, y2))

'''
