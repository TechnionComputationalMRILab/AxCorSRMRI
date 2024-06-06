from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='axcorsrmri',
    version='1.0.0',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Technion Computational MRI Lab',
    author_email='tcml.bme@gmail.com',
    url='https://github.com/TechnionComputationalMRILab/AxCorSRMRI',
    install_requires=requirements,
)
