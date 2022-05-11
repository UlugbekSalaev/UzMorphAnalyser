import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UzMorphAnalyser",
    version="0.0.4",
    author="Ulugbek Salaev",
    author_email="ulugbek0302@gmail.com",
    description="UzMorphAnalyser | Uzbek Morphological Analyser on Python",
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
    keywords=['python', 'mophology', 'uzbek-language'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={"": ["*.csv"]},
    #package_data={"": ["cyr_exwords.csv", "lat_exwords.csv"],},
)