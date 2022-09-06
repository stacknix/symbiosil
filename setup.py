from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'Symbiosil is open source AI bot framework. Our goal is to make living like symbiosis which can run on any platform and device.'

setup(
    name='symbiosil',
    version='1.0.0',
    author='Ashish Sahu',
    author_email='spiraldeveloper@gmail.com',
    url='https://github.com/stacknix/symbiosil',
    description='Symbiosil is living AI bot framework.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'symbiosil = symbiosil.cli:cli'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='python package symbiosil',
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False
)
