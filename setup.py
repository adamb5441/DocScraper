
from setuptools import setup, find_packages
from webrec.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='webrec',
    version=VERSION,
    description='Webpage to PDF',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Adam Brown',
    author_email='adamb5441@gmail.com',
    url='https://github.com/adamb5441/Web-Record',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'webrec': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        webrec = webrec.main:main
    """,
)
