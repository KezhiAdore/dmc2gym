from setuptools import setup
from setuptools import find_packages

setup(
    name='dmc2gym',
    version='1.1.0',
    author='Zhao Yu',
    description=('a gym like wrapper for dm_control'),
    license='',
    keywords='gym dm_control openai deepmind',
    packages=find_packages(),
    install_requires=[
        'gymnasium==1.1.1',
        'dm_control==1.0.28',
    ],
)
