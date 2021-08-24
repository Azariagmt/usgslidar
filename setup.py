from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='usgslidar',
    version='0.0.25',
    description='A basic package to fetch USGs\'s LIDAR agriculture data',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='Azaria Gebremichael',
    author_email='azariagebremichael10@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['usgs', 'lidar'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['fiona', 'gdal', 'pdal',
                      'geopandas', 'pyproj', 'laspy', 'matplotlib']
)
