# Step 1: Import the necessary libraries
import pandas as pd
import folium

# Step 2: Load the CSV file
file_path = r'C:\Users\HP\Desktop\RIM Analysis\Year-to-date.csv'  # Update the file path
data = pd.read_csv(file_path)

# Step 3: Function to check if coordinates are valid
def is_valid_coordinates(lat, lon):
    return -90 <= lat <= 90 and -180 <= lon <= 180

# Step 4: Initialize the map
map_refugees = folium.Map(location=[20, 0], zoom_start=2)  # Centered on Africa

# Step 5: Iterate through the data and create markers with text for valid coordinates
for index, row in data.iterrows():
    country = row['Country']
    lat = row['Latitude']
    lon = row['Longitude']
    admitted = row['Total Admitted']
    
    # Check if the latitude and longitude are valid
    if is_valid_coordinates(lat, lon):
        # Add a marker with the number of admitted refugees as text
        folium.Marker(
            location=[lat, lon],
            icon=folium.DivIcon(html=f"""<div style="font-size: 12px; color: black;">{admitted}</div>""")
        ).add_to(map_refugees)
    else:
        # Log invalid data
        print(f"Skipping invalid data for {country}: Latitude={lat}, Longitude={lon}, Total Refugees Admitted={admitted}")

# Step 6: Save the map to an HTML file
output_path = r'C:\Users\HP\Desktop\RIM Analysis\interactive_map.html'  # Update the file path
map_refugees.save(output_path)

print(f"Map saved to {output_path}")
