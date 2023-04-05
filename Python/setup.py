import sys
from setuptools import setup

with open('LICENSE') as f:
    license = f.read()

with open('README') as f:
    readme = f.read()

dependency_version_specification = [
    'selenium==4.8.3',
    'setuptools==63.2.0'
]

setup(
    name='kaiju-quality-examples',
    version='0.0.1',
    packages=['utilities'],
    url='https://github.com/eschlange/kaiju-quality-examples',
    license=license,
    classifiers=['Programming Language :: Python :: 3.10'],
    author='Kaiju Quality Consulting LLC',
    author_email='eric.schlange@pizzahut.com',
    description='Kaiju Quality Consulting Example Library',
    include_package_data=True,
    long_description=readme,
    install_requires=dependency_version_specification,
)