# Code artifacts for visualization and multi-level linear regression analysis of codeTMS data

## Directory contents

### Scripts
1. `data-management.ipynb` generates a single `.csv` file from the raw data stored in `test-data-[x]`. This script should be run before either of the other two.
2. `data-visualization.ipynb` generates plots of various aspects of the data using standard Python tools.
3. `regression-analysis.Rmd` contains data analysis presented for RQs 2-4 of the submitted paper.

### Data files and other outputs
1. `test-data-1` contains the raw data input to `data-management.ipynb`
2. `processed-data-1` contains anonymized data output from `data-management.ipynb`
3. `processed-data-2` contains non-anonymized data output from `data-management.ipynb`
4. FIXME visualizations and R script output

## Installation
Data management and visualization are done in Python. Regression analysis and additional visualization are done in R. Setup instructions for both are provided below.

### Python setup

The two `.ipynb` files are Python Notebooks and require the standard Jupyter support. There are several ways to set this up; one option is presented here.

#### First time setup:
1. Run `pip install conda` if you don't already have it.
2. Run `conda env list`. You should see a `base` environment with a filepath.
3. Run `conda activate base` to activate the virtual environment. Alternatively, you can create and use a different virtual environment for this project.
4. Run `pip install ipykernel ipython jupyter jupyterlab numpy matplotlib scipy pandas PyWavelets`.
5. Run `python -m ipykernel install --user --name=[choose-a-name-related-to-this-project]`. This starts a python kernel, using the current virtual environment, for the  Jupyter notebook to connect to.
6. Run `pip install -U "jupyter-server<2.0.0"`.
7. Run `jupyter notebook`. Check for errors in the output and follow any instructions (e.g. missing packages) depending on your setup. You may need to repeat this command multiple times until all errors are resolved.
    - If you use WSL/WSL2 on Windows, run `jupyter notebook --port=8889 --no-browser` instead.
    - You can safely ignore any prompts related to upgrading to Notebook 7.
    - You can safely ignore most warnings.
8. At the end of the output from the previous command, there will be a block of text like the following. Follow the instructions to open the project directory in Jupyter.
```
[C 22:32:19.671 NotebookApp]

To access the notebook, open this file in a browser:
    file:///home/emshedde/.local/share/jupyter/runtime/nbserver-15057-open.html
Or copy and paste one of these URLs:
    http://localhost:8889/?token=7a40b78e800ac1574c7435815ccb54497ac50eaac846db92
    or http://127.0.0.1:8889/?token=7a40b78e800ac1574c7435815ccb54497ac50eaac846db92
```
9. Code is ready to edit/run within the browser.

#### Subsequent use:
1. Run `conda activate base` to activate the virtual environment. If you created a different venv for this project, activate that (you can check what venvs are available using `conda env list`).
2. Run `jupyter notebook`.
    - Again, if you use WSL/WSL2 on Windows, run `jupyter notebook --port=8889 --no-browser` instead.
3. Follow the instructions to open the project directory in Jupyter.

#### Ending the session:
1. When you're done, make sure to save changes (upper left corner). Close the browser window and return to the command line.
2. Type `Ctrl + C`, then `y` to terminate the Jupyter session.
3. Run `conda deactivate` to deactivate the virtual environment.

Source: [This guide](https://devinschumacher.com/how-to-setup-jupyter-notebook-virtual-environment-vs-code-kernels/).

### R setup

Follow the instructions on [CRAN](https://cran.rstudio.com/) to install R.

## Usage

Run `data-management.ipynb` first. For the results presented in the paper, run `regression-analysis.Rmd` next. Visualization is provided for the interest of the reader, and is not included in the paper.

Specific usage instructions can be found at the beginning of each notebook. In particular, note that configurable options can be changed according to the preference of the user. 

Results of the data management and visualization scripts can be viewed in the notebook or as separate output files. Regression analysis results are best viewed in the notebook, as file output is very verbose and not all results are included.
