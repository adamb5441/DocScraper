
from setuptools import setup, find_packages
from web record.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='web record',
    version=VERSION,
    description='Store web documentation for future use.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Adam Brown',
    author_email='adamb5441@gmail.com',
    url='https://github.com/adamb5441/Web-Record',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'web record': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        web record = web record.main:main
    """,
)
