from setuptools import setup, find_packages


setup(
    author="PADMEC",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    description="PyMOAB geometric utilities.",
    name="pymoab-geoutils",
    version='0.1',
    url='https://github.com/padmec-reservoir/pymoab-geoutils',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-mock', 'pytest-faker'],
    install_requires=['cypyler'],
    packages=find_packages(),
    license="MIT license",
    zip_safe=False,
    include_package_data=True
)
