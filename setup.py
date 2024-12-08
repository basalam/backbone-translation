from setuptools import setup, find_namespace_packages

setup(
    name="backbone-translation",
    author="Mojtabaa Habibain",
    author_email="mojtabaa.hn@gmail.com",
    description="Python Utilities & Basalam Micro-Services SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/basalam/backbone-translation",
    packages=find_namespace_packages(where='src', include=['basalam.backbone_translation']),
    package_dir={'': 'src'},
    namespace_packages=["basalam"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setuptools_git_versioning={"enabled": True},
    setup_requires=["setuptools-git-versioning"],
)
