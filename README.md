tip:

in vs code use terminal and type:

        git remote -v

this will give the ulr for the remote repo and you can quickly access remote repo ulr.


## Data Science Tutorial with VS Code

This project follows the [Data Science Tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial) provided by Visual Studio Code. The tutorial demonstrates how to set up a data science environment, work with Jupyter notebooks, and perform data analysis using Python and popular libraries like Pandas and Matplotlib.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

1. Clone the repository:

        git clone https://github.com/yourusername/yourproject.git

2. Navigate to the project directory:

        cd data-science-tutorial
   
3. Set up the Conda environment by using the yml from this repo:

        conda env create -f environment.yml

4. Activate the environment:

        conda activate myenv


## Usage

1. Open VS Code.
2. Launch the Jupyter notebook server:
  - Open the integrated terminal in VS Code (Ctrl + `).
  - Run the following command to start Jupyter:

        jupyter notebook

  - Open the notebook.ipynb file.

3. Execute the cells to perform the data analysis.

## Project Structure

        ├── data/               # Contains datasets used in the tutorial
        ├── notebooks/          # Jupyter notebooks with code and analysis
        ├── environment.yml     # Conda environment file for setting up the environment
        └── README.md           # Project README file

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bugs.

## Acknowledgments

This project is based on the VS Code Data Science Tutorial.


# Data Science in VS Code tutorial 

## Part 1. Prerequisites:
        Visual Studio Code
            Extensions:
                Python extension for VS Code
                Jupyter extension for VS Code
        Miniconda or Full Anaconda distribution

## Part 2. Set up a data science environment

## Part 3. Prepare the data

   - Play and clean the data
   - Check correlations
   - After preparation you will have a dataset that can be used for training a model
      - in this case we chose: 'sex', 'pclass','age','relatives','fare','survived'

## Part 4. Train and evaluate a model

   - For this section use the scikit-learn library (as it offers some useful helper functions) to process the dataset, train a classification model to determinen survivability on the boat and then use the model with the test data to determinen its accuracy.

   Steps:
   1. common first step to training a model is to divide the dataset to training and validation data. This allows you to use a portion of the data to train the model and a portion of the data to test the model. If you used all your data to train the model, you wouldn't have a way to estimate how well it would actually perform against data the model hasn't yet seen. A benefit of the scikit-learn library is that it provides a method specifically for splitting a dataset into training and test data.
    
   Add and run a cell with the following code to the notebook to split up the data.

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(data[['sex','pclass','age','relatives','fare']], data.survived, test_size=0.2, random_state=0)

