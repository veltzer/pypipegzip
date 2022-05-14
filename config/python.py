import config.project

package_name = config.project.project_name

dev_requires = [
    "pypitools",
]
config_requires = [
    "pyclassifiers",
]
make_requires = [
    "pymakehelper",
]
test_requires = [
    "pylint",
    "flake8",
    "pytest",
    "pytest-cov",
    "pyflakes",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
