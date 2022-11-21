import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


file = 're_eq_data.json'
with open(file) as f:
  all_eq_data = json.load(f)

map_title = all_eq_data['metadata']['title']+(f" ({all_eq_data['metadata']['count']} points)")

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_text = [], [], [], []
for i in range(len(all_eq_dicts)):
  mags.append(all_eq_dicts[i]['properties']['mag'])
  lons.append(all_eq_dicts[i]['geometry']['coordinates'][0])
  lats.append(all_eq_dicts[i]['geometry']['coordinates'][1])
  hover_text.append(all_eq_dicts[i]['properties']['title'])

#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
  'type': 'scattergeo',
  'lon': lons,
  'lat': lats,
  'text': hover_text,
  'marker': {
    'size': [5*mag for mag in mags],
    'color': mags,
    'colorscale': 'Rainbow',
    'reversescale': True,
    'colorbar': {
      'title': 'Magnitude'
    }
  }
}]
my_layout = Layout(title=map_title)

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')





