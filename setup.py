from setuptools import setup, find_packages
from Cython.Build import cythonize

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="dmtapi",
    version="2025.0.dev0",
    ext_modules=cythonize(
        "dmtapi/**/*.py",
        compiler_directives={
            'language_level': "3",
            'boundscheck': False,       # No bounds checking (fast, but unsafe)
            'wraparound': False,        # No negative indexing checks
            'initializedcheck': False,  # No uninitialized variable checks
            'nonecheck': False,         # No None checks
            'cdivision': True,          # Use C-style division (faster)
            'profile': False,           # Disable profiling overhead
            'infer_types': True         # Let Cython infer types (faster execution)
        },
        exclude=["dmtapi/tests/*"]
    ),
    options={"build_ext": {"parallel": True}},
    packages=find_packages(include=["dmtapi", "dmtapi.*"]),
    install_requires=[
        "httpx>=0.28.1",
        "aiohttp>=3.11.12",
        "pendulum>=3.0.0",
        "pydantic>=2.10.6"
    ],
    author="Hamim (Dynamo)",
    author_email="developer@dynamotrader.com",
    description="Dynamo MetaTrader API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dynamotrader/dmtapi",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
)
