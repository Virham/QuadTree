import pygame


class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity

        self.points = []
        self.subTrees = None

    def divide(self):
        self.subTrees = []

        halfW = self.boundary.w / 2
        halfH = self.boundary.h / 2

        self.subTrees.append(
            QuadTree(pygame.Rect(self.boundary.x, self.boundary.y, halfW, halfH), self.capacity))
        self.subTrees.append(
            QuadTree(pygame.Rect(self.boundary.x + halfW, self.boundary.y, halfW, halfH), self.capacity))
        self.subTrees.append(
            QuadTree(pygame.Rect(self.boundary.x, self.boundary.y + halfH, halfW, halfH), self.capacity))
        self.subTrees.append(
            QuadTree(pygame.Rect(self.boundary.x + halfW, self.boundary.y + halfH, halfW, halfH), self.capacity))

    def add(self, point):
        if self.boundary.collidepoint(point):
            self.points.append(point)

            if len(self.points) >= self.capacity:
                if not self.subTrees:
                    self.divide()
                    for point in self.points:
                        for tree in self.subTrees:
                            tree.add(point)

                    return

                for subTree in self.subTrees:
                    subTree.add(point)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), self.boundary, self.capacity)

        if not self.subTrees:
            return

        for tree in self.subTrees:
            tree.draw(win)


