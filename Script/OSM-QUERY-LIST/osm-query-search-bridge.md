```
/*
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
*/
[out:json][timeout:25];
// gather results
nwr["bridge"="yes"]({{bbox}});
// print results
out geom;
```
