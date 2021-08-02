import torch
#Put your equations to matrix shape - form Ax-b = 0
#Create x 
x = torch.nn.Parameter(torch.zeros((2, 1)))
#Create A and b part of equation
A = torch.tensor([[1., 1.], [3., 2.]])
b = torch.tensor([[-2.], [0.]])

#Define our "model"
def model(x):
    k =  torch.matmul(A, x)-b
    return k

#Define optimizer and put x in it
optimizer = torch.optim.Adam([x], lr=0.5)

for _ in range(50):
    #Put x to model
    y = model(x)
    #Calculate loss
    loss = (y**2).mean()
    print(loss)

    #Zero gradients
    optimizer.zero_grad()
    #Calculate dx
    loss.backward()
    #Update x 
    optimizer.step()

print(x[0],x[1], "X Y ")