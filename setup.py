from setuptools import setup, find_packages

setup(
    name="student-management-system",
    version="1.0.0",
    description="A modern student management system with GUI",
    author="Mohammad Mehdi Bagheri",
    author_email="mehdibagheri.official@gmail",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'student-management=src.main:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
