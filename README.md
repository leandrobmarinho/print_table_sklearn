## Print table with results from Scikit-learn

![](screen.png?raw=true)

### Install virtualenv via pip:
pip install virtualenv

### Test your installation
virtualenv --version



### Create the virtualenv for the project
cd print_table_sklearn\
virtualenv .env -p python3 --no-site-packages

### To begin using the virtual environment, it needs to be activated:
. .env/bin/activate

### Intall the packages
pip install -r requirements.txt

### Run the application
python3 run_create_table.py

#### If you are done working in the virtual environment for the moment, you can deactivate it:
deactivate


