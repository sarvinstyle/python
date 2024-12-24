from pathlib import Path
import os 

# p = Path("lesson13\\docs\\1.text")
# # read r - write w - append a - x create
# file = open("lesson13\\docs\\1.txt" , "r")
# # file.read(2)
# # print(file.read())
# # file.readline()
# # print(file.readline())
# for line in file:
#     print(line)


# file.close()

if not os.path.exists("lesson13\\docs\\3.txt") :
    file = open("lesson13\\docs\\3.txt" , "x")
    file.write("\namir")


my_path = Path("lesson13\\docs\\2.txt")
print(my_path.read_text())
my_path.write_text("some text")



target = Path("lesson13\\docs\\1.txt")
target.write_text(my_path.read_text())

import shutil
shutil.copy("lesson13\\docs\\1.txt" , "lesson13\\docs\\4.txt")

#os.remove(my_path)
del_file = Path("lesson13\\docs\\1.txt")
del_file.unlink()
