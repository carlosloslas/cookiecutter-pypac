from setuptools import setup

setup(
    name="{{cookiecutter.package_name}",
    description="{{cookiecutter.description}}",
    author="{{cookiecutter.author}}",
    version="{{cookiecutter.version}}",
    packages=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
