# Simple Perceptron algorithm
# EDGlio
# 15, 3, 2022

import numpy as np

def get_vector(num_inputs):
  return [[0] * num_inputs]

class Perceptron:
  def __init__(self, num_inputs):
    self.num_inputs = num_inputs
    self.eval_vector = get_vector(self.num_inputs)
    self.bias = 5
    print(self.eval_vector)

  # Evaluate the Matrix
  def evaluate(self, inputs):
    evaluation = [np.array(self.eval_vector)).dot(np.array(inputs)][0]
    if evaluation > self.bias:
      return 1
    else:
      return 0

  # Checking the perceptron versus the input
  def learn(self, inputs, correct):
    output = self.evaluate(inputs)
    if output > correct:
      self.eval_vector = np.array(self.eval_vector) - np.array(inputs)
    if output < correct:
      self.eval_vector = np.array(self.eval_vector) + np.array(inputs)
  
  # Commencing the learning
  def full_learning(self, data):
    run = True
    while run:
      run = False
      for i in range(len(data)):
        if self.learn(data[i][0], data[i][1]):
          run = True # Continues if any errors occur
    print(self.eval_vector)
