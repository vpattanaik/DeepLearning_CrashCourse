import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# loading dataset
mnist = tf.keras.datasets.mnist

# preparing data
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

fig, a = plt.subplots(2, 5)
a[0][0].imshow(x_train[0])
a[0][0].axis('off')
a[0][1].imshow(x_train[1])
a[0][1].axis('off')
a[0][2].imshow(x_train[2])
a[0][2].axis('off')
a[0][3].imshow(x_train[3])
a[0][3].axis('off')
a[0][4].imshow(x_train[4])
a[0][4].axis('off')
a[1][0].imshow(x_train[5])
a[1][0].axis('off')
a[1][1].imshow(x_train[6])
a[1][1].axis('off')
a[1][2].imshow(x_train[7])
a[1][2].axis('off')
a[1][3].imshow(x_train[8])
a[1][3].axis('off')
a[1][4].imshow(x_train[9])
a[1][4].axis('off')
plt.show()

# simple four-layer Sequential model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# training
model.fit(x_train, y_train, epochs=5)

# testing
model.evaluate(x_test, y_test)
