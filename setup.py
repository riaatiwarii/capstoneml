from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
  """
  This function will return the list of requirements
  """
  requirements = []
  with open(file_path, "r") as file:
    requirements = file.readlines()
    requirements = [req.replace("\n","")for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
    
  return requirements

setup(
  name="end_to_end",
  version="0.1.0",
  author="Riya",
  author_email="riyatrpthi@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements("requirements.txt"),

)
