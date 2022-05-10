from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name="BMDFO",
    version="1.0.1",
    description="Python package that benchmark DFO algorithms mainly OMADS.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    author="Ahmed H. Bayoumy",
    author_email='ahmed.bayoumy@mail.mcgill.ca',
    url='https://github.com/Ahmed-Bayoumy/BM_DFO',
    license="GPL",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    keywords="Derivative free optimization",
    packages=find_packages(),
    install_requires="requests>=2",
    python_requires="~=3.8"
)