import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='cli-changelog',  
     version='1.3.0',
     scripts=['changelog'] ,
     author="Mathieu MARACHE",
     author_email="mathieu@marache.com",
     description="A changelog update cli tool",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mathieu/changelog-cli",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )