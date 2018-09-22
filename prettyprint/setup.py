from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='prettyprint',
    version='0.1.1',
    author='Christopher Agard',
    author_email='cragard@gmail.com',
    description="Python library for facilitating automated print job",
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
