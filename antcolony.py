import random
import matplotlib.pyplot as plt


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
    def go(self, coof):
        self.pher = coof * self.pher

class Ant():
    def __init__(self, point:Point):
        self.point = point
        self.distance = 0

    def change_point(self, point:Point, distance):
        self.distance += distance
        self.point = point


    def go(self, a, b, points, start_point):
        self.point = start_point
        meeted_edges = list()
        unmeeted_points = points.copy()
        unmeeted_points.remove(self.point)
        for j in range(len(unmeeted_points)):
            # поиск доступных эджей
            edges = list()
            for i in unmeeted_points:
                for k in i.edges:
                    if k.points[0] is self.point or k.points[1] is self.point:
                        edges.append(k)
            # j-я итерация
            probability = 0
            prob = list()
            for i in edges:
                p = i.pher**a * (1/i.distance)**b
                prob.append(p)
                probability += p
            for i in range(len(prob)):
                prob[i] = prob[i]/probability

            rn = random.random()
            for i in range(len(prob)):
                if sum(prob[0:i+1]) > rn:
                    point = edges[i].points[0] if not(edges[i].points[0] is self.point) else edges[i].points[1]
                    distance = edges[i].distance
                    meeted_edges.append(edges[i])
                    unmeeted_points.remove(point)
                    self.change_point(point, distance)
                    break
        edge = [i for i in start_point.edges if i.points[0] is self.point or i.points[1] is self.point][0]
        meeted_edges.append(edge)
        distance = edge.distance
        self.change_point(start_point, distance)
        return self.distance, meeted_edges

class AntColony():
    def __init__(self, points : list, make_links = True):
        temp = points.copy()
        i = 0
        while i < len(temp):
            if not type(temp[i]) is Point:
                print('Type other than Point encountered in array')
                temp.pop(i)
                i-=1
            else:
                i+=1
        self.points = temp
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

    def go(self, ants_count, iters, DIS_COOF, Q, A, B, show_result = True):
        # data checking:
        # types checking
        values = [ants_count, iters, DIS_COOF, Q, A, B]
        valid_types = [int, float]
        if show_result not in [False, True, int]:
            print('Invalid Bool Type Detected')
            show_result = True
        for i in range(len(values)):
            if type(values[i]) not in valid_types:
                print('Invalid Type Detected')
                try:
                    values[i] = int(values[i])
                except:
                    values[i] = 1
        ants_count, iters, DIS_COOF, Q, A, B = values

        # values checking
        if 100 < ants_count or ants_count < 0:
            print('Too many ants')
            ants_count = 10
        if 100 < iters or iters < 0:
            print('Too many iterations')
            iters = 10
        if 1.< DIS_COOF or DIS_COOF < 0:
            print('Incorrect evaporative coefficient')
            DIS_COOF = 0.36
        if 100 < Q or Q < 0:
            print('Too large or too small value for the pheramon accrual constant')
            Q = 0.5
        if 100 < A or A < -100:
            print('Too big or too small value for dependency constant')
            A = 2
        if 100 < B or B < -100:
            print('Too big or too small value for dependency constant')
            B = 4

        # ant algorithm:
        minimal_way = (1000000000000, None)
        edges = set()
        for i in self.points:
            edges.update(i.edges)
        for i in range(iters):
            ant_results = list()
            for k in range(ants_count):
                ant_results.append(self.ant.go(a=A, b=B, points=self.points, start_point=self.points[random.randrange(len(self.points))]))
                self.ant.distance = 0
            # убираем с каждой дорожки некий коэффициент DIS_COOF
            for k in edges:
                k.pher = k.pher*(1-DIS_COOF)
            # добавляем заслуженный феромон на пути
            for distance, ant_edges in ant_results:
                if distance < minimal_way[0]:
                    minimal_way = (distance,ant_edges)
                for edge in ant_edges:
                    edge.pher += Q/distance
        print(minimal_way)

        #показ данных на экране
        fig = plt.figure()
        for i in self.points:
            plt.scatter(i.x, i.y)
        for i in minimal_way[1]:
            p1, p2 = i.points[0], i.points[1]
            plt.plot([p1.x, p2.x],[p1.y,p2.y], c = 'gray')
        plt.text(100, 100, minimal_way[0])
        print(values)
        plt.show()

