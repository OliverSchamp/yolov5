from pathlib import Path

import setuptools

current_folder: Path = Path(__file__).parent
name: str = current_folder.name
version: str = "0.0.0"

with open(f"{current_folder}/requirements.txt", "r", encoding="utf-8") as file:
    requirements = file.readlines()

with open(f"{current_folder}/README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


setuptools.setup(
    name=name,
    version=version,
    author="OiverSchamp",
    author_email="oliverpj.schamp@gmail.com",
    description="YOLOv5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: GPU :: NVIDIA CUDA :: 11.4",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="object detection",
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={},
)
