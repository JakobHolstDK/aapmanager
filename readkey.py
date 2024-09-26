import json

# Load the SSH key from a file
with open('data/aapdemo', 'r') as key_file:
    ssh_key_data = key_file.read()

# Create the JSON structure
json_data = {
    "username": "team-nine",
    "password": "ixj90j2s",
    "ssh_key_data": ssh_key_data
}

# Convert to JSON string
json_string = json.dumps(json_data)
print(json_string)  # This will output your JSON string for use in the CLI
