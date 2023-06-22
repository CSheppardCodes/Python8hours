#json2md
from mdutils.mdutils import MdUtils
import json
#read file
myjsonfile = open('5.json', 'r')
jsondata = myjsonfile.read()

#parse
obj = json.loads(jsondata)

#display json contents
print(str(obj['id']))
numfloors = obj['floor_priority']
print(str(obj['two_bays']))
bayslist = obj['two_bays']
print(len(bayslist))

#for i in range(len(bayslist)):

print(str(obj['max_reservations_in_section']))

Location = obj['name'].capitalize() + ' (' + obj['id'] + ')'
Floor_Priority = '\tFloor Priority: ' + str(numfloors[0]) + ',' + str(
  numfloors[1])  #make forloop
Max_Reserve = '\tMax Reservations in Section: ' + str(
  obj['max_reservations_in_section'])
#for i in range(len(bayslist)):##sort first if mdutil does not do list sort

mdFile = MdUtils(file_name='Example_markdon', title='markdown file example')
mdFile.new_header(level=1, title=Location)
mdFile.new_line(Floor_Priority)
mdFile.new_line(Max_Reserve)

mdFile.create_md_file()

# #md
# markdown_string = '# Hello World'
# html_string = markdown.markdown(markdown_string)
# print(html_string)
print("we reached this point")
