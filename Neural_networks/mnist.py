from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from numpy import asarray


class MyNeural:
    class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, epoch_count):
        tf.compat.v1.disable_eager_execution()
        self.ses = tf.compat.v1.Session()
        self.epoch_count = epoch_count
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = self.load_data()
        self.model = self.build_model()
        self.scale_images()
        self.predictions = None
        self.history = None

    @staticmethod
    def load_data():
        mnist = keras.datasets.mnist
        return mnist.load_data()

    def scale_images(self):
        self.train_images = self.train_images / 255.0
        self.test_images = self.test_images / 255.0

    def show_images(self, count=25):
        plt.figure(figsize=(10, 10))
        for i in range(count):
            plt.subplot(5, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(self.train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_names[self.train_labels[i]])
        plt.show()

    def build_model(self):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dropout(0.3),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dropout(0.3),
            keras.layers.Dense(10, activation='softmax')
        ])
        self.compile_model(model)
        return model

    @staticmethod
    def compile_model(model):
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def fit_model(self):
        self.history = self.model.fit(self.train_images, self.train_labels,
                                      epochs=self.epoch_count,
                                      validation_split=0.2,
                                      batch_size=512,
                                      verbose=0,
                                      callbacks=[self.Callback()])
        self.load_weights()
        self.save_model()

    class Callback(keras.callbacks.Callback):
        cnt = 0
        min_loss = np.inf
        min_epoch = None

        def on_epoch_end(self, epoch, logs):
            if logs['val_loss'] >= self.min_loss:
                self.cnt += 1
            else:
                self.cnt = 0
                self.min_loss = logs['val_loss']
                self.min_epoch = epoch
                checkpoint_path = "training/cp.ckpt"
                self.model.save_weights(checkpoint_path.format(epoch=epoch))
            if self.cnt == 20:
                self.model.stop_training = True

    def load_weights(self):
        self.model = neural.build_model()
        checkpoint_path = "training/cp.ckpt"
        self.model.load_weights(checkpoint_path)

    def save_model(self):
        self.model.save('my_model.h5')

    def load_model(self):
        self.model = keras.models.load_model('my_model.h5')

    def get_loss_and_acc(self):
        test_loss, test_acc = self.model.evaluate(self.test_images, self.test_labels, verbose=2)
        print('\nТочность на проверочных данных:', test_acc)

    def get_predictions(self):
        self.predictions = self.model.predict(self.test_images)
        # for i in range(100):
        #     print(np.argmax(self.predictions[i]), self.test_labels[i])

    def plot_image(self, i, predictions_array, true_label, img):
        predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])

        plt.imshow(img, cmap=plt.cm.binary)

        predicted_label = np.argmax(predictions_array)
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'

        plt.xlabel("{} {:2.0f}% ({})".format(self.class_names[predicted_label],
                                             100 * np.max(predictions_array),
                                             self.class_names[true_label]),
                   color=color)

    @staticmethod
    def plot_value_array(i, predictions_array, true_label):
        predictions_array, true_label = predictions_array[i], true_label[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10), predictions_array, color="#777777")
        plt.ylim([0, 1])
        predicted_label = np.argmax(predictions_array)

        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')

    def get_one_image_and_table(self, number):
        plt.figure(figsize=(6, 3))
        plt.subplot(1, 2, 1)
        self.plot_image(number, self.predictions, self.test_labels, self.test_images)
        plt.subplot(1, 2, 2)
        self.plot_value_array(number, self.predictions, self.test_labels)
        plt.show()

    def get_many_images_and_table(self, num_rows, num_cols):
        num_images = num_rows * num_cols
        plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
        for i in range(num_images):
            plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
            self.plot_image(i, self.predictions, self.test_labels, self.test_images)
            plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
            self.plot_value_array(i, self.predictions, self.test_labels)
        plt.show()

    @staticmethod
    def plot_history(history):
        hist = pd.DataFrame(history.history)
        hist['epoch'] = history.epoch

        plt.figure()
        plt.xlabel('Epoch')
        plt.ylabel('loss')
        plt.plot(hist['epoch'], hist['loss'],
                 label='Train loss')
        plt.plot(hist['epoch'], hist['val_loss'],
                 label='Val loss')
        plt.ylim([0, 1])
        plt.legend()

        plt.figure()
        plt.xlabel('Epoch')
        plt.ylabel('accuracy')
        plt.plot(hist['epoch'], hist['accuracy'],
                 label='Train accuracy')
        plt.plot(hist['epoch'], hist['val_accuracy'],
                 label='Val accuracy')
        plt.ylim([0.6, 1])
        plt.legend()
        plt.show()

    def go_predict(self, img):
        image = Image.open(img)
        data = asarray(image)
        data = data[..., 0]
        data = 1 - data / 255
        img = (np.expand_dims(data, 0))
        predictions_single = self.model.predict(img)
        print(np.argmax(predictions_single[0]))


if __name__ == '__main__':
    neural = MyNeural(150)
    # neural.show_images()
    neural.build_model()
    # neural.fit_model()
    neural.load_model()
    # neural.get_loss_and_acc()
    # neural.get_predictions()
    # neural.get_one_image_and_table(12)
    # neural.get_many_images_and_table(5, 3)
    # neural.plot_history(neural.history)
    neural.go_predict('image.png')

