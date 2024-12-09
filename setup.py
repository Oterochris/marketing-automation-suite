from setuptools import setup, find_packages

setup(
    name='marketing-automation-suite',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
        'requests>=2.26.0',
        'python-dotenv>=0.19.0',
    ],
)