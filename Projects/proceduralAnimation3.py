import numpy as np
import pygame as pg
import math
#The fabrik algorithm works by moving the first point to the target,
#then along the line from the next point to the point at the target, we move the second point to the distance it should be from the first point.
#We repeat these processes for all the points, and then we do it in reverse, to the anchor point. It eventually will be optimising for a straight line,
#so "fabriks" per second is a large question.

#for clarity, easy of reading and ease of life for the developer, I have separated FABRIK into FABRIKF and FARBIKB

#"Constants"


WIDTH, HEIGHT = 1280, 640

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Procedural Animation, with FABRIK algorithm")


RUNNING = True

COLOR = (100, 60, 100)

#classes/methods


class Segment:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.pos = (x, y)

    def draw(self):
        pg.draw.circle(SCREEN, COLOR, self.pos, self.radius)

class Animal:

    def __init__(self, segmentArr, distanceArr):
        self.distanceArr = distanceArr
        self.segmentArr = segmentArr

    def FABRIKF(self, targetx, targety):
        segment_array_index = 1
        for segment in self.segmentArr:
            if segment == self.segmentArr[0]:
                pg.draw.circle(SCREEN, COLOR, (targetx, targety), 20)
                self.segmentArr[0].pos = (targetx, targety)
            else:

                distance = np.sqrt(abs(self.segmentArr[segment_array_index-1].pos[0] - segment.pos[0]) ** 2 + abs(self.segmentArr[segment_array_index-1].pos[1] - segment.pos[1]) ** 2)
                theta = math.degrees(math.atan2(-(self.segmentArr[segment_array_index-1].pos[1] - segment.pos[1]),  (self.segmentArr[segment_array_index-1].pos[0] - segment.pos[0])))

                pg.draw.line(SCREEN, COLOR, segment.pos, self.segmentArr[segment_array_index-1].pos)


                
                segment_array_index += 1

    def FABRIKB(self):
        pass


#body

segment1 = Segment(400, 400, 20)
segment2 = Segment(400, 400, 20)
segment3 = Segment(100, 100, 20)
animal = Animal([segment1, segment2], None)

while RUNNING:
    SCREEN.fill((100, 100, 100))

    mousex, mousey = pg.mouse.get_pos()
    animal.FABRIKF(mousex, mousey)

    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False


pg.quit()