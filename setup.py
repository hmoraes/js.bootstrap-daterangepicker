from setuptools import setup, find_packages
import os

version = '2.1.25'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'bootstrap_daterangepicker', 'test.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.bootstrap_daterangepicker',
    version=version,
    description="fanstatic twitter bootstrap daterangepicker.",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic twitter bootstrap daterangepicker',
    author='Heberte Fernandes de Moraes',
    url='https://github.com/hmoraes/js.bootstrap-daterangepicker',
    author_email='brebete@gmail.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'fanstatic[cssmin]',
        'fanstatic[jsmin]',
        'js.jquery>=1.9.0',
        'js.bootstrap',
        'js.momentjs',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap_daterangepicker = js.bootstrap_daterangepicker:library',
            ],
        },
    )
