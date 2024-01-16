from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'


def get_requirements(file_path: str)-> List[str]:
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Bittu Hussain',
    author_email='nb705033848@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()



)
