from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    """
    Read the requirements from a file and return them as a list.
    
    :param file_path: Path to the requirements file.
    :return: List of requirements.
    """
    with open(file_path) as f:
        return f.read().splitlines()

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    author='Ahmed Hammad',
    author_email='ma6922ma@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)