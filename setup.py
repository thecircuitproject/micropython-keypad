from setuptools import setup, find_packages

with open("keypad/README.md", "r") as f:
    long_description = f.read()

setup(
    name="micro-keypad",
    version="0.0.3",
    description="The Keypad library is designed to simplify keypad interfacing in Micropython-based hardware projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="José Carlos Borrayo Tojín",
    author_email="thecircuitproject1@gmail.com",
    packages=find_packages(),
    install_requires=[],
    url="https://github.com/thecircuitproject/micropython-keypad",
    license="MIT",
    extras_require={"dev": ["pytest", "twine>=5.1.1"]},
    python_requires=">=3.4",
)
