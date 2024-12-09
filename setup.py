from setuptools import setup, find_packages

setup(
    name='marketing-suite',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
        'python-dotenv>=0.19.0',
    ]
)