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

### Step 1
   common first step to training a model is to divide the dataset to training and validation data. This allows you to use a portion of the data to train the model and a portion of the data to test the model. If you used all your data to train the model, you wouldn't have a way to estimate how well it would actually perform against data the model hasn't yet seen. A benefit of the scikit-learn library is that it provides a method specifically for splitting a dataset into training and test data. Add and run a cell with the following code to the notebook to split up the data.

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(data[['sex','pclass','age','relatives','fare']], data.survived, test_size=0.2, random_state=0)

### Step 2
   Next, normalize the inputs such that all features are treated equally. For example, within the dataset the values for age range from ~0-100, while gender is only a 1 or 0. By normalizing all the variables, you can ensure that the ranges of values are all the same. Use the following code in a new code cell to scale the input values.

        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(x_train)
        X_test = sc.transform(x_test)

### Step 3
   There are many machine learning algorithms to choose from to model the data. The scikit-learn library provides support for many of [them](https://scikit-learn.org/stable/user_guide.html) and a [chart](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) to help select the one that's right for your scenario. For now, use the [Naïve Bayes algorithm](https://scikit-learn.org/stable/modules/naive_bayes.html), a common algorithm for classification problems. Add a cell with the following code to create and train the algorithm.

   from sklearn.naive_bayes import GaussianNB
   model = GaussianNB()
   model.fit(X_train, y_train)

### Step 4
   With a trained model, you can now try it against the test data set that was held back from training. Add and run the following code to predict the outcome of the test data and calculate the accuracy of the model.


## Part 5 (Optional) Use a neural network

   - A neural network is a model that uses weights and activation functions, modeling aspects of human neurons, to determine an outcome based on provided inputs. Unlike the machine learning algorithm you looked at previously, neural networks are a form of deep learning wherein you don't need to know an ideal algorithm for your problem set ahead of time. It can be used for many different scenarios and classification is one of them. For this section, you'll use the [Keras](https://keras.io/) library with [TensorFlow](https://www.tensorflow.org/) to construct the neural network, and explore how it handles the Titanic dataset.