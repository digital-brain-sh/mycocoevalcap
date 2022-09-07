from setuptools import setup, find_namespace_packages, find_packages

# Prepend pycocoevalcap to package names
# package_names = ['mycocoevalcap.'+p for p in find_namespace_packages()]

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='mycocoevalcap',
    version=1.2,
    maintainer='jxchen',
    description="MS-COCO Caption Evaluation for Python 3",
    long_description=readme,
    long_description_content_type="text/markdown",
    # url="https://github.com/salaniz/pycocoevalcap",
    # packages=['mycocoevalcap']+package_names,
    packages=find_packages(),
    # package_dir={'mycocoevalcap': '.'},
    package_data={'': ['*.jar', '*.gz']},
    install_requires=['pycocotools>=2.0.2'],
    python_requires='>=3'
)
