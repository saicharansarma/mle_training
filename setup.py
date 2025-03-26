from setuptools import find_packages, setup

setup(
    name="housingPricePrediction",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "six",
        "flake8",
    ],
)
