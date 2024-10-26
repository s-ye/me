import folium

# Initialize map without specifying center and zoom
auto_center_map = folium.Map()

# Define all locations with coordinates and labels
all_locations = {
    # Southeast Asia
    "1. Bangkok, Thailand": [13.7563, 100.5018],
    "2. Chiang Mai, Thailand": [18.7883, 98.9853],
    "3. Hanoi, Vietnam": [21.0285, 105.8542],
    "4. Ha Long Bay, Vietnam": [20.9101, 107.1839],
    
    # South China
    "5. Nanning, China": [22.8170, 108.3669],
    "6. Guilin, China": [25.2744, 110.2900],
    "7. Kunming, China": [24.8801, 102.8329],
    
    # Yunnan Province Cluster
    "8. Dali, China": [25.6939, 100.1619],
    "9. Lijiang, China": [26.8721, 100.2257],
    "10. Shangri-La, China": [27.8252, 99.7074],
    
    # Central and Southwest China
    "11. Chongqing, China": [29.5630, 106.5516],
    "12. Chengdu, China": [30.5728, 104.0668],
    
    # North-Central China
    "13. Xi’an, China": [34.3416, 108.9398],
    "14. Pingyao, China": [37.1987, 112.1784],
    "15. Datong, China": [40.0768, 113.3001],
    "16. Mount Wutai, China": [39.0585, 113.5931],
    "17. Shijiazhuang, China": [38.0428, 114.5149],
    
    # Beijing to Shanghai Route
    "18. Beijing, China": [39.9042, 116.4074],
    "19. Qufu, China": [35.5964, 116.9919],          # New addition
    "20. Mount Tai, China": [36.2506, 117.1018],     # New addition
    "21. Nanjing, China": [32.0603, 118.7969],       # New addition
    "22. Shanghai, China": [31.2304, 121.4737],
    
    # West China (Xinjiang)
    "23. Urumqi, China": [43.8256, 87.6168],
    "24. Turpan, China": [42.9513, 89.1897],
    "25. Kashgar, China": [39.4704, 75.9898],
    
    # Central Asia
    "26. Osh, Kyrgyzstan": [40.5283, 72.7985],
    "27. Bishkek, Kyrgyzstan": [42.8746, 74.5698],
    "28. Almaty, Kazakhstan": [43.2220, 76.8512],
    "29. Tashkent, Uzbekistan": [41.2995, 69.2401],
    "30. Samarkand, Uzbekistan": [39.6542, 66.9597],
    "31. Bukhara, Uzbekistan": [39.7747, 64.4286],
    "32. Dushanbe, Tajikistan": [38.5598, 68.7870],
}


# Convert dictionary to list of coordinates to ensure ordered path
location_coords = list(all_locations.values())

# Add markers for each location with labels
for place, coords in all_locations.items():
    folium.Marker(location=coords, popup=place).add_to(auto_center_map)

# Draw path lines between consecutive points
for i in range(len(location_coords) - 1):
    folium.PolyLine([location_coords[i], location_coords[i + 1]], color="blue", weight=2.5, opacity=0.8).add_to(auto_center_map)

# Automatically center and zoom to fit all markers
auto_center_map.fit_bounds([coords for coords in location_coords])

# Save the map to an HTML file
auto_center_map.save('AutoCentered_Map_Route.html')
