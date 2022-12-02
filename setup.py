from setuptools import setup

setup(
    name="pklmpl",
    version="1.0.0",
    description="Small utility to pickle matplotlib figures and load them later",
    url="https://github.com/rocheseb/pklmpl",
    author="Sebastien Roche",
    author_email="sroche@g.harvard.edu",
    license="MIT",
    packages=["pklmpl"],
    package_dir={"pklmpl":"pklmpl"},
    entry_points={
        'console_scripts':[
            'pklmpl=pklmpl.pklmpl:main',
        ],
    },
    zip_safe=False,
    install_requires=[
        "matplotlib",
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
