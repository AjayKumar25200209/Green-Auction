import json

# Existing JSON data
existing_json_str = '{"bidding": {"bidnum": 9, "ano": "1017", "bammount": "11"}, "bidnum": 5, "ano": "1017", "bammount": "5456"}'

# Parse the existing JSON string into a Python dictionary
existing_data = json.loads(existing_json_str)

# New data to update the dictionary
new_data = {"bidnum": 10, "ano": "1017", "bammount": "12345"}

# Update the dictionary with the new data
existing_data.update(new_data)

# Convert the updated dictionary back to a JSON string
updated_json_str = json.dumps(existing_data)

# Print the updated JSON string
print(updated_json_str)
