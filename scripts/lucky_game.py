from mpl_toolkits import mplot3d
import random 
N = 10
C = 10

# data = [[[] for _ in range(C + 1)] for _ in range(N + 1)]

# def sim(n, c):
#   global data
#   iterations = 10000
#   for _ in range(iterations): 
#     people = [c for _ in range(n)]
#     turns = 0
#     left = n
#     while not any(person == n * c for person in people) : 
#       center = 0 
#       for i in range(n):  
#         if people[i]: 
#           people[i] -= 1
#           center += 1
#         elif people[i] is 0: 
#           people[i] = None
#           people[i], people[left - 1] = people[left - 1], people[i]
#           left -= 1
#       if left < 1: continue
#       winner = random.randint(0, left - 1)
#       people[winner] += center
#       turns += 1

#     data[n][c].append(turns)

# for n in range(1, N + 1): 
#   for c in range(1, C + 1): 
#     sim(n, c)
#     data[n][c] = sum(data[n][c]) / 10000.0
#   print (str(n / N * 100) + "% complete")


# print(data)

data = [[[], [], [], [], [], [], [], [], [], [], []], [[], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [[], 1.0, 4.0224, 9.0214, 15.9326, 24.7658, 36.6204, 49.0898, 64.2618, 82.3134, 98.9456], [[], 1.0, 8.1356, 19.7089, 35.3809, 56.0989, 80.3666, 111.6516, 147.6523, 187.949, 229.3465], [[], 1.0, 14.3663, 34.8348, 63.6572, 100.7299, 145.7847, 198.8804, 260.6665, 327.6051, 407.3888], [[], 1.0, 22.6444, 54.2938, 98.9776, 155.7757, 228.0005, 309.9628, 404.9402, 517.5966, 640.135], [[], 1.0, 32.9422, 80.5369, 144.0615, 225.2106, 329.9293, 447.012, 590.7891, 742.7223, 914.373], [[], 1.0, 44.9691, 108.5447, 194.4628, 308.6846, 453.3788, 611.6085, 810.0763, 1016.9255, 1266.1157], [[], 1.0, 58.314, 142.1653, 259.039, 403.538, 579.8754, 808.904, 1048.6363, 1326.1287, 1639.8777], [[], 1.0, 75.5654, 179.2686, 328.9666, 515.8791, 751.56, 1018.588, 1345.2816, 1685.4023, 2086.9396], [[], 1.0, 93.1368, 222.0048, 406.4562, 639.4706, 914.454, 1266.9436, 1667.6076, 2105.7318, 2607.7327]]

from mpl_toolkits import mplot3d
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

z = []
x = []
y = []

ax.set_xlabel('N')
ax.set_ylabel('C')
ax.set_zlabel('Expected Number of Turns')

for n in range(1, len(data)): 
  for c in range(1, len(data)): 
    x.append(n)
    y.append(c)
    z.append(data[n][c])
    print(n, c, data[n][c])
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

# ax.legend()

plt.show()
