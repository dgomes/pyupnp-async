from setuptools import setup

with open("README.rst") as readme_file:
    readme_string = readme_file.read()

setup(
    name="pyupnp-async",
    version='0.1.0.0',
    description="Python Library for UPnP operations using asyncio",
    author="Xin Huang",
    author_email="xinhuang.abc@gmail.com",
    url="https://github.com/xinhuang/pyupnp-async",
    packages=['pyupnp_async', 'tests'],
    license="License :: OSI Approved :: MIT License",
    long_description=readme_string,
    install_requires=[
        'aiohttp',
        'async-timeout',
        'xmltodict',
    ],
)
