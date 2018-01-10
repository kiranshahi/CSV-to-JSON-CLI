from setuptools import setup

setup(
    name='CSV-to-JSON',
    version='0.1',
    license='GPL-3.0',
    description='A command line tool to convert csv file into json file.',
    author='Kiran Shahi',
    author_email='kiran.shahi.np@gmail.com',
    url='https://github.com/kiranshahi/CSV-to-JSON-CLI',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3'
        ],
    scripts=['csv2json']
)