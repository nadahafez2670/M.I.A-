# Neural Network Implementation: From Scratch vs PyTorch

## Overview

In this project, we implemented and trained neural networks using two different approaches:

1. Building a neural network completely from scratch using Python and a custom automatic differentiation engine.
2. Implementing a neural network using PyTorch to understand how modern deep learning frameworks simplify the training process.

The main objective was to understand the internal mechanisms of neural networks, including forward propagation, computational graphs, backpropagation, gradient calculation, and parameter updates, then compare this manual implementation with a real deep learning framework.

---

# Part 1: Neural Network From Scratch

## Description

In the first part, we built a complete neural network without using any deep learning libraries.

The implementation focused on understanding how neural networks work internally by manually creating the main components.

The model was trained on the **8×8 handwritten digits dataset**.

---

## Implemented Components

### 1. Custom Value Class (Autograd Engine)

A custom `Value` class was implemented to support automatic differentiation.

The class was responsible for:

* Storing numerical values
* Tracking the computational graph
* Storing gradients
* Performing backward propagation

Operations such as:

* Addition
* Multiplication
* Power
* Negation
* Subtraction
* Division

were implemented manually.

The backward pass was created by traversing the computational graph and applying the chain rule to calculate gradients.

---

### 2. Neural Network Components

The neural network was built from basic components:

### Neuron

Each neuron performs:

[
z = \sum wx + b
]

where weights and biases are learnable parameters.

---

### Layer

A layer contains multiple neurons and processes multiple inputs simultaneously.

---

### Multi-Layer Perceptron (MLP)

Multiple layers were combined to create the complete neural network.

The training pipeline included:

1. Forward propagation
2. Loss calculation
3. Backpropagation
4. Parameter update using gradient descent

---

## From-Scratch Results

The scratch implementation achieved:

* Test Accuracy: **85.56%**
* Dataset size: **1437 training samples**
* Input features per image: **64**
* Number of parameters: **2410**

Training was performed using manually implemented operations, which provided a better understanding of the internal behavior of neural networks.

---

# Part 2: PyTorch Neural Network

## Description

In the second part, the same neural network concept was implemented using PyTorch.

Instead of manually implementing the computational graph and gradient calculations, PyTorch provides:

* Automatic differentiation through Autograd
* Optimizers for parameter updates
* Efficient tensor operations

The model was trained on the real **MNIST dataset**.

---

## PyTorch Implementation

The workflow included:

1. Loading and preprocessing MNIST data
2. Creating a neural network using PyTorch layers
3. Performing forward propagation
4. Computing loss using a built-in loss function
5. Calculating gradients using `loss.backward()`
6. Updating parameters using an optimizer

PyTorch automatically manages the computational graph and gradient calculations.

---

## PyTorch Results

The PyTorch implementation achieved:

* Test Accuracy: **97.84%**
* Dataset size: **60000 training samples**
* Input features per image: **784**
* Number of parameters: **101770**

Despite having a much larger dataset, more input features, and more parameters, PyTorch trained significantly faster due to its optimized implementation.

---

# Results Comparison

|                          | From-Scratch (8×8 digits) | PyTorch (Real MNIST) |
| ------------------------ | ------------------------- | -------------------- |
| Dataset size (train)     | 1437                      | 60000                |
| Inputs per image         | 64                        | 784                  |
| Number of parameters     | 2410                      | 101770               |
| Time per epoch (approx.) | ~3 minutes                | ~6 seconds           |
| Test accuracy            | 85.56%                    | 97.84%               |

---

# Understanding the Difference Between Both Approaches

Although both implementations perform the same fundamental steps, they differ greatly in how computations are handled.

## Gradient Calculation

In the scratch implementation:

* The `Value` class creates a computational graph.
* Calling `backward()` on the loss manually propagates gradients through this graph.

This corresponds to PyTorch:

```python
loss.backward()
```

---

## Resetting Gradients

In the scratch implementation:

```python
neural_network.zero_grad()
```

resets gradients before calculating new ones.

This corresponds to:

```python
optimizer.zero_grad()
```

in PyTorch.

---

## Updating Parameters

In the scratch version, parameters are updated manually:

```python
parameter.data -= learning_rate * parameter.grad
```

This is equivalent to:

```python
optimizer.step()
```

in PyTorch.

---

# Why PyTorch is Faster?

Although both approaches perform the same mathematical operations, PyTorch is much faster because it uses optimized tensor-based computations.

## Scalar Operations vs Tensor Operations

The scratch implementation works with individual scalar values.

Every operation creates a separate object and requires Python-level processing.

PyTorch works with tensors, allowing thousands of operations to be executed together efficiently.

---

## Python Loops vs Optimized Kernels

The scratch implementation depends heavily on Python loops, which are slower.

PyTorch uses optimized C/C++ backend operations and can also use CUDA for GPU acceleration.

This allows PyTorch to perform matrix operations much faster.

---

# Conclusion

Building the neural network from scratch provided a strong understanding of the internal mechanisms behind deep learning, especially computational graphs and backpropagation.

The PyTorch implementation showed how modern frameworks automate these processes and provide efficient training through optimized tensor operations.

The comparison demonstrates that while manual implementation is valuable for learning, frameworks like PyTorch are essential for building and training practical deep learning models efficiently.
