import folium
import geopandas as gpd
import pycountry

def create_auto_centered_map(locations, output_file="AutoCentered_Map_Route.html"):
    # Initialize map without specifying center and zoom
    auto_center_map = folium.Map()

    # Add all locations to the map
    for location, coordinates in locations.items():
        folium.Marker(location=coordinates, popup=location).add_to(auto_center_map)

    # Add edges from i to i+1
    locations_list = list(locations.values())
    for i in range(len(locations_list) - 1):
        folium.PolyLine(locations_list[i:i+2], color="blue", weight=2.5, opacity=1).add_to(auto_center_map)

    # Save map to HTML file
    auto_center_map.save(output_file)
    print(f"Map has been saved to {output_file}")

def highlight_countries_on_map(countries, shapefile_path, output_file="highlighted_countries_map.html"):
    # Load the world shapefile from the local file
    world = gpd.read_file(shapefile_path)

    # Convert country names to ISO Alpha-3 codes using pycountry
    country_codes = []
    for country in countries:
        try:
            country_code = pycountry.countries.lookup(country).alpha_3
            country_codes.append(country_code)
        except LookupError:
            print(f"Warning: '{country}' not found in pycountry database.")

    # Filter for the specified countries by ISO code
    highlighted = world[world["ADM0_A3"].isin(country_codes)]

    # Initialize a folium map centered globally
    world_map = folium.Map(location=[20, 0], zoom_start=2)

    # Add highlighted countries to the map in red
    folium.GeoJson(
        highlighted,
        style_function=lambda x: {'fillColor': 'red', 'color': 'black', 'weight': 0.5, 'fillOpacity': 0.7}
    ).add_to(world_map)

    # Save the map to an HTML file
    world_map.save(output_file)
    print(f"Map has been saved to {output_file}")

# # Define all locations with coordinates and labels
# all_locations = {
#     # South China
#     "1. Hong Kong": [22.3193, 114.1694],
#     "2. Shenzhen, China": [22.5431, 114.0579],
#     "3. Guangzhou, China": [23.1291, 113.2644],
#     # South-Central China
#     "4. Nanning, China": [22.8170, 108.3669],
#     "5. Guilin, China": [25.2744, 110.2900],
#     "6. Kunming, China": [24.8801, 102.8329],
#     # Yunnan Province Cluster
#     "7. Dali, China": [25.6939, 100.1619],
#     "8. Lijiang, China": [26.8721, 100.2257],
#     "9. Shangri-La, China": [27.8252, 99.7074],
#     # Central and Southwest China
#     "10. Chongqing, China": [29.5630, 106.5516],
#     "11. Chengdu, China": [30.5728, 104.0668],
#     # North-Central China
#     "12. Xi’an, China": [34.3416, 108.9398],
#     "13. Luoyang, China": [34.6587, 112.4249],       # Henan, near Xi'an
#     "14. Zhengzhou, China": [34.7466, 113.6254],     # Henan, capital of Henan
#     "15. Kaifeng, China": [34.7972, 114.3075],       # Henan, close to Zhengzhou
#     "16. Anyang, China": [36.0976, 114.3924],
#     "17. Pingyao, China": [37.1987, 112.1784],
#     "18. Datong, China": [40.0768, 113.3001],
#     "19. Mount Wutai, China": [39.0585, 113.5931],
#     "20. Shijiazhuang, China": [38.0428, 114.5149],
#     # Beijing to Shanghai Route
#     "21. Beijing, China": [39.9042, 116.4074],
#     "22. Qufu, China": [35.5964, 116.9919],
#     "23. Mount Tai, China": [36.2506, 117.1018],
#     "24. Qingdao, China": [36.0671, 120.3826],
#     "25. Nanjing, China": [32.0603, 118.7969],
#     "26. Shanghai, China": [31.2304, 121.4737],
#     "27. Fuzhou, China": [26.0765, 119.2911],
#     "28. Xiamen, China": [24.4798, 118.0894],
#     # West China (Xinjiang)
#     "29. Urumqi, China": [43.8256, 87.6168],
#     "30. Turpan, China": [42.9513, 89.1897],
#     "31. Kashgar, China": [39.4704, 75.9898],
#     "32. Mount Kailash, Tibet": [31.0685, 81.3104],
#     "33. Lake Manasarovar, Tibet": [30.6476, 81.4634],
#     "34. Darchen, Tibet": [30.9650, 81.3189],
#     "35. Pulan County (Burang), Tibet": [30.2972, 81.2464],
#     "36. Hilsa, Nepal": [30.0381, 81.1750],
#     "37. Lhasa, China (Tibet)": [29.6520, 91.1721],  # Tibet's capital
#     "38. Shigatse, China (Tibet)": [29.2682, 88.8806],  # Major city near Everest
#     "39. Kathmandu, Nepal": [27.7172, 85.3240],  # Nepal's capital
#     "40. Lumbini, Nepal": [27.4695, 83.2750],
#     "41. Varanasi, India": [25.3176, 82.9739],
#     "42. Agra, India": [27.1751, 78.0421],  # Taj Mahal location
#     "43. Jaipur, India": [26.9124, 75.7873],
#     "44. Delhi, India": [28.6139, 77.2090],  # India’s capital
# }

all_locations = {
    "Izmir/Alacati, Turkey": [38.2816, 26.3744],
    "Cappadocia, Turkey": [38.6431, 34.8278],
    "Safranbolu, Turkey": [41.2500, 32.6833],
    "Istanbul, Turkey": [41.0082, 28.9784]
}

if __name__ == "__main__":
    # Create auto-centered map with locations
    create_auto_centered_map(all_locations)

    # List of countries to highlight
    countries_to_highlight = ["China", "Mexico", "United States", "Canada", "Guatemala", "Honduras", "Spain", "United Kingdom"]

    # Call the function to highlight countries and save to HTML
    highlight_countries_on_map(countries_to_highlight, shapefile_path="/Users/songye03/Desktop/me/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")