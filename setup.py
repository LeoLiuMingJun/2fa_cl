import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='twofa_cl',
     version='0.0.1',
     scripts=['2fa'] ,
     author="Leo Liu",
     author_email="leoliumingjun@gmail.com",
     description="Two-factor authentication on the command line by python.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/LeoLiuMingJun/2fa_cl",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )