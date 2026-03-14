import setuptools
from typing import List
HYPEN_E_DOT='-E.'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path, 'r') as file_obj:
        for line in file_obj:
            line = line.strip()
            if line.startswith("-e"):
                continue
            if line and not line.startswith('#'):
                requirements.append(line)
    return requirements

setuptools.setup(
    name='mlproject',
    version='0.0.1',
    author='haricharan',
    author_email='musipatlaharicharan2005@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=get_requirements('requirements.txt')
)