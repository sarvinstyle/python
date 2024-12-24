import json
from pathlib import Path

# course = [
#     {"id" : 1 , "name" : "sarvin" , "sallary" : 100},
#     {"id" :  2 , "name" : "sarva" , "sallary" : 150},
#     {"id" : 4 , "name" : "a;i" , "sallary" : 100},
# ]

# data = json.dumps(course)
# Path("lesson13\\docs\\1.json").write_text(data)


data = Path("lesson13\\docs\\1.json").read_text()
courses= json.loads(data)
print(courses)
print(courses[1]["name"])

