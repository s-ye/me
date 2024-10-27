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
    
    # Central Asia
    "28. Osh, Kyrgyzstan": [40.5283, 72.7985],
    "29. Bishkek, Kyrgyzstan": [42.8746, 74.5698],
    "30. Almaty, Kazakhstan": [43.2220, 76.8512],
    "31. Tashkent, Uzbekistan": [41.2995, 69.2401],
    "32. Samarkand, Uzbekistan": [39.6542, 66.9597],
    "33. Bukhara, Uzbekistan": [39.7747, 64.4286],
    "34. Dushanbe, Tajikistan": [38.5598, 68.7870],
}

# Add all locations to the map
for location, coordinates in all_locations.items():
    folium.Marker(location=coordinates, popup=location).add_to(auto_center_map)

# Save map to HTML file
auto_center_map.save("AutoCentered_Map_Route.html")

