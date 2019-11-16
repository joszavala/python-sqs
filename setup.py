from setuptools import setup, find_packages

setup(
    name='python-sqs',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest'
    ],
)
