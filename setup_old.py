from setuptools import find_packages, setup
from typing import List
import os

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file.
    """
    HYPEN_E_DOT = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Read long description from README.md if available
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="smartdocAI",
    version="0.0.1",
    author="Akash Soni",
    author_email="toakashsoni@gmail.com",
    description="Document Analysis, Chat & Comparison Portal with Advanced RAG",
    long_description=long_description or "Document Analysis, Chat & Comparison Portal with Advanced RAG",
    long_description_content_type="text/markdown",
    url="https://github.com/akash-soni/SmartDocAI",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.10",
    install_requires=get_requirements("requirements.txt"),
)
