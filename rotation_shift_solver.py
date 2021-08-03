import torch

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()

        # Create model parameters
        self.angle_pred = torch.nn.Parameter(torch.zeros(1), requires_grad=True)
        self.shift_pred = torch.nn.Parameter(torch.zeros((1, 2), requires_grad=True))

        #Create matrix
        self.x     = torch.rand((512,2))

        # Create variables for matrix transformation
        self.angle = torch.tensor(0.8)
        self.shift = torch.tensor([[2,5]])

        # Rotation matrix
        self.rot   = torch.tensor([[torch.cos(self.angle), -torch.sin(self.angle)], [torch.sin(self.angle), torch.cos(self.angle)]])

        #Rotate matrix
        self.x_rot = torch.matmul(self.x, self.rot)

        #Shift matrix
        self.x_shifted_rotated = self.x_rot + self.shift


    def forward(self,angle_pred,shift_pred):
        s = torch.cos(angle_pred[0])
        c = torch.sin(angle_pred[0])

        rot_back = torch.stack([torch.stack([s, -c]),
                            torch.stack([c, s])])


        """
        
        rot_back = torch.zeros((2, 2))
        rot_back[0][0] = torch.cos(angle_pred[0])
        rot_back[0][1] = -torch.sin(angle_pred[0])
        rot_back[1][0] = torch.sin(angle_pred[0])
        rot_back[1][1] = torch.cos(angle_pred[0])
        """


        x_rotated_shifted_pred = torch.matmul(self.x, rot_back)+ shift_pred

        return  x_rotated_shifted_pred



if __name__ == "__main__":
    # Create model
    model = Model()

    #Create optimizer and put parameters in it
    optimizer = torch.optim.Adam(model.parameters(), lr=0.15)

    for _ in range(300):
        # Create prediction - push unknowns to model
        y = model.forward(model.angle_pred,model.shift_pred)

        #Calculate loss
        loss = ((model.x_shifted_rotated - y) ** 2).mean()

        # Zero gradients
        optimizer.zero_grad()
        # Calculate dx
        loss.backward()
        # Update parameters
        optimizer.step()


    shift_pred =  -model.shift_pred.detach().numpy()[0]
    angle_pred =  -model.angle_pred.detach().numpy()[0]


    print("Predicted shift is " ,"X =",-shift_pred[0],"Y =",-shift_pred[1])
    print("Predicted angle is  ",-angle_pred)