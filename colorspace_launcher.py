import pathlib
import sys
import urllib.request
url = "https://framagit.org/robinechuca/cutcutcodec/-/raw/main/docs/demo/colorspace.py"
file = pathlib.Path.cwd() / "colorspace_demo.py"
if not file.exists():
    urllib.request.urlretrieve(url, file)
if sys.path[0] != str(file):
    sys.path.insert(0, str(file))
import colorspace_demo
colorspace_demo.main()
