from typing import List


dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = []
make_requires: List[str] = [
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
