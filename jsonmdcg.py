import json


def generate_markdown(json_data):
  output = ""

  # Extract values from the JSON data
  id = json_data["id"]
  floor_priority = json_data["floor_priority"]
  name = json_data["name"]
  bays = json_data["two_bays"]
  max_res = json_data["max_reservations_in_section"]

  # Generate the output string
  output += f" # {name.capitalize()} ({id})\n"
  output += f"Floor Priority: {','.join(str(x) for x in floor_priority)}\n\n"
  output += f"Max Reservations in Section: {max_res}\n\n"#error with \n\n vs \n not working in github preview
  output += f"Two Bays:\n" 

  # Generate the lis values with bullet points
  for num in sorted(bays, reverse=True):
    output += f"- {num}-{num + 1}\n"

  return output


# Read the input JSON file
with open("5.json", "r") as file:
  json_data = json.load(file)

# Generate the markdown file
markdown_output = generate_markdown(json_data)

# Write the output to a file
with open("output.md", "w") as file:
  file.write(markdown_output)
