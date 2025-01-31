from setuptools import setup, find_packages

setup(
    name="docflow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'pytesseract',
        'python-docx',
        'PyYAML',
        'pdf2image'
    ],
    entry_points={
        'console_scripts': [
            'docflow=docflow.cli:main'
        ]
    }
)
