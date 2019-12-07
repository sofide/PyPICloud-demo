from setuptools import setup, find_packages


setup(
    name="pycon-pypi",
    version="0.1",
    packages=find_packages(),
    entry_points={"paste.app_factory": ["main = pypi_pycon:main"]},
)
