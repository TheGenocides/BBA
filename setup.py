from setuptools import setup
import re

version = ""
with open("bba/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.md") as f:
    readme = f.read()

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Operating System :: OS Independent",
    "Topic :: Internet",
    "Topic :: Utilities",
    "Development Status :: 5 - Production/Stable",
]


setup(
    name="BBA",
    author="TheGenocide",
    maintainer="TheGenocide",
    url="https://github.com/TheGenocides/BBA/",
    version=version,
    packages=["bba"],
    include_package_data=True,
    license="MIT",
    project_urls={
        "HomePage/Github": "https://github.com/TheGenocides/BBA/",
    },
    description="A Synchronous python API wrapper for twitter's api",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    keywords="BBA, bba, breadbot, breadbotapi, api",
    python_requires=">=3.7.0",
    classifiers=classifiers
)