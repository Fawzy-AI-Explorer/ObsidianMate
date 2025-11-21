"""
Setup module for the <project_name> package.
"""

from setuptools import setup, find_packages

setup(
    name="project-boilerplate",
    version="1.0.0",
    description=(
        "A reusable project template with a clean structure and "
        "pre-configured setup to kickstart new projects."
    ),
    author="Adham Allam",
    author_email="adham32003200@gmail.com",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.12",
    license="MIT",
    license_files=["LICEN[CS]E*", "AUTHORS.md"],
    keywords=["boilerplate", "template", "project"],
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Setup Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    url="https://github.com/Ad7amstein/project-boilerplate",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            # Example: "mycli = my_package.cli:main",
        ],
    },
)
