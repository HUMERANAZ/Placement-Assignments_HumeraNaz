import tensorflow as tf
from tensorflow.keras import layers

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess the data
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# Set the number of classes
num_classes = 10

# Define the first CNN architecture
model1 = tf.keras.Sequential([
    layers.Conv2D(16, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(num_classes, activation="softmax")
])

# Compile the model
model1.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model1.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2)

# Evaluate the model
_, accuracy1 = model1.evaluate(x_test, y_test, verbose=0)
print("Model 1 Accuracy:", accuracy1)

# Define the second CNN architecture
model2 = tf.keras.Sequential([
    layers.Conv2D(8, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(16, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(num_classes, activation="softmax")
])

# Compile the model
model2.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model2.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2)

# Evaluate the model
_, accuracy2 = model2.evaluate(x_test, y_test, verbose=0)
print("Model 2 Accuracy:", accuracy2)

# Define the third CNN architecture
model3 = tf.keras.Sequential([
    layers.Conv2D(4, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.Conv2D(8, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(32, activation="relu"),
    layers.Dense(num_classes, activation="softmax")
])

# Compile the model
model3.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model3.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2)

# Evaluate the model
_, accuracy3 = model3.evaluate(x_test, y_test, verbose=0)
print("Model 3 Accuracy:", accuracy3)
