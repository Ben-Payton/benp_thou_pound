import setuptools

import pathlib

PROJECT_NAME = "your_project_name"
VERSION = "0.0.0"
SHORT_DESCRIPTION = "useful python tools that I use to streamline my work."
SOURCE_CODE_LINK= "https://github.com/Ben-Payton/repo_name"
DOCUMENTATION_LINK = "https://github.com/Ben-Payton/ben_sci_tools/blob/main/README.md" 
REQUIRED_DEPENDANCIES = []


setuptools.setup(
    name = PROJECT_NAME,
    version = VERSION,
    description= SHORT_DESCRIPTION,
    long_description= pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author = "Ben Payton",
    project_urls = {
        "Documentation" : DOCUMENTATION_LINK,
        "Source" : SOURCE_CODE_LINK
    },
    install_requires = REQUIRED_DEPENDANCIES,
    packages=setuptools.find_packages()
    )