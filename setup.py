from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["wheel"] # 这里填依赖包信息

setup(
    name = "BaseConverter",
    version = "0.0.1",
    author = "makabaka1880",
    author_email = "makabaka1880@outlook.com",
    description = "A package to convert number to different bases",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/your_package/homepage/",
    packages = find_packages(),
    # Single module也可以：
    # py_modules=['timedd']
    install_requires = requirements,
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)