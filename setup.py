from setuptools import find_packages, setup

setup(
    name='bittrexTools',
    packages=find_packages(include=['bittrexTools']),
    version='0.1.0',
    description='A set of API functions to be used with Bittrex API v3',
    author='Xattle',
    license='',
    install_requires=[],
    setup_requires=[''],
    tests_require=[''],
    test_suite='tests',
)

#https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f