import json
import glob


def generate_markdown(json_data):
  output = ""

  # Extract values from the JSON data
  i = json_data["i"]
  f = json_data["f"]
  n = json_data["n"]
  t = json_data["t"]
  m = json_data["m"]

  # Generate the output string
  output += f" # {n.title()} ({i})\n"
  output += f"**Floor Priority:** {','.join(str(x) for x in f)}\n\n"
  output += f"**Max Reservations in Section:** {m}\n\n"
  #error with \n\n vs \n not working in github preview
  output += "**Two Bays:**\n"

  # Group the bays values by the first digit
  grouped_bays = {}
  for num in t:
    first_digit = str(num)[0]
    if first_digit in grouped_bays:
      grouped_bays[first_digit].append(num)
    else:
      grouped_bays[first_digit] = [num]

  # Generate the bays values with the desired format
  for _, nums in sorted(grouped_bays.items(), reverse=True):
    output += "- "
    output += ", ".join(f"{n}-{n+1}" for n in sorted(nums))
    output += "\n"

  return output


# Get a list of JSON file paths
file_paths = glob.glob("*.json")

# Read the JSON data and sort the file paths based on "n": "d" value
sorted_file_paths = sorted(file_paths,
                           key=lambda path: json.load(open(path))["n"])

# Process each JSON file
markdown_output = ""
for file_path in sorted_file_paths:  ###file_paths
  # Read the JSON data from the file
  with open(file_path, "r") as file:
    json_data = json.load(file)

  # Check if the value of "name" is a string
  if isinstance(json_data["n"], str):
    # Generate the markdown output for the valid JSON data
    markdown_output += generate_markdown(json_data)

# Write the output to a file
with open("output.md", "w") as file:
  file.write(markdown_output)
