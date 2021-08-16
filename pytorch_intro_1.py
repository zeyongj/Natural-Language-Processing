from __future__ import print_function
import torch

# Create a matrix w/o init.
x = torch.empty(5,3)
print(x)
# Output: tensor([[2.0431e-12, 8.1976e-43, 2.0431e-12],
#         [8.1976e-43, 2.0437e-12, 8.1976e-43],
#         [2.0437e-12, 8.1976e-43, 2.0433e-12],
#         [8.1976e-43, 2.0433e-12, 8.1976e-43],
#         [2.0434e-12, 8.1976e-43, 2.0434e-12]])
# Actually, not exact value for each entry. Meaningless data.

# Create a matrix w/ init.
y = torch.rand(5,3)
print(y)
# Output: tensor([[0.2608, 0.9908, 0.9984],
#         [0.6337, 0.6599, 0.7454],
#         [0.4625, 0.2361, 0.4855],
#         [0.7539, 0.7024, 0.4550],
#         [0.9314, 0.3171, 0.5338]])
# Actually, Gaussian Distribution. Real number, meaningful.



