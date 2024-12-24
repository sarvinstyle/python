# path folder files

from pathlib import Path

Path("C:\\Users\\Sarvin")
#Path("/user/local/bin")

Path()
p= Path("lesson13\\path.py")
m= p.exists()
m= p.is_dir()
m= p.is_file()
m= p.name
m = p.stem
m = p.suffix
m = p.absolute()
m = p.with_name("changed.py")
m = p.with_suffix(".txt")
print(m)