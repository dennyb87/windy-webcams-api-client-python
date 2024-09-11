from distutils.core import setup

from setuptools import find_packages

setup(
    name="windy-webcams-api-client-python",
    version="0.1.0",
    description="Simple python client for windy webcams api",
    author="Denny Baldini",
    author_email="dennybaldini@gmail.com",
    url="https://github.com/dennyb87/windy-webcams-api-client-python",
    install_requires=[
        "requests==2.31.0",
    ],
    packages=find_packages(),
    package_dir={"": "src"},
)
