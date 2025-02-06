from setuptools import setup, find_packages

setup(
    name="cat_processor",
    version="0.1.0",
    author="Jessica",
    author_email="jessicakah2307@gmail.com",
    description="Pacote para processamento de imagens de gatos.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JessicaVieiraKah/cat-image-processor",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "opencv-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
