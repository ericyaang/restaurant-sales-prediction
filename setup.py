from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define our package
setup(
    name="restaurant-sales-prediction",
    version=0.1,
    description="",
    author="Eric Yang",
    author_email="ericyaang@gmail.com",
    url="",
    python_requires=">=3.8",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)
