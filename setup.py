from setuptools import setup, find_packages

setup(
    name="important_personal_packages",                    
    version="0.1.0",                        
    description="Packages that i will use in future", 
    long_description=open("README.md").read(),     # Detailed description (from README.md)
    long_description_content_type="text/markdown", # Description format
    author="Tirthankar Ghosh",                    
    author_email="tirthankar.ghosh.isno1@gmail.com",  
    url="https://github.com/tirthadagr8/personal_library_packages",  # GitHub repo URL
    packages=find_packages(),               # Automatically finds "hid_keycodes" folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",                # Minimum Python version
)
