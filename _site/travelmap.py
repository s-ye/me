import folium

# Initialize map without specifying center and zoom
auto_center_map = folium.Map()

# Define all locations with coordinates and labels
all_locations = {
    # South China
    "1. Hong Kong": [22.3193, 114.1694],
    "2. Shenzhen, China": [22.5431, 114.0579],
    "3. Guangzhou, China": [23.1291, 113.2644],

    # South-Central China
    "4. Nanning, China": [22.8170, 108.3669],
    "5. Guilin, China": [25.2744, 110.2900],
    "6. Kunming, China": [24.8801, 102.8329],
    
    # Yunnan Province Cluster
    "7. Dali, China": [25.6939, 100.1619],
    "8. Lijiang, China": [26.8721, 100.2257],
    "9. Shangri-La, China": [27.8252, 99.7074],
    
    # Central and Southwest China
    "10. Chongqing, China": [29.5630, 106.5516],
    "11. Chengdu, China": [30.5728, 104.0668],
    
    # North-Central China
    "12. Xi’an, China": [34.3416, 108.9398],
    "13. Pingyao, China": [37.1987, 112.1784],
    "14. Datong, China": [40.0768, 113.3001],
    "15. Mount Wutai, China": [39.0585, 113.5931],
    "16. Shijiazhuang, China": [38.0428, 114.5149],
    
    # Beijing to Shanghai Route
    "17. Beijing, China": [39.9042, 116.4074],
    "18. Qufu, China": [35.5964, 116.9919],
    "19. Mount Tai, China": [36.2506, 117.1018],
    "20. Qingdao, China": [36.0671, 120.3826],
    "21. Nanjing, China": [32.0603, 118.7969],
    "22. Shanghai, China": [31.2304, 121.4737],
    "23. Fuzhou, China": [26.0765, 119.2911],
    "24. Xiamen, China": [24.4798, 118.0894],
    
    # West China (Xinjiang)
    "25. Urumqi, China": [43.8256, 87.6168],
    "26. Turpan, China": [42.9513, 89.1897],
    "27. Kashgar, China": [39.4704, 75.9898],

    "Mount Kailash, Tibet": [31.0685, 81.3104],
    "Lake Manasarovar, Tibet": [30.6476, 81.4634],
    "Darchen, Tibet": [30.9650, 81.3189],
    "Pulan County (Burang), Tibet": [30.2972, 81.2464],
    "Hilsa, Nepal": [30.0381, 81.1750],

    "28. Lhasa, China (Tibet)": [29.6520, 91.1721],  # Tibet's capital
    "29. Shigatse, China (Tibet)": [29.2682, 88.8806],  # Major city near Everest
    # Add Indian cities after crossing
    # "30. Leh, India": [34.1526, 77.5771],  # A major town in northern India
    # "31. Srinagar, India": [34.0837, 74.7973],  # Capital of Jammu and Kashmir
    # "32. Delhi, India": [28.6139, 77.2090],  # India’s capital
    "Kathmandu, Nepal": [27.7172, 85.3240],  # Nepal's capital
    "Lumbini, Nepal": [27.4695, 83.2750],
    "Varanasi, India": [25.3176, 82.9739],
    "Agra, India": [27.1751, 78.0421],  # Taj Mahal location
    "Jaipur, India": [26.9124, 75.7873],
    "Delhi, India": [28.6139, 77.2090],  # India’s capital

}

# Add all locations to the map
for location, coordinates in all_locations.items():
    folium.Marker(location=coordinates, popup=location).add_to(auto_center_map)

# Add edges from i to i+1
locations_list = list(all_locations.values())
for i in range(len(locations_list) - 1):
    folium.PolyLine(locations_list[i:i+2], color="blue", weight=2.5, opacity=1).add_to(auto_center_map)

# Save map to HTML file
auto_center_map.save("AutoCentered_Map_Route.html")

