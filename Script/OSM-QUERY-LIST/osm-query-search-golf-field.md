```
[out:json][timeout:15];

(
  // Lapangan golf spot ani ani 
  node["leisure"="golf_course"]( -6.37,106.68,-6.08,107.00 );
  way["leisure"="golf_course"]( -6.37,106.68,-6.08,107.00 );

  node["golf"="driving_range"]( -6.37,106.68,-6.08,107.00 );
  way["golf"="driving_range"]( -6.37,106.68,-6.08,107.00 );
);

out center tags;
```