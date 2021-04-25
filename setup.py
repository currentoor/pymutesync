from setuptools import find_packages, setup

long_description = open("README.md").read()

setup(
    name="mutesync",
    version="0.0.1",
    license="Apache License 2.0",
    url="https://github.com/currentoor/pymutesync",
    author="Karanbir Toor",
    author_email="support@mutesync.com",
    description="Asynchronous library to control mutesync devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["mutesync"],
    zip_safe=True,
    platforms="any",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

