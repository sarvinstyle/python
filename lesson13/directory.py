from pathlib import Path
import os

# p = Path("lesson13\\docs2")
# if not p.exists() :
#     p.mkdir()

# p.rmdir()

#os.mkdir("lesson13\\doc3")
#os.rmdir("lesson13\\doc3")

content = os.listdir("lesson13")
content = os.listdir( Path())
print(content)