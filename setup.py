from setuptools import find_packages, setup
from typing import List

# This is used to ignore "-e ." in requirements.txt
HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements from a requirements.txt file
    and return them as a list.
    """
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.1.0",
    author="Muhammad Talha Hussain",
    author_email="mtalhahussain23@gmail.com",
    description="End-to-end Machine Learning Project",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.10",
    license="MIT",
)