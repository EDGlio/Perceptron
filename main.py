# Simple Perceptron algorithm
# EDGlio
# 15, 3, 2022

import functions

# Initializing variables
k = functions.Perceptron(16)

data = [
  [[
  0, 1, 1, 0,
  1, 0, 0, 1,
  1, 0, 0, 1,
  0, 1, 1, 0,
  ], 0],
  [[
  0, 0, 0, 0,
  0, 1, 1, 0,
  0, 1, 1, 0,
  0, 0, 0, 0,
  ], 1]
]

k.full_learning(data)
