## How to install Python in OSX  
- - - -  
- homebrew: [homebrew](https://brew.sh/)  

# Install homebrew:  
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Install Python via homebrew:  
```bash
brew install python
```

# Check list of Python version in brew:  
```bash
brew info python
```

# Switch python version in brew:  
```bash
# example
brew switch python 3.6.5
```

# Install pipenv via homebrew:  
- Choose the Python version first.  
```
brew install pipenv
```

# Using pipenv  
- Create pipfile:  
```bash
cd project

pipenv shell --two

pipenv sheel --three
```

- Create pipfile.lock:  
```bash
pipenv install 
```

