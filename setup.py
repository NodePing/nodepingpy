import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "nodepingpy"
DESCRIPTION = "Python package for querying the NodePing API"
URL = "https://github.com/NodePing/nodepingpy"
EMAIL = "support@nodeping.com"
AUTHOR = "NodePing"
VERSION = "1.0.1"
LICENSE = "MIT"

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
