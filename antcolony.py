class Point():
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.edges = list()

    def add_edge(self, point):
        edge = Edge(self,point)
        self.edges.append(edge)
        point.edges.append(edge)

    def __repr__(self):
        return f'({self.x:.1f},{self.y:.1f})'

class Edge():
    def __init__(self, point1, point2, pheramon = 0.1):
        self.pher = pheramon
        self.points = (point1, point2)
        self.distance = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5
        self.t = 0.

    def add(self, value):
        self.t += value

    def go(self, coof):
        self.pher = coof * self.pher + self.t
        self.t = 0

class Ant():
    def __init__(self, point:Point):
        self.point = point

    def change_point(self, point:Point):
        self.point = point

    def go(self):
        pass

class AntColony():
    def __init__(self, points : list):
        self.points = points

    def add_point(self, point:Point):
        self.points+=point

    def add_ant(self):
        if self.points:
            self.ant = Ant(point= self.points[0])

    def change_ant_point_to_point(self, point:Point):
        self.ant.change_point(point)

    def go(self, iters, DIS_COOF, Q, A, B, show_result = True):
        pass