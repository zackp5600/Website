import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


loaded_model = tf.keras.models.load_model('generator_model.h5')

loaded_model.compile(optimizer='adam',  # You need to specify the optimizer
                     loss='sparse_categorical_crossentropy',  # You need to specify the loss function
                     metrics=['accuracy']) 


random_latent_vectors = tf.random.normal(shape=(1, 128))



predictions = loaded_model.predict(random_latent_vectors)


print(predictions.shape)
print(predictions.dtype)


predictions = np.clip(predictions, 0, 1)

plt.imshow(predictions[0])
plt.show()