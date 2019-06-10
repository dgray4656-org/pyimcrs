import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyimcrs",
    version="0.0.1",
    author="David E. Gray",
    author_email="dgray4656@yahoo.com",
    description="Python package for interacting with HR iMC restful services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgray4656-org/pyimcrs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)