import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='compressortoolbox',
    version='0.0.3',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Compressor Toolbox for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['compressortoolbox'],
    install_requires=[],
)