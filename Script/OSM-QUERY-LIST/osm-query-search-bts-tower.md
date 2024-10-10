![image](https://github.com/user-attachments/assets/5e5f1eba-09d9-4f11-b41e-88319c0a09bf)

````
/*
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
*/
[out:json][timeout:25];
// gather results
nwr["tower:type"="communication"]({{bbox}});
// print results
out geom;
````

### Script by Dhukera OSINT Mindset 

```
{{geocodeArea:<change your area>}}->.searchArea;

node["man_made"="tower"]["tower:type"="communication"](area.searchArea) -> .tower;

way["power"="line"](around.tower:200) -> .tower_line;

way["building"="yes"](around.tower_line:50) -> .tower_line_building;

way["amenity"="parking"]["parking"="street_side"](around.tower_line_building:30);

out;
>;
out skel;
```

