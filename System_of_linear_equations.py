import torch

#Create model class

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()

        # Create model parameters
        self.x =  torch.nn.Parameter(torch.zeros((2, 1)))
        #Create A and b part of equation
        # Put your equations to matrix shape - form Ax-b = 0
        self.A = torch.tensor([[1., 1.], [3., 2.]])
        self.b = torch.tensor([[-2.], [0.]])

    def forward(self,x):
        y = torch.matmul(self.A, x) - self.b
        return y


if __name__ == "__main__":
    #Create model
    model = Model()

    #Define optimizer and put x in it
    optimizer = torch.optim.Adam(model.parameters(), lr=0.5)


    for _ in range(50):

        #Put x to model
        y = model.forward(model.x)

        #Calculate loss
        loss = (y**2).mean()


        #Zero gradients
        optimizer.zero_grad()
        #Calculate dx
        loss.backward()
        #Update x
        optimizer.step()

    x = -model.x.detach().numpy()[0]
    print("X is equal to - ",-x[0])