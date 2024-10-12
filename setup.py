from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT_E = '-e .'

def getRequirements(path:str) -> List[str]:
    req = []
    with open(path) as f:
        req = f.read().splitlines()

    if HYPHEN_DOT_E in req:
        req.remove(HYPHEN_DOT_E)

    return req


setup(
    name='generic-ml-struct',
    version='0.0.1',
    author='Yashaswee Kesharwani',
    author_email='career.yashaswee@gmail.com',
    packages=find_packages(),
    install_requires = getRequirements('requirements.txt')
)