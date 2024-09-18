import requests
import os
import json

# Load the country codes from the JSON file
with open('', 'r') as f:
    country_data = json.load(f)

# Create a folder to store downloaded images
if not os.path.exists('flags'):
    os.makedirs('flags')

# Loop through all country entries in the JSON and download the corresponding flag image
for country in country_data:
    country_name = country['Name']
    country_code = country['Code'].lower()  # Convert to lowercase to match the URL format
    url = f'https://flagsapi.com/{country_code}/flat/64.png'
    
    # Save the image using the country name in the filename
    img_name = os.path.join('flags', f'{country_name}.png')
    
    # Download and save the image
    with open(img_name, 'wb') as f:
        f.write(requests.get(url).content)
    
    print(f"Downloaded: {img_name}")

print("All flag images downloaded!")
