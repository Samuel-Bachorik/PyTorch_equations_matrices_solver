import torch

#Create model class
class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()

        #Create model parameters
        self.x = torch.nn.Parameter(torch.zeros(1), requires_grad=True)
        #Create euation variables
        self.a = 2
        self.b = 3
        self.c = 1

    def forward(self,x):

        y = self.a * x ** 2 + self.b * x + self.c
        return y


if __name__ == "__main__":
    #Create model
    model = Model()

    #Create optimizer and add parameters
    optimizer = torch.optim.Adam(model.parameters(), lr=0.04)

    for _ in range(150):
        #Push x to model
        y = model.forward(model.x)
        #Calculate loss
        loss = (0 - y) ** 2

        # process training step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


    x =  -model.x.detach().numpy()[0]
    print("X is equal to - ",x)