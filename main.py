import random
from antcolony import AntColony, Point

points = [Point(100 * random.random(), 100 * random.random()) for i in range(100)]
colony = AntColony(points)
colony.go(ants=10,iters=50, DIS_COOF=0.36, A=2, B=4, Q=0.5)