import setuptools


def get_readme():
    with open("README.rst") as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pypipegzip",
    version="0.0.24",
    packages=[
        "pypipegzip",
    ],
    # from here all is optional
    description="faster read of gzip files using a pipe to zcat(1)",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        "pipe",
        "pipeline",
        "gzip",
        "read",
        "speed",
        "pypipegzip",
    ],
    url="https://veltzer.github.io/pypipegzip",
    download_url="https://github.com/veltzer/pypipegzip",
    license="MIT",
    platforms=[
        "python3",
    ],
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
)
