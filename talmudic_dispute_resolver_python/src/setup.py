from setuptools import setup, find_packages

setup(
    name="talmudic_dispute_resolver",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Talmudic dispute resolver implementation in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/talmudic_dispute_resolver",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your project dependencies here
        # e.g., "requests>=2.22.0"
    ],
    entry_points={
        'console_scripts': [
            'talmudic-dispute-resolver=resolution:main',
        ],
    },
)
