class Point():
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.edges = list()

    def link(self, point):
        is_empty = True
        for i in self.edges:
            i = i.points
            if self in i and point in i:
                is_empty = False
        for i in point.edges:
            i = i.points
            if self in i and point in i:
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
    def go(self, coof):
        self.pher = coof * self.pher

class Ant():
    def __init__(self, point:Point):
        self.point = point

    def change_point(self, point:Point):
        self.point = point

    def go(self):
        pass

class AntColony():
    def __init__(self, points : list, make_links = True):
        self.points = points
        if make_links:
            self.link_points()

    def add_point(self, point:Point):
        self.points+=point

    def link_points(self):
        for i in self.points:
            for k in self.points:
                i.link(k)

    def add_ant(self):
        if self.points:
            self.ant = Ant(point= self.points[0])

    def change_ant_position_to_point(self, point:Point):
        self.ant.change_point(point)

    def go(self, iters, DIS_COOF, Q, A, B, show_result = True):
        pass