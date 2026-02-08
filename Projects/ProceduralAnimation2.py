import numpy as np
import pygame as pg
import pygame.time


class Segment:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.pos = (x, y)


class Animal:
    def __init__(self, segmentArr, distanceArr):
        self.segmentArr = segmentArr
        self.distanceArr = distanceArr

    def draw(self):
        indexes = 0
        x = 0
        for segment in self.segmentArr:
            indexes+=1
        for segment in self.segmentArr:
            pg.draw.circle(screen, (60, 60, 60), segment.pos, segment.radius)
            if x != indexes-1:
                pg.draw.line(screen, (60, 60, 60), segment.pos, self.segmentArr[x+1].pos, 2)
                distance = np.sqrt(abs(self.segmentArr[x+1].pos[0] - segment.pos[0])**2 + abs(self.segmentArr[x+1].pos[1] - segment.pos[1])**2)
                distance = float(distance)
                self.distanceArr.append(distance)
            x += 1


    def FabrikF(self, target):


        pg.draw.circle(screen, (60, 60, 60), (target[0], target[1]), self.segmentArr[0].radius)

        index = 0
        total_segments = 0
        for segment in self.segmentArr:
            total_segments +=1
        for segment in self.segmentArr:
            if segment != self.segmentArr[0]:
                distance = np.sqrt(abs(self.segmentArr[index + 1].pos[0] - segment.pos[0]) ** 2 + abs(self.segmentArr[index + 1].pos[1] - segment.pos[1]) ** 2)
                print(distance)
                theta = np.arcsin(segment.pos[1]-self.segmentArr[index-1].pos[1]/distance)
                newy = np.sin(theta)*(distance - self.distanceArr[index-1])+self.segmentArr[index].pos[1]
                newx = np.cos(theta) * (distance - self.distanceArr[index - 1]) + self.segmentArr[index].pos[0]
                pg.draw.circle(screen, (60, 60, 60), (newx, newy),self.segmentArr[0].radius)
    def FabrikB(self):
        pass


    def connect(self):

        self.FabrikF(None)
        self.FabrikB()

pg.init()

running = True
WIDTH = 1280
HEIGHT = 720
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

segment3 = Segment(WIDTH*0.5, 0, 20)
segment2 = Segment(WIDTH*0.5, 200, 20)
segment1 = Segment(WIDTH*0.5, 400, 20)

newAnimal = Animal([segment1,
                    segment2,
                    segment3], [20, 20])

while running:

    for event in pg.event.get():
        print(event)
        if event.type == pg.QUIT:
            running = False

    mousex, mousey = pg.mouse.get_pos()
    newAnimal.FabrikF((mousex, mousey))
    pg.display.flip()
pg.quit()