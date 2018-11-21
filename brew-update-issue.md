## brew update issue  
- - - -  
When brew update and brew upgrade, it will update the python3.  
Originally python3 was install via brew and it was python 3.6.5.  
brew update and brew upgrade cause upgrade python version to 3.7.1.  
I cause serval issue with existing develop environment issue.  
The issues as follows:  
- macvim  
- pipenv  


The main cause is when brew install a package depends on python3, which is also installed via brew.  
It stick to the installed version when the package is installed at first.  
Resulting pipenv's malfunction because of python version has been updated.  
Even if re-install pipenv with the newer version of python, it still search for the older version of python in runtime.  
Re-install cause more problem because even if brew switch python 3.6.5 can't help because it need to start a run with python 3.7.1.  
To summarize the issue:  
- Upgrade to python version 3.7.1  
- Staring pipenv is OK  
- Can't run because pipenv can't find python version 3.6.5 in environment.  


- Re-install pipenv with python version 3.7.1  
- Starting pipenv is OK  
- Can't run because pipenv can't find python version 3.6.5 in environment.  


- brew switch python version 3.6.5  
- Can't start the pipenv because re-installation make depency to 3.7.1  


To resolve the issue, brew uninstall pipenv and install via curl  
This time, make user the brew switch python 3.6.5 and install via curl  



