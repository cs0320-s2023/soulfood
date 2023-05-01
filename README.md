# soulfood

## Dependencies and env to run the program:

For the python backend, install conda following this webpage: https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html

Create a virtual environment using: conda create --name myenv

Activate the virtual environment by running: conda activate myenv
Remember to follow the intructions on adding conda to PATH if you are using a windows computer. 

We need a version of python 3.9 for the surprise library to work: conda create -n myenv python=3.9

Install necessary dependencies: 
conda install pandas
conda install -c conda-forge scikit-surprise
