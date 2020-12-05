from setuptools import setup, find_packages

VERSION = "0.0.4"

tests_require = ["unittest", "sphinx"]

requires = ["numpy", "matplotlib", "scipy"]


def write_version_py(filename):
    """Write version."""
    cnt = f'"""THIS FILE IS GENERATED FROM SecondOrderElec SETUP.PY."""\nversion = \'{VERSION}\''
    with open(filename, "w") as a:
        a.write(cnt)


if __name__ == "__main__":

    write_version_py("SecondOrderElec/version.py")

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setup(
        name="SecondOrderElec",
        version=VERSION,
        url="https://github.com/slashformotion/SecondOrderElec",
        license="MIT",
        author="slashformotion",
        author_email="slashformotion@protonmail.com",
        description="A python module to work with continuous-time system. You will find various second order electronic filters models.",
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
