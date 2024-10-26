import folium

# Initialize map without specifying center and zoom
auto_center_map = folium.Map()

# Define all locations with coordinates and labels
all_locations = {
    "1. Bangkok, Thailand": [13.7563, 100.5018],
    "2. Chiang Mai, Thailand": [18.7883, 98.9853],
    "3. Hanoi, Vietnam": [21.0285, 105.8542],
    "4. Ha Long Bay, Vietnam": [20.9101, 107.1839],
    "5. Nanning, China": [22.8170, 108.3669],
    "6. Guilin, China": [25.2744, 110.2900],
    "7. Kunming, China": [24.8801, 102.8329],
    "8. Chongqing, China": [29.5630, 106.5516],
    "9. Chengdu, China": [30.5728, 104.0668],
    "10. Dali, China": [25.6939, 100.1619],
    "11. Lijiang, China": [26.8721, 100.2257],
    "12. Shangri-La, China": [27.8252, 99.7074],
    "13. Xi'an, China": [34.3416, 108.9398],
    "14. Beijing, China": [39.9042, 116.4074],
    "15. Shanghai, China": [31.2304, 121.4737],
    "16. Urumqi, China": [43.8256, 87.6168],
    "17. Turpan, China": [42.9513, 89.1897],
    "18. Kashgar, China": [39.4704, 75.9898],
    "19. Osh, Kyrgyzstan": [40.5283, 72.7985],
    "20. Bishkek, Kyrgyzstan": [42.8746, 74.5698],
    "21. Almaty, Kazakhstan": [43.2220, 76.8512],
    "22. Tashkent, Uzbekistan": [41.2995, 69.2401],
    "23. Samarkand, Uzbekistan": [39.6542, 66.9597],
    "24. Bukhara, Uzbekistan": [39.7747, 64.4286],
    "25. Dushanbe, Tajikistan": [38.5598, 68.7870],
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
