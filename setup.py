import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHOR_USER_NAME = "introvert730180"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL = "ch21btech11001@iith.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'ensure==1.0.2',
        'py-youtube==1.1.7',
    ],
    extras_require={
        "dev": [
            "pytest>=7.1.3",
            "mypy>=0.971",
            "flake8>=5.0.4",
            "tox>=3.25.1",
            "black>=22.8.0",
        ]
    },
)
