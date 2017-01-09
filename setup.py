import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pypipegzip',
    version='0.0.2',
    description='faster read of gzip files using a pipe to zcat(1)',
    long_description='pypipegzip helps you read gzipped files faster by using a subprocess',
    url='https://veltzer.github.io/pypipegzip',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='pipe pipeline gzip read speed pypipegzip',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
)
