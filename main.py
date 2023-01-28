import random
from antcolony import AntColony, Point

points = [Point(100 * random.random(), 100 * random.random()) for i in range(3)]
colony = AntColony(points)
colony.go(iters=10, DIS_COOF=1, A=4, B=4, Q=3, points=colony.points)