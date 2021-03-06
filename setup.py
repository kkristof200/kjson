import setuptools, os

if os.path.exists(os.path.join(os.getcwd(), "README.md")):
    with open("README.md", "r") as f:
        long_description = f.read()
else:
    long_description = 'kjson'

setuptools.setup(
    name="kjson",
    version="0.0.2",
    author="Kristof",
    description="some json util methods/shorthands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/kjson",
    packages=setuptools.find_packages(),
    install_requires=[""],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)