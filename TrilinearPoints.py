import pygame
import math

pygame.init()

h = int(255*3)
# https://en.wikipedia.org/wiki/Equilateral_triangle#Principal_properties. Distance side to center = h/3
l = 2/math.sqrt(3) * h

screen = pygame.display.set_mode((int(l), int(h)))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
mainloop = True
selected_point = None


def find_point(points, x, y):
    for p in points:
        if math.hypot(p.x - x, p.y - y) <= p.size:
            return p
    return None


class Point:
    def __init__(self, x_y, size, color):
        x, y = x_y
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)

x_shift = 0
y_shift = 0

pointR = Point((0 + x_shift, h + y_shift), 20, (255, 0, 0))
pointG = Point((.5 * l + x_shift, 0 + y_shift), 20, (0, 255, 0))
pointB = Point((l + x_shift, h + y_shift), 20, (0, 0, 255))
pointP = Point((.5 * l + x_shift, int(2 / 3 * h)+y_shift), 20, (0, 0, 0))
# https://en.wikipedia.org/wiki/Equilateral_triangle#Principal_properties ; geometric center

my_points = [pointR, pointG, pointB, pointP]
for point in my_points:
    point.display()
pygame.display.flip()


def dist_from_line(p1, p2, point_p):
    if p2[1] == p1[1] and p2[0] == p1[0]:
        return 0
    else:
        # https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
        numerator = ((p2[1] - p1[1]) * point_p[0]) - ((p2[0] - p1[0]) * point_p[1]) + (p2[0] * p1[1]) - (p2[1] * p1[0])
        denominator = math.sqrt(((p2[1] - p1[1]) ** 2) + ((p2[0] - p1[0]) ** 2))
        return math.fabs(numerator / denominator)

while mainloop:
    sc_f = 1  # optional scale factor
    Tri1 = min(float(255), (dist_from_line((pointG.x, pointG.y), (pointB.x, pointB.y), (pointP.x, pointP.y))) * sc_f)
    Tri2 = min(float(255), (dist_from_line((pointB.x, pointB.y), (pointR.x, pointR.y), (pointP.x, pointP.y))) * sc_f)
    Tri3 = min(float(255), (dist_from_line((pointR.x, pointR.y), (pointG.x, pointG.y), (pointP.x, pointP.y))) * sc_f)

    for event in pygame.event.get():
        # mouse button position and button clicking
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            # debug tool
            elif event.key == pygame.K_SPACE:
                print(Tri1, Tri2, Tri3)
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_point = find_point(my_points, mouseX, mouseY)
        if event.type == pygame.MOUSEBUTTONUP:
            selected_point = None

    if selected_point:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        selected_point.x = mouseX
        selected_point.y = mouseY
        for point in my_points:
            point.display()
            pygame.display.flip()
    screen.fill((255, 255, 255))
    ColorSquare = pygame.draw.rect(background, (Tri1, Tri2, Tri3), (0, 0, 50, 50))
    screen.blit(background, (0, 0))
    pygame.display.set_caption("Points")
pygame.quit()
