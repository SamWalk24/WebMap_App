#tiles = "Stamen Terrain"
import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
info = list(data["NAME"] + ", " + data["LOCATION"]) 
elev = list(data["ELEV"])


def icon_color(elevation):
    if elevation < 1000:
        i_color = "green"
    elif 1000 <=  elevation < 3000:
        i_color = "orange"
    else:
        i_color = "red" 
    return i_color 



map = folium.Map(location=[34.01435,-118.49933], zoom_start=6, tiles="Stamen Terrain")



fgv = folium.FeatureGroup(name="Volvanoes")

for lt,ln,i,el in zip(lat,lon,info,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=2, popup=i+"; Elevation:"+ str(el), color=icon_color(el)))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 100000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map1.html")