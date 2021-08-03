import torch
import numpy


class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        
        #generate random initial parameters
        self.k = torch.nn.Parameter(torch.randn(1), requires_grad=True)
        self.q = torch.nn.Parameter(torch.randn(1), requires_grad=True)
 
    # forward propagate input
    def forward(self, x):
        
        y = self.k*x + self.q
        return y


#some linear target function
def target_function(x):
    return 0.7*x - 1.35


if __name__ == "__main__":

    #create model
    model = MyModel()
    #add parameters to optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

    for step in range(100):

        #generate random input, 256 numbers
        x = torch.randn(256)
        print(x)

        #compute prediction
        y_target        = target_function(x)
        #print(y_target)
        y_prediction    = model.forward(x)
        #print(y_prediction)

        #compute loss
        loss = ((y_target - y_prediction)**2).mean()

        #process training step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        #print trainig results
        loss_np = loss.detach().numpy()
        k_np =  model.k.detach().numpy()[0]
        q_np =  model.q.detach().numpy()[0]

        print(step, loss_np, k_np, q_np)