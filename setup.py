import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mprstyle-mathematica", # Replace with your own username
    version="0.0.1",
    author="Phil Killewald",
    author_email="pkillewald@mathematica-mpr.com",
    description="Where to start for Mathematica-standard publication-quality plots in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/repo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)