# python-translator
uses google cloud translator

# setup
1) dependencies: python3, pip, not sure what the minimum version is but I developed this on 3.11.5
2) run `pip install -r requirements.txt`
3) enable cloud translate api (you need to enable billing to get the option to use it) 
4) get a service account private key and download it
5) run `python3 translator.py` and drag and drop your config.json into it
6) fin

# compilation (for more or less performance/simplicity)
1) follow steps 1-4 in setup
2) install a C compiler, for linux: gcc and windows: visual studio build tools
3) run `python -m pip install nuitka` and use `python -m nuitka --version`
4) run `python -m nuitka translator.py` or if you want to move around the compiled version `python -m nuitka translator.py --standalone`
5) `./translator` or translator.exe, drag and drop your config.json
6) fin

# credits
@f-underscore for helping with development
