from setuptools import find_packages,setup
from typing import List

EDOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function we will return the list of requirements.!!!!!!
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n"," ") for req in requirements]
        if EDOT in requirements:
            requirements.remove(EDOT)
    return requirements



setup(
    name='MLProject',
    version='0.0.1',
    author='venkata',
    author_email='surya.bandi92@gmail.com',
    install_requires = ['panda','numpy','seaborn'],
    packages=find_packages(),
    install_requirements = get_requirements('requirements.txt')
    
    )
