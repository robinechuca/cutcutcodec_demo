import urllib.request
url = "https://framagit.org/robinechuca/cutcutcodec/-/raw/main/docs/demo/colorspace.py"
urllib.request.urlretrieve(url, "colorspace_demo.py")
import colorspace_demo
