# :exclamation:ReadMe - [First Keras Demo](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) by [Jason Brownlee](https://machinelearningmastery.com/)

## The `pima-indians-diabetes` dataset is available here

* [Dataset CSV File](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv)
* [Dataset Details](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names)

## The Keras Model

~~~
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
~~~

* The `first hidden layer` has `12 nodes` and uses the `relu` activation function.
* The `second hidden layer` has `8 nodes` and uses the `relu` activation function.
* The `output layer` has `one node` and uses the `sigmoid` activation function.

