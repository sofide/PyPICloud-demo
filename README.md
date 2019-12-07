# PyPICloud Demo

This is the PyPICloud demo I show in PyConAr 2019.

Here you can find the resulting files, after the demo.

## Run an internal PyPI sever
To repeat the demo, first you need to create and activate a virtual environment and 
install PyPICloud
```bash
pip install pypicloud[server]
```

The steps to repeat the demo are the following:
```bash
make start # to clean up the workspace
cd pypi-talk
pypicloud-make-config -t local.ini # choose "filesystem" storage
pserve local.ini
```

Now, you have a PyPI server running in http://localhost:6543

## Upload and install a package
First, you need to install "twine", to be able to upload the lib to the local new 
pypi server.

Then, build the packages and upload them to the PyPI server which should be running 
locally in port 6543.
```bash
pip install twine
cd my_lib
python setup.py sdist
twine upload --verbose dist/*  --repository-url http://localhost:6543
```
Now, you can install the lib with pip 
```
pip install -i http://localhost:6543/simple/ awesome-pycon-lib
```

## Extend PyPICloud with a custom view
Copy all files from custom_pypi inside pypi-talk folder and install the new copied 
library.
```
cd pypi-talk
cp -r ../custom_pypi/* .
pip install -e .
```
The, edit the local.ini file, changing the second line to use the new library:
```
use = egg:pycon-pypi
```
Now you can run your pypicloud again:
```
pserve local.ini --reload
```
And you can see the new endpoing in http://localhost:6543/ping
