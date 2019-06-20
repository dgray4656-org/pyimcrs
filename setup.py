import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyimcrs",
    version="0.0.1a",
    author="David E. Gray",
    author_email="dgray4656@yahoo.com",
    description="Python package for interacting with HP iMC restful services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgray4656-org/pyimcrs",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests>=2.22.0',
      ],
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)