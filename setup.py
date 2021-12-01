from setuptools import setup, find_packages

setup(
    name="pygazebo",
    version="4.0.0",
    description="Python bindings for the Gazebo multi-robot simulator.",
    long_description=open("README.rst").read(),
    author="Markus Sommer",
    author_email="msommer@informatik.uni-marburg.de",
    url="https://github.com/CryptoCopter/pygazebo",
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=["protobuf"],
    license="Apache License 2.0",
    zip_safe=True,
    keywords="gazebo",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
    ],
    tests_require=["pytest", "mock"],
    extras_require={
        "testing": ["pytest", "mock"],
    },
    project_urls={
        "Bug Reports": "https://github.com/CryptoCopter/pygazebo/issues",
        "Source": "https://github.com/CryptoCopter/pygazebo",
    },
)
