from setuptools import find_packages,setup
from typing import List


HYPHEN_E="-e ."
def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

        return requirements


setup(
    name="credit_card_fault",
    version="0.0.1",
    author="Pravin",
    author_email="pravinpoojari007@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()

)