import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__= "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHUOR_USER_NAME="introvert730180"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL = "ch21btech11001@iith.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHUOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="A small python packages",
    Long_description = long_description,
    Long_description_content= "text/markdown",
    url=f"https://github.com/{AUTHUOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHUOR_USER_NAME}/{REPO_NAME}/issues",

    },
    packages_dir={"":"src"},
    packages = setuptools.find_packages(where = "src")

)
