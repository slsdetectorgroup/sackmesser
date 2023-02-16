import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="sackmesser",
    version= '2023.2.17',
    author="Erik Frojdh",
    author_email="erik.frojdh@psi.ch",
    description="Python utils to work with detectors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slsdetectorgroup/sackmesser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
