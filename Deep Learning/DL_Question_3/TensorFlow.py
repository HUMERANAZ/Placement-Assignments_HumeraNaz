import tensorflow as tf
from tensorflow.keras import layers, models
import tensorflow_datasets as tfds

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Normalize and reshape the images
train_images = train_images.reshape(-1, 28, 28, 1) / 255.0
test_images = test_images.reshape(-1, 28, 28, 1) / 255.0

# Set the number of classes
num_classes = 10

# Define the CNN model
model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(num_classes, activation='softmax')
])

# Print the model summary
model.summary()

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# Define the training parameters
num_epochs = 10
batch_size = 64

# Train the model
model.fit(train_images, train_labels, epochs=num_epochs, batch_size=batch_size)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("Validation Accuracy: {:.2f}%".format(test_accuracy * 100))
