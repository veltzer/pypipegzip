import setuptools

setuptools.setup(
    name='pypipegzip',
    version='0.0.11',
    description='faster read of gzip files using a pipe to zcat(1)',
    long_description='pypipegzip helps you read gzipped files faster by using a subprocess',
    url='https://veltzer.github.io/pypipegzip',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    keywords='pipe pipeline gzip read speed pypipegzip',
    packages=setuptools.find_packages(),
)
