import torch 
test=torch.rand(3)
test1=torch.rand(3,2,3,1)
test_end=test@test1
print(test_end)
