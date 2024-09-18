import os
import json

# Load the country codes from the JSON file
with open('countrycodes.json', 'r') as f:
    country_data = json.load(f)

# Folder where the images are stored
flags_folder = 'flags'

# Loop through all country entries in the JSON
for country in country_data:
    country_name = country['Name']
    country_code = country['Code'].upper()  # Convert to uppercase for country codes

    # Build the old filename (current name is the country name)
    old_filename = os.path.join(flags_folder, f'{country_name}.png')

    # Build the new filename (to rename to the country code)
    new_filename = os.path.join(flags_folder, f'{country_code}.png')

    # Check if the file exists, then rename it
    if os.path.exists(old_filename):
        os.rename(old_filename, new_filename)
        print(f'Renamed: {old_filename} -> {new_filename}')
    else:
        print(f'File not found: {old_filename}')

print("All images have been renamed!")
