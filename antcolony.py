import random
import matplotlib


class Point():
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.edges = list()

    def view_pos(self):
        for i in self.edges:
            print(i.distance)
    def link(self, point):
        is_empty = True
        for i in self.edges:
            if self in i.points and point in i.points:
                is_empty = False
        for i in point.edges:
            if self in i.points and point in i.points:
                is_empty = False
        if is_empty:
            edge = Edge(self, point)
            self.edges.append(edge)
            point.edges.append(edge)

    def __repr__(self):
        return f'({self.x:.1f},{self.y:.1f})'

class Edge():
    def __init__(self, point1, point2, pheramon = 0.1):
        self.pher = pheramon
        self.points = (point1, point2)
        self.distance = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5
        print(self.distance)
    def go(self, coof):
        self.pher = coof * self.pher

class Ant():
    def __init__(self, point:Point):
        self.point = point

    def change_point(self, point:Point):
        self.point = point

    def go(self, a, b, points):
        unmeeted_edges = self.point.edges.copy()
        for j in range(len(points)):
            # j-я итерация
            probability = 0
            prob = list()
            for i in unmeeted_edges:
                p = i.pher**a * (1/i.distance)**b
                prob.append(p)
                probability += p
            for i in range(len(prob)):
                prob[i] = prob[i]/probability

            rn = random.random()
            for i in range(len(prob)):
                if sum(prob[0:i+1]) > rn:
                    point = self.point.edges[i].points[0] if not(self.point.edges[i].points[0] is self.point) else self.point.edges[i].points[1]
                    unmeeted_edges.remove(point)
                    self.change_point(point)
                    print(point)

class AntColony():
    def __init__(self, points : list, make_links = True):
        self.points = points
        if make_links:
            self.link_points()
        self.add_ant()

    def add_point(self, point:Point):
        self.points+=point

    def link_points(self):
        for i in self.points:
            for k in self.points:
                if not i is k:
                    i.link(k)

    def add_ant(self):
        if self.points:
            self.ant = Ant(point= self.points[0])

    def go(self, iters, DIS_COOF, Q, A, B,points, show_result = True):
        self.ant.go(a=A, b=B, points=points)