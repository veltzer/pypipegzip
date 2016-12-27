import setuptools

setuptools.setup(
    name='pipegzip',
    version='0.0.2',
    description='faster read of gzip files using a pipe to zcat(1)',
    long_description='pipegzip helps you read gzipped files faster by using a subprocess',
    url='https://veltzer.github.io/pipegzip',
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
    keywords='pipe pipeline gzip read speed',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
)
