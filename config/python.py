from typing import List


config_requires: List[str] = [
    "pyclassifiers",
]
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = []
make_requires: List[str] = [
    "pyclassifiers",
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "flake8",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
