from setuptools import setup, find_packages

setup(
    name='talmudic_dispute_resolver',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # list your package dependencies here
        # e.g., 'requests', 'pandas', etc.
    ],
    entry_points={
        'console_scripts': [
            # if you have any scripts you want to be accessible from the command line
            # e.g., 'talmudic-resolver = talmudic_dispute_resolver.main:main_function'
        ],
    },
)
