from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="UzMorphAnalyser",
    version="0.0.2",
    author="Ulugbek Salaev",
    author_email="ulugbek0302@gmail.com",
    description="Uzbek Morphological Analyser on Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UlugbekSalaev/UzMorphAnalyser",
    project_urls={
        "Bug Tracker": "https://github.com/UlugbekSalaev/UzMorphAnalyser/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "lxml"
    ],
    include_package_data=True,
)