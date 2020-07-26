import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="markdown-word-count",
    version="0.0.1",
    author="Georgios Andreadis",
    author_email="info@gandreadis.com",
    description="Word counter for raw Markdown files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gandreadis/markdown-word-count",
    packages=['mwc'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['mwc=mwc.cli:main'],
    }
)
