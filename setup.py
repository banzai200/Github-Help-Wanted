from setuptools import setup

setup(
    name='github-help-wanted',
    version='1.0',
    packages=['github-help-wanted'],
    url='https://github.com/banzai200/Github-Help-Wanted',
    license='MIT License',
    author='Wesley',
    author_email='tairoria@gmail.com',
    description='A python program for fetching github issues with the "help-wanted" tag',
    install_requires=['PyGithub'],
    entry_points={
        'console_scripts': [
            'gh = gh.gh:exe'
        ]
    },
)