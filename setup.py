from setuptools import setup

version = '0.1'

setup(  name='dodo',
        version=version,
        description='DigitalOcean Library and Command Line tools',
        author='Adam Wisniewski',
        author_email='adamw@tbcn.ca',
        licence='MIT',
        packages=['dodo'],
        scripts=['bin/dodo']
    )

