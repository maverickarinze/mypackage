from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Sample Python Package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https//:github.com/maverickarinze/mypackage',
    author='Stanley Agbo',
    author_email='arinzestanley65@gmail.com'
)