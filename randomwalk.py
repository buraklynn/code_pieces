from random import choice
import matplotlib.pyplot as plt


class RandomWalk:

  def __init__(self, numpoint=5000):
    self.numpoint = numpoint
    pass

  def createpoint(self):
    self.x_point = [0]
    self.y_point = [0]

    while len(self.x_point) < self.numpoint:
      x_yon = choice([-1, 1])
      x_mesafe = choice([1, 2, 3])
      x_deger = x_yon * x_mesafe

      y_yon = choice([-1 ,1])
      y_mesafe = choice([1, 2, 3])
      y_deger = y_yon * y_mesafe

      x = self.x_point[-1] + x_deger
      y = self.y_point[-1] + y_deger

      self.x_point.append(x)
      self.y_point.append(y)

while True:

  yuru = RandomWalk()
  yuru.createpoint()

  plt.style.use('classic')
  fig, ax = plt.subplots()
  point_num = range(yuru.numpoint)
  ax.scatter(yuru.x_point, yuru.y_point, s=1, c=point_num, cmap=plt.cm.Blues, edgecolors='none' )
  ax.scatter(yuru.x_point[0], yuru.y_point[0], c="red", edgecolors='none', s=10)
  ax.scatter(yuru.x_point[-1], yuru.y_point[-1], c="blue", edgecolors='none', s=10)
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  ax.set_title("Random Walk")
  plt.show()

