import torch 
test=torch.tensor([2,3])
test1=torch.tensor([2,3])
test_copy=test
test_end=test.add(test1)
test_end1=test*test1
test_copy.add_(test1)
print(test_end)
print(test_copy)
print(test_end1)
