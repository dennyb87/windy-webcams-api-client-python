from distutils.core import setup

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
    packages=["windy_webcams_api", "windy_webcams_api/v3"],
    package_dir={"": "src"},
)
