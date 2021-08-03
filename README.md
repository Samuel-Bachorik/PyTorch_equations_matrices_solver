# PyTorch_equations_matrices_solver
Matrix rotation and shift, quadratic, linear equations, System of linear equations<br/>

`rotation_shift_solver.py` can find shift and rotation of matrix<br/>
Example - <br/>
Lets think matrix x<br/>

![Matrix x](https://github.com/Samuel-Bachorik/PyTorch_equations_matrices_solver/blob/master/Images/Matrix%20x.PNG)<br/>

Transform by shift and rotation matrix - <br/>
Rotation matrix R =<br/>
![Matrix xR](https://github.com/Samuel-Bachorik/PyTorch_equations_matrices_solver/blob/master/Images/Rotation%20matrix.PNG)<br/>
θ = 0.8 = 45.8366 degrees (random angle)<br/>
Shift matrix S (random numbers) =<br/>
![Matrix S](https://github.com/Samuel-Bachorik/PyTorch_equations_matrices_solver/blob/master/Images/shift%20matrix.PNG)<br/>
Transofrm matrix x with shift and rotation matrix =<br/>
x_rotated_shifted = torch.matmul(x, R)+ S<br/>

Now we get our rotated and shifted matrix<br/>
![Matrix rotated_shifted](https://github.com/Samuel-Bachorik/PyTorch_equations_matrices_solver/blob/master/Images/Matrix%20rotated%20shifted.PNG)<br/>

Now we have two inputs - Matrix x and matrix x_rotated_shifted<br/>
`rotation_shift_solver.py` will find back Shift and angle theta. 


`Quadratic_equation.py` solves quadratic equations in matrix form of Ax-b = 0<br/>


