import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="email_tools",
    version="0.0.1",
    author="Colin Evans",
    author_email="cevans@sdge.com",
    description="Tools for extracting and manipulating emails in the MSG and TXT format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cevans-sdge/email_tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
