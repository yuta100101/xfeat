from typing import List

from setuptools import find_packages, setup


def get_install_requires() -> List[str]:

    return [
        "PyYAML",
        "optuna>=1.3.0",
        "lightgbm",
        "scikit-learn",
        "pandas",
        "pyarrow",
    ]


def get_tests_require() -> List[str]:

    return ["pytest"]


setup(
    name="xfeat",
    version="0.1.1",
    description="Feature Engineering & Exploration Library using GPUs and Optuna",
    author="Kohei Ozaki",
    author_email="ozaki@preferred.jp",
    packages=find_packages(),
    install_requires=get_install_requires(),
    extras_require={"develop": ["pytest"]},
    entry_points={"console_scripts": []},
)
