import setuptools

with open("README.md", "r") as fh:
    long_description = str(fh.read()).strip()

with open("VERSION", "r") as fh:
    version = str(fh.read()).strip()

setuptools.setup(
    name="console-card-game-of-war",
    version=version,
    author="Alex Goretoy",
    author_email="alex@goretoy.com",
    description="CONSOLE CARD GAME OF WAR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlatEarthTruther/console-card-game-of-war",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)