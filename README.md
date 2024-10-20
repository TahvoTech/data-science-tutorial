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

### 4.1 Divide dataset to training and validation data
   common first step to training a model is to divide the dataset to training and validation data. This allows you to use a portion of the data to train the model and a portion of the data to test the model. If you used all your data to train the model, you wouldn't have a way to estimate how well it would actually perform against data the model hasn't yet seen. A benefit of the scikit-learn library is that it provides a method specifically for splitting a dataset into training and test data. Add and run a cell with the following code to the notebook to split up the data.

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(data[['sex','pclass','age','relatives','fare']], data.survived, test_size=0.2, random_state=0)

### 4.2 Normalize the inputs
   Next, normalize the inputs such that all features are treated equally. For example, within the dataset the values for age range from ~0-100, while gender is only a 1 or 0. By normalizing all the variables, you can ensure that the ranges of values are all the same. Use the following code in a new code cell to scale the input values.

        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(x_train)
        X_test = sc.transform(x_test)

### 4.3 Choose, create & train the algorithm
   There are many machine learning algorithms to choose from to model the data. The scikit-learn library provides support for many of [them](https://scikit-learn.org/stable/user_guide.html) and a [chart](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) to help select the one that's right for your scenario. For now, use the [Naïve Bayes algorithm](https://scikit-learn.org/stable/modules/naive_bayes.html), a common algorithm for classification problems. Add a cell with the following code to create and train the algorithm.

        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        model.fit(X_train, y_train)

### 4.4 Try the trained model against the test data set
   With a trained model, you can now try it against the test data set that was held back from training. Add and run the following code to predict the outcome of the test data and calculate the accuracy of the model.

        from sklearn import metrics
        predict_test = model.predict(X_test)
        print(metrics.accuracy_score(y_test, predict_test))


## Part 5 (Optional) Use a neural network

   - A neural network is a model that uses weights and activation functions, modeling aspects of human neurons, to determine an outcome based on provided inputs. Unlike the machine learning algorithm you looked at previously, neural networks are a form of deep learning wherein you don't need to know an ideal algorithm for your problem set ahead of time. It can be used for many different scenarios and classification is one of them. For this section, you'll use the [Keras](https://keras.io/) library with [TensorFlow](https://www.tensorflow.org/) to construct the neural network, and explore how it handles the Titanic dataset.

### 5.1 Import libraries and create the model
   The first step is to import the required libraries and to create the model. In this case, you'll use a [Sequential](https://keras.io/getting-started/sequential-model-guide/) neural network, which is a layered neural network wherein there are multiple layers that feed into each other in sequence.

        from keras.models import Sequential
        from keras.layers import Dense

        model = Sequential()

### 5.2 Create the layers of the neural network
   After defining the model, the next step is to add the layers of the neural network. For now, let's keep things simple and just use three layers. Add the following code to create the layers of the neural network.

        model.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu', input_dim = 5))
        model.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu'))
        model.add(Dense(1, kernel_initializer = 'uniform', activation = 'sigmoid'))

   
   - The first layer will be set to have a dimension of 5, since you have five inputs: sex, pclass, age, relatives, and fare.
   - The last layer must output 1, since you want a 1-dimensional output indicating whether a passenger would survive.
   - The middle layer was kept at 5 for simplicity, although that value could have been different.

   The rectified linear unit (relu) activation function is used as a good general activation function for the first two layers, while the sigmoid activation function is required for the final layer as the output you want (of whether a passenger survives or not) needs to be scaled in the range of 0-1 (the probability of a passenger surviving).

   You can also look at the summary of the model you built with this line of code:
   
        model.summary()

### 5.3 Compile the created model: Build & train
   Once the model is created, it needs to be compiled. As part of this, you need to define what type of optimizer will be used, how loss will be calculated, and what metric should be optimized for. Add the following code to build and train the model. You'll notice that after training, the accuracy is ~61%.

   Note: This step may take anywhere from a few seconds to a few minutes to run depending on your machine.

        model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(X_train, y_train, batch_size=32, epochs=50)

### 5.4 Test the created model against test data
   Now that the model is built and trained, we can see how it works against the test data.
        
        y_pred = np.rint(model.predict(X_test).flatten())
        print(metrics.accuracy_score(y_test, y_pred))

   Similar to the training, you'll notice that you now have 79% accuracy in predicting survival of passengers. Using this simple neural network, the result is better than the 75% accuracy from the Naive Bayes Classifier tried previously.


## Next steps

   Now that you're familiar with the basics of performing machine learning within Visual Studio Code, here are some other Microsoft resources and tutorials to check out.

   - [Data Science profile template](https://code.visualstudio.com/docs/editor/profiles#_data-science-profile-template) - Create a new [profile](https://code.visualstudio.com/docs/editor/profiles) with a curated set of extensions, settings, and snippets.
   - Learn more about working with [Jupyter Notebooks in Visual Studio Code](https://youtu.be/FSdIoJdSnig) (video).
   - [Get started with Azure Machine Learning for VS Code](https://learn.microsoft.com/azure/machine-learning/how-to-setup-vs-code) to deploy and optimize your model using the power of Azure.
   - Find more data to explore on [Azure Open Data Sets](https://azure.microsoft.com/services/open-datasets/).
