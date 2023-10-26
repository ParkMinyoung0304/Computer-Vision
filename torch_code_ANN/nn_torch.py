import torch
import torch.nn.functional as F

input = torch.tensor([[1,0,2,3,1],
                     [4,5,6,7,1],
                     [8,9,10,11,1],
                     [2,1,3,4,1],
                     [2,4,3,6,4]])

kernel = torch.tensor([[1,0,1],
                       [0,1,0],
                       [1,0,1]])

input = torch.reshape(input, (1,1,5,5))
kernel = torch.reshape(kernel, (1,1,3,3))

print(input.shape)
print(kernel.shape)

#步长为1
output = F.conv2d(input, kernel, stride=1)
print(output)

#步长为2
output = F.conv2d(input, kernel, stride=2)
print(output)

#padding为1
output = F.conv2d(input, kernel, padding=1)
print(output)