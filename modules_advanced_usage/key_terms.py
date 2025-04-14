# Module - A Python file containing reusable code like functions or classes

# Import - Retrieves modules making their contents available in current namespace

# Virtualenv - Self-contained directory housing isolated Python packages/dependencies

# Activation - Configures shell to use virtualenv's dedicated Python interpreter

# Pip - Python tool for installing/managing packages and dependencies

# Import module 
import utils

# Access function  
print(utils.format_name("Wyclef"))

# Virtualenv creation
python3 -m venv env

# Activate virtualenv 
source env/bin/activate  

# Install dependency
pip install pandas  

# Deactivate when done
deactivate
