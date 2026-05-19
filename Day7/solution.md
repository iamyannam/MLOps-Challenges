-----------------
Corrected pyproject.toml
***************
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "fraud_detection"
version = "0.1.0"
description = "Fraud detection model for xFusionCorp Industries"
requires-python = ">=3.10"
dependencies = ["scikit-learn", "pandas", "numpy"]

[tool.setuptools.packages.find]
where = ["src"]

-----------------
root@controlplane ~/code ✖ cd fraud-detection/

root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ➜  python3 -m build
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools>=61.0
  - wheel
* Getting build dependencies for sdist...
running egg_info
creating src/fraud_detection.egg-info
writing src/fraud_detection.egg-info/PKG-INFO
writing dependency_links to src/fraud_detection.egg-info/dependency_links.txt
writing requirements to src/fraud_detection.egg-info/requires.txt
writing top-level names to src/fraud_detection.egg-info/top_level.txt
writing manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
reading manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
writing manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
* Building sdist...
running sdist
running egg_info
writing src/fraud_detection.egg-info/PKG-INFO
writing dependency_links to src/fraud_detection.egg-info/dependency_links.txt
writing requirements to src/fraud_detection.egg-info/requires.txt
writing top-level names to src/fraud_detection.egg-info/top_level.txt
reading manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
writing manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
creating fraud_detection-0.1.0
creating fraud_detection-0.1.0/src/fraud_detection
creating fraud_detection-0.1.0/src/fraud_detection.egg-info
copying files to fraud_detection-0.1.0...
copying pyproject.toml -> fraud_detection-0.1.0
copying src/fraud_detection/__init__.py -> fraud_detection-0.1.0/src/fraud_detection
copying src/fraud_detection/predict.py -> fraud_detection-0.1.0/src/fraud_detection
copying src/fraud_detection.egg-info/PKG-INFO -> fraud_detection-0.1.0/src/fraud_detection.egg-info
copying src/fraud_detection.egg-info/SOURCES.txt -> fraud_detection-0.1.0/src/fraud_detection.egg-info
copying src/fraud_detection.egg-info/dependency_links.txt -> fraud_detection-0.1.0/src/fraud_detection.egg-info
copying src/fraud_detection.egg-info/requires.txt -> fraud_detection-0.1.0/src/fraud_detection.egg-info
copying src/fraud_detection.egg-info/top_level.txt -> fraud_detection-0.1.0/src/fraud_detection.egg-info
copying src/fraud_detection.egg-info/SOURCES.txt -> fraud_detection-0.1.0/src/fraud_detection.egg-info
Writing fraud_detection-0.1.0/setup.cfg
Creating tar archive
removing 'fraud_detection-0.1.0' (and everything under it)
* Building wheel from sdist
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools>=61.0
  - wheel
* Getting build dependencies for wheel...
running egg_info
writing src/fraud_detection.egg-info/PKG-INFO
writing dependency_links to src/fraud_detection.egg-info/dependency_links.txt
writing requirements to src/fraud_detection.egg-info/requires.txt
writing top-level names to src/fraud_detection.egg-info/top_level.txt
reading manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
writing manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
* Building wheel...
running bdist_wheel
running build
running build_py
creating build/lib/fraud_detection
copying src/fraud_detection/predict.py -> build/lib/fraud_detection
copying src/fraud_detection/__init__.py -> build/lib/fraud_detection
running egg_info
writing src/fraud_detection.egg-info/PKG-INFO
writing dependency_links to src/fraud_detection.egg-info/dependency_links.txt
writing requirements to src/fraud_detection.egg-info/requires.txt
writing top-level names to src/fraud_detection.egg-info/top_level.txt
reading manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
writing manifest file 'src/fraud_detection.egg-info/SOURCES.txt'
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/fraud_detection
copying build/lib/fraud_detection/predict.py -> build/bdist.linux-x86_64/wheel/./fraud_detection
copying build/lib/fraud_detection/__init__.py -> build/bdist.linux-x86_64/wheel/./fraud_detection
running install_egg_info
Copying src/fraud_detection.egg-info to build/bdist.linux-x86_64/wheel/./fraud_detection-0.1.0-py3.12.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/fraud_detection-0.1.0.dist-info/WHEEL
creating '/root/code/fraud-detection/dist/.tmp-hcr55l0g/fraud_detection-0.1.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'fraud_detection/__init__.py'
adding 'fraud_detection/predict.py'
adding 'fraud_detection-0.1.0.dist-info/METADATA'
adding 'fraud_detection-0.1.0.dist-info/WHEEL'
adding 'fraud_detection-0.1.0.dist-info/top_level.txt'
adding 'fraud_detection-0.1.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
Successfully built fraud_detection-0.1.0.tar.gz and fraud_detection-0.1.0-py3-none-any.whl
root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ➜  


<img width="1792" height="983" alt="image" src="https://github.com/user-attachments/assets/621f4173-31a3-4cb0-8f6f-7433c894d6c1" />
