import random
from antcolony import AntColony, Point

points = [Point(100 * random.random(), 100 * random.random()) for i in range(100)]
colony = AntColony(points)


