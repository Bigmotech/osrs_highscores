import os
import setuptools

here = str(os.path.abspath(os.path.dirname(__file__)))

with open("README.md", "r") as fh:
    long_description = fh.read()

about = {}
with open(os.path.join(here, 'osrs_highscores', '__version__.py'), 'r') as f:
    exec(f.read(), about)


setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about['__url__'],
    license=about['__license__'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_reqires=[
        'requests==2.22.0',
    ]
)
