import pathlib
import sys
import urllib.request
url = "https://framagit.org/robinechuca/cutcutcodec/-/raw/main/docs/demo/wiener_audio.py"
file = pathlib.Path.cwd() / "wiener_audio_demo.py"
if not file.exists():
    urllib.request.urlretrieve(url, file)
if sys.path[0] != str(file):
    sys.path.insert(0, str(file))
import wiener_audio_demo
wiener_audio_demo.main()
