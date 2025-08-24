import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
  rw = RandomWalk(50_000)
  rw.fill_walk()

  plt.style.use('classic')
  fig, ax = plt.subplots(figsize=(10,6),dpi=128)
  point_number = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=15)
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  # ax.set_aspect('equal')
  plt.show()

  keep_running = input('Make another walk? (y/n): ')
  if keep_running == 'n':
    break
  