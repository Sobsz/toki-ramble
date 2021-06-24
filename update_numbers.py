import os
import re

files = tuple(os.scandir("./toki"))
size = format(sum([i.stat().st_size for i in files]) / 1000, ".1f")
count = str(len(files))

with open("README.md", "r") as f:
    readme = f.read()

readme = re.sub("(?<=<!--sizestart-->).*?(?=<!--sizeend-->)", size, readme)
readme = re.sub("(?<=<!--countstart-->).*?(?=<!--countend-->)", count, readme)

with open("README.md", "w") as f:
    f.write(readme)
