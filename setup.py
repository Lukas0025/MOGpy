import setuptools
from shutil import copyfile

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MOGpy",
    version="0.0.1",
    author="Lukáš Plevač",
    author_email="lukas@plevac.eu",
    description="Python lib for molecular genetic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lukas0025/MOGpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=[
	    'matplotlib',
        'numpy'
    ],
)