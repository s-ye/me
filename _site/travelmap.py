import folium
import geopandas as gpd


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
    "13. Luoyang, China": [34.6587, 112.4249],       # Henan, near Xi'an
    "14. Zhengzhou, China": [34.7466, 113.6254],     # Henan, capital of Henan
    "15. Kaifeng, China": [34.7972, 114.3075],       # Henan, close to Zhengzhou
    "16. Anyang, China": [36.0976, 114.3924],
    "17. Pingyao, China": [37.1987, 112.1784],
    "18. Datong, China": [40.0768, 113.3001],
    "19. Mount Wutai, China": [39.0585, 113.5931],
    "20. Shijiazhuang, China": [38.0428, 114.5149],
    
    # Beijing to Shanghai Route
    "21. Beijing, China": [39.9042, 116.4074],
    "22. Qufu, China": [35.5964, 116.9919],
    "23. Mount Tai, China": [36.2506, 117.1018],
    "24. Qingdao, China": [36.0671, 120.3826],
    "25. Nanjing, China": [32.0603, 118.7969],
    "26. Shanghai, China": [31.2304, 121.4737],
    "27. Fuzhou, China": [26.0765, 119.2911],
    "28. Xiamen, China": [24.4798, 118.0894],
    
    # West China (Xinjiang)
    "29. Urumqi, China": [43.8256, 87.6168],
    "30. Turpan, China": [42.9513, 89.1897],
    "31. Kashgar, China": [39.4704, 75.9898],

    "32. Mount Kailash, Tibet": [31.0685, 81.3104],
    "33. Lake Manasarovar, Tibet": [30.6476, 81.4634],
    "34. Darchen, Tibet": [30.9650, 81.3189],
    "35. Pulan County (Burang), Tibet": [30.2972, 81.2464],
    "36. Hilsa, Nepal": [30.0381, 81.1750],

    "37. Lhasa, China (Tibet)": [29.6520, 91.1721],  # Tibet's capital
    "38. Shigatse, China (Tibet)": [29.2682, 88.8806],  # Major city near Everest
    # Add Indian cities after crossing
    # "39. Leh, India": [34.1526, 77.5771],  # A major town in northern India
    # "40. Srinagar, India": [34.0837, 74.7973],  # Capital of Jammu and Kashmir
    # "41. Delhi, India": [28.6139, 77.2090],  # India’s capital
    "39. Kathmandu, Nepal": [27.7172, 85.3240],  # Nepal's capital
    "40. Lumbini, Nepal": [27.4695, 83.2750],
    "41. Varanasi, India": [25.3176, 82.9739],
    "42. Agra, India": [27.1751, 78.0421],  # Taj Mahal location
    "43. Jaipur, India": [26.9124, 75.7873],
    "44. Delhi, India": [28.6139, 77.2090],  # India’s capital
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



def highlight_countries(countries):
    # Load the world shapefile from GeoPandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Check if each country is in the dataset and print any not found
    missing_countries = [country for country in countries if country not in world['name'].values]
    if missing_countries:
        print(f"Warning: The following countries were not found: {missing_countries}")

    # Plot the world map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.plot(ax=ax, color="lightgrey", edgecolor="black")

    # Highlight specified countries in red
    world[world['name'].isin(countries)].plot(ax=ax, color="red")

    # Add title and show the plot
    ax.set_title("Highlighted Countries", fontsize=15)
    plt.show()

# List of countries to highlight
countries_to_highlight = ["China", "India", "United States", "Brazil", "Australia"]

# Call the function to highlight countries
highlight_countries(countries_to_highlight)

