#json2md
from mdutils.mdutils import MdUtils
import json
#read file
myjsonfile = open('5.json', 'r')
jsondata = myjsonfile.read()

#parse
obj = json.loads(jsondata)

#display json contents
bayslist = obj['two_bays']
print(bayslist.sort(reverse = True))
print(bayslist)
print(type(bayslist))
print(bayslist)
#add second list befor turning to string
bayslistSTR = (str(x) for x in bayslist)
print (bayslistSTR)


Location = obj['name'].capitalize() + ' (' + obj['id'] + ')'
numfloors = obj['floor_priority']
Floor_Priority = ','.join(map(str, numfloors))
Floor_Priority = '\tFloor Priority: ' + Floor_Priority
Max_Reserve = '\tMax Reservations in Section: ' + str(obj['max_reservations_in_section'])
Two_Bays = "\tTwo_Bays:"


mdFile = MdUtils(file_name='Example_markdon', title='markdown file example')
mdFile.new_header(level=1, title=Location)
mdFile.new_line(str(Floor_Priority))
mdFile.new_line(Max_Reserve)
mdFile.new_line(Two_Bays)
#mdFile.new_line(str(bayslist))
mdFile.new_list(bayslistSTR)
mdFile.create_md_file()

# #md
# markdown_string = '# Hello World'
# html_string = markdown.markdown(markdown_string)
# print(html_string)
print("we reached this point")
