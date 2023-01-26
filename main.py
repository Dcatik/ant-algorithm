import random
import math
import matplotlib.pyplot as plt

# начальные данные
pheramon = .2

# Определяем класс Точка и Ребро
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
    def __init__(self, point1, point2, pheramon = pheramon):
        self.pher = pheramon
        self.points = (point1, point2)
        self.distance = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5
        self.t = 0.
    def add(self, value):
        self.t += value
    def go(self, coof):
        self.pher = coof * self.pher + self.t
        self.t = 0

# создаем точки
maxy,maxx = 100, 100
points = []
for i in range(25):
    points.append(Point(-maxx * random.random() + maxx, -maxy * random.random() + maxy))
# создаем грани
c_o_p = len(points)

pinned_points = []
for i in range(c_o_p):
    for j in range(c_o_p):
        if not points[i] is points[j]:
            if not (i, j) in pinned_points and not (j, i) in pinned_points:
                points[i].add_edge(points[j])
                pinned_points.append((i,j))

links = set()
for i in range(c_o_p):
    for j in range(len(points[i].edges)):
        links.add(points[i].edges[j])
# муравьиный алгоритм
DIS_COOF = 1 - 0.36
Q = 4
A = 1
B = 2

q = 5

minimal_way = float(100000000000000)
minimal_way_points = []
for i in range(10): # итерации
    for j in range(10): # муравьи
        # итерация 1 муравья
        distance = 0.
        curent_point = points[random.randrange(0, len(points))]
        meeted_points = []
        print(points)
        unmeeted_points = points.copy()
        print(unmeeted_points)
        while unmeeted_points:
            edges = curent_point.edges.copy()

            for unchecked in edges:
                if unchecked.points[0] in meeted_points and unchecked.points[1] in meeted_points:
                    del edges[edges.index(unchecked)]

            prob = []
            # сумма вероятностей
            for w in range(len(edges)):
                prob.append((edges[w].pher ** A) * ((1 / edges[w].distance) ** B))
            sum_prob = sum(prob)
            # находим вероятность для каждой отдельной точки
            for w in range(len(prob)):
                prob[w] = prob[w] / sum_prob
            # находим рандомное число
            rnd_number = random.random()
            # находим индекс ребра, куда мы попали
            prb = 0.
            ind = 0
            while prb + prob[ind] < rnd_number:
                prb += prob[ind]
                ind += 1
            meeted_points.append(curent_point)
            distance += edges[ind].distance
            if curent_point is edges[ind].points[0]:
                curent_point = edges[ind].points[1]
            elif curent_point is edges[ind].points[1]:
                curent_point = edges[ind].points[0]
            else:print('error')

        if distance < minimal_way:
            minimal_way = distance
            minimal_way_points = meeted_points

        _t = Q / distance
        for k in links:
            k.add(_t)
    for edge in links:
        edge.go(DIS_COOF)


for i in range(len(points)-1, -1, -1):
    if len(points[i].edges) != 49:
        print('error')
        print('Total Error')




# отображаем точки
fig, ax = plt.subplots()
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
for i in range(c_o_p):
    x,y = points[i].x, points[i].y
    ax.scatter(x,y)
    ax.text(x, y + 1.5, f'{i}')
# отображем грани
for i in links:
    x,y, x1, y1 = i.points[0].x, i.points[0].y, i.points[1].x, i.points[1].y
    ax.plot([x,x1], [y,y1], c='green', alpha = 1/(int(1/1 + math.e ** -i.pher) * 100))
    # ax.text((x + x1)/2, (y + y1)/2, f'{i.distance:.2f}', size = 12, alpha = 0.5) # дистанция между точками
    print(i.pher)

print(minimal_way)
print(minimal_way_points)
print(len(minimal_way_points))
for i in range(len(minimal_way_points) - 1):
    p1, p2 = minimal_way_points[i], minimal_way_points[i+1]
    x, y, x1, y1 = p1.x, p1.y, p2.x, p2.y
    ax.plot([x, x1], [y, y1], c='black')
plt.show()
