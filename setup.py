from setuptools import setup, find_packages

VERSION = "0.0.1"

tests_require = ["unittest", "sphinx"]

requires = ["numpy", "matplotlib", "scipy"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SecondOrderElec",
    version=VERSION,
    url="https://github.com/slashformotion/SecondOrderElec",
    license="MIT",
    author="slashformotion",
    author_email="slashformotion@protonmail.com",
    description="A set of tools to work with continuous-time system. You will find various second order electronic filters models.",
    packages=["SecondOrderElec"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    tests_require=tests_require,
    install_requires=requires,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
