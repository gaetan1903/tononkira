import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tononkira",                  # This is the name of the package
    version='1.1.0',                      # The release version
    author="iTeam-$",                         # Full name of the author
    description="Unofficial Module and CLI tool to get Malagasy song lyrics from https://tononkira.serasera.org",
    long_description=long_description,  # Long description read from the readme
    long_description_content_type="text/markdown",
    packages=['tononkira'],  # List of all modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                      # Information to filter the project on PyPi website
    python_requires='>=3.6',
    py_modules=["tononkira"],                      # Name of the python package
    install_requires=[
        "beautifulSoup4", "requests"
    ],  # depandance
    include_package_data=True, # Include all data file with the package
    scripts=['bin/tononkira', 'bin/tononkira.bat']
)