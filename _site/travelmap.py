# Add markers and route lines, as you did previously
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
    "8. Dali, China": [25.6939, 100.1619],
    "9. Lijiang, China": [26.8721, 100.2257],
    "10. Shangri-La, China": [27.8252, 99.7074],
    "11. Chengdu, China": [30.5728, 104.0668],
    "12. Xi'an, China": [34.3416, 108.9398],
    "13. Urumqi, China": [43.8256, 87.6168],
    "14. Turpan, China": [42.9513, 89.1897],
    "15. Kashgar, China": [39.4704, 75.9898],
    "16. Osh, Kyrgyzstan": [40.5283, 72.7985],
    "17. Bishkek, Kyrgyzstan": [42.8746, 74.5698],
    "18. Almaty, Kazakhstan": [43.2220, 76.8512],
    "19. Tashkent, Uzbekistan": [41.2995, 69.2401],
    "20. Samarkand, Uzbekistan": [39.6542, 66.9597],
    "21. Bukhara, Uzbekistan": [39.7747, 64.4286],
    "22. Dushanbe, Tajikistan": [38.5598, 68.7870],
}

# Add markers for each location with labels
for place, coords in all_locations.items():
    folium.Marker(location=coords, popup=place).add_to(auto_center_map)

# Automatically center and zoom to fit all markers
auto_center_map.fit_bounds([coords for coords in all_locations.values()])

# Save the map to an HTML file
auto_center_map.save('AutoCentered_Map_Route.html')

