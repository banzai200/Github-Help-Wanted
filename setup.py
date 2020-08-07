from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='github-help-wanted',
    version='1.1',
    packages=['githubhelp'],
    url='https://github.com/banzai200/Github-Help-Wanted',
    license='MIT License',
    author='Wesley',
    author_email='tairoria@gmail.com',
    description='A python program for fetching github issues with the "help-wanted" tag',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['PyGithub'],
    entry_points={
        'console_scripts': [
            'gh = githubhelp.gh:main'
        ]
    },
)
