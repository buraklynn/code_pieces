from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
  def __init__(self, num_sides=6):
    self.num_sides = num_sides
    pass
  def roll(self):
    return randint(1, self.num_sides)



die = Die()

results = []

for roll_num in range(1000):
  result = die.roll()
  results.append(result)

frequencies = []

for side in range(1, die.num_sides+1):
  frequency = results.count(side)
  frequencies.append(frequency)

print(frequencies)

# VISUALIZATION

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Sonuç'}
y_axis_config = {'title': 'Sonucun frekansı'}
my_layout = Layout(title='Bir zarı altı kez atmak', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d6.html')


