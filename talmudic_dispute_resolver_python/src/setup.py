from setuptools import setup, find_packages

setup(
    name="talmudic_dispute_resolver_python",
    version="1.0.0",
    author="Your Name",
    author_email="mbialost@gmainl.com",
    description="A Talmudic dispute resolver implementation in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mbialost/talmudic_dispute_resolver",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'talmudic-dispute-resolver=resolution:main',
        ],
    },
)
