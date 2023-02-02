import random
from antcolony import AntColony, Point

points = [Point(100 * random.random(), 100 * random.random()) for i in range(24)] + ['abpb']
colony = AntColony(points)
colony.go(ants_count='abpba',iters=5, DIS_COOF=0.36, A=2, B=4, Q=0.5)