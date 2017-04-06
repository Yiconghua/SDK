

from setuptools import setup, find_packages

setup(
    name='eleme.openapi.sdk',
    version='0.0.1.13',
    keywords=('eleme', 'openapi'),
    #long_description=open('README.md').read(),
    description='eleme openapi python sdk',
    license='MIT License',
    package_data = {
        '': ['*.html'],
    },
    packages=find_packages(),
    #install_requires=['web>=0.38'],
    author='David',
    author_email='pengfei.zhu@ele.me',
)

