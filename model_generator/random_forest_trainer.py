# -*- coding: utf-8 -*-

# Random Forest Classification on Tensorflow
# Import libraries
import gen as generator
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources

import sklearn
from sklearn.model_selection import train_test_split

# Ignore all GPUs, tf random forest does not benefit from it.
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# Import data
try:
    data = pd.read_csv('./truth_template_dataset.csv', index_col=0, skiprows=range(1))
except: 
    generator.generate()
    data = pd.read_csv('./truth_template_dataset.csv', index_col=0, skiprows=range(1))


#Extract feature and target np arrays (inputs for placeholders)
input_x = data.iloc[:, 0:-1].values
input_y = data.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(input_x, input_y, test_size = 0.25, random_state = 0)
data1 = data.iloc[:,:].values

# Parameters
num_steps = 100 # Total steps to train
num_classes = 5 
num_features = 6 
num_trees = 10 
max_nodes = 1000 

# Input and Target placeholders 
X = tf.placeholder(tf.float32, shape=[None, num_features])
Y = tf.placeholder(tf.int64, shape=[None])

# Random Forest Parameters
hparams = tensor_forest.ForestHParams(num_classes=num_classes, num_features=num_features, num_trees=num_trees, max_nodes=max_nodes).fill()

# Build the Random Forest
forest_graph = tensor_forest.RandomForestGraphs(hparams)

# Get training graph and loss
train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

# Measure the accuracy
infer_op, _, _ = forest_graph.inference_graph(X)
correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Initialize the variables (i.e. assign their default value) and forest resources
init_vars = tf.group(tf.global_variables_initializer(), resources.initialize_resources(resources.shared_resources()))
    
# Start TensorFlow session
sess = tf.Session()

# Run the initializer
sess.run(init_vars)

# Training
for i in range(1, num_steps + 1):
    _, l = sess.run([train_op, loss_op], feed_dict={X: X_train, Y: y_train})
    if i % 50 == 0 or i == 1:
        acc = sess.run(accuracy_op, feed_dict={X: X_train, Y: y_train})
        print('Step %i, Loss: %f, Acc: %f' % (i, l, acc))

# Test Model
print("Test Accuracy:", sess.run(accuracy_op, feed_dict={X: X_test, Y: y_test}))


#do a prediction
y_sample =  np.array([1,2,3,4])
x_sample =  np.array([[724,11,0,3,360,1]])
#array([321,   1,   1,  73,  35,   5], dtype=int64)
print("Test Accuracy - intermediate:", sess.run(accuracy_op, feed_dict={X: x_sample, Y: np.array([1])}))
print("Test Accuracy - novice:", sess.run(accuracy_op, feed_dict={X: x_sample, Y: np.array([2])}))
print("Test Accuracy - disqualified:", sess.run(accuracy_op, feed_dict={X: x_sample, Y: np.array([3])}))
print("Test Accuracy - expert:", sess.run(accuracy_op, feed_dict={X: x_sample, Y: np.array([4])}))

print("done")
