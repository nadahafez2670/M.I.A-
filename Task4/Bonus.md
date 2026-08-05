# Bonus Extensions Evaluation

## Performance Evaluation

The bonus version introduced several advanced deep learning techniques, including:

* Softmax output layer
* Cross Entropy Loss
* ReLU activation
* Improved weight initialization
* Momentum optimization
* Dropout regularization

Although these techniques are commonly used in modern neural networks and usually improve classification performance, the current bonus implementation did not outperform the original baseline model.

The original from-scratch implementation achieved better evaluation performance, while the bonus version requires additional tuning and debugging to reach its expected improvement.

Possible factors affecting the current performance include:

* Hyperparameter selection (learning rate, momentum factor, dropout probability)
* Training stability
* Interaction between Softmax and Cross Entropy implementation
* Optimization behavior with the custom autograd engine

The bonus implementation successfully demonstrates the integration of advanced neural network components, while further experiments are needed to achieve optimal performance.

---

## Comparison with Baseline Model

| Model                      | Main Techniques                                     | Test Accuracy |
| -------------------------- | --------------------------------------------------- | ------------- |
| Basic From-Scratch Network | Manual backpropagation + gradient descent           | 85.56%        |
| Bonus Version              | Softmax + Cross Entropy + ReLU + Momentum + Dropout | 63.61%        |

The baseline model achieved better accuracy in the current experiments. However, the bonus version provided valuable experience in implementing advanced training techniques and understanding their effect on neural network optimization.
