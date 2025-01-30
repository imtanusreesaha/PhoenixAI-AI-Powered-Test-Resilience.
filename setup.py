
from setuptools import setup, find_packages

setup(
    name="self_healing_tests",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "selenium==4.1.0",
        "pytest==7.1.2",
        "pytest-allure-adaptor==2.10.0",
        "pyyaml==6.0",
        "docker==5.0.3"
    ],
    test_suite='pytest',
)
