import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "cnnproj1"
AUTHOR_USER_NAME = "aqeeljabir"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "abdullaaqeeljabir@gmail.com"

setuptools.setup(
     name = SRC_REPO,
     version=__version__,
     author=AUTHOR_USER_NAME,
     author_email=AUTHOR_EMAIL,
     description="for cnn",
     long_description=long_description,
     long_description_content="text/markdown",
     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
     project_urls={
         "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
     }, 
 )