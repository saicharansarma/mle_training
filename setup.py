from setuptools import setup, find_packages  # or find_namespace_packages

setup(
    # ...
    packages=find_packages(
        where='src',
        include=['mypackage*'],
        exclude=['mypackage.tests'],
    ),
    # ...
)