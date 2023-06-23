import json
#read file
myjsonfile = open('5.json', 'r')
jsondata = myjsonfile.read()

#parse
jsondata = json.loads(jsondata)


def generate_markdown(json_data):
  output = ""

  # Extract values from the JSON data
  i = json_data["id"]
  fp = json_data["floor_priority"]
  n = json_data["name"]
  lis = json_data["two_bays"]
  mris = json_data["max_reservations_in_section"]

  # Generate the output string
  output += f" # {n.capitalize()} ({i})\n"
  output += f"    FP: {', '.join(str(x) for x in fp)}\n"
  output += f"MRIS: {mris}\n"
  output += "\tlis:\n"

  # Generate the lis values with bullet points
  for num in sorted(lis, reverse=True):
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
