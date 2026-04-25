from setuptools import setup, find_packages

setup(
    name="secret_to_file",
    version="1.5",
    packages=find_packages(),
    install_requires=[],
    author="slave725",
    description="A beginner's file secret encoder/decoder in Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)