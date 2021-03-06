import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trifacta",
    version="2.2",
    author="Vijay Balasubramaniam",
    author_email="vbalasu@gmail.com",
    description="Trifacta client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vbalasu/trifacta",
    packages=setuptools.find_packages(),
    install_requires=['requests','pywebhdfs','pandas', 'boto3', 'ipywidgets', 'ijson', 'simplejson'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
