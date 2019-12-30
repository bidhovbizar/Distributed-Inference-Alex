import numpy as np;
# describing Path matrix for flows described in " A Stochastic Kaczmarz Algorithm for Network Tomography"
A = np.zeros(13 * 6).reshape(6,13);
# column 1
A[0,0]=1;
A[1,0]=1;
A[2,0]=1;
# column 2
A[0,1]=1;
# column 3
A[0,2]=1;
A[3,2]=1;
# column 4
A[1,3]=1;
A[2,3]=1;
# column 5
A[3,4]=1;
# column 6
A[3,5]=1;
A[4,5]=1;
A[5,5]=1;
# column 7
A[4,6]=1;
# column 8
A[1,7]=1;
A[2,7]=1;
A[4,7]=1;
# column 9
A[1,8]=1;
A[4,8]=1;
# column 10
A[3,9]=1;
A[5,9]=1;
# column 11
A[5,10]=1;
# column 12
A[2,11]=1;
# column 13
A[2,12]=1;
A[5,12]=1;


# defining random variables for Y=AX+W 

#let X(j) be a random variable that defines the delay faced by packet parsing through 'j'th path
# creating X
noOfObservation = 300
X = np.zeros(13 * noOfObservation).reshape(13,noOfObservation);
# creating array of X using exponential random variable
for i in range(X.shape[1]) :
    X[:,i] = [ np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3),np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3), np.random.exponential(1/3)]  

#calculating Y  from X using equation Y = AX
Y = np.matmul(A,X)      

#Finding expectation of Y as ExpY
ExpY = np.mean(Y,axis=1)

#Setting the initial value of X0 for deterministic Kaczmarz
X0 = np.zeros(13) 

#Finding the X_star for Determinitstic Kaczmarz
X_star = X0 + np.matmul(np.matmul(A.T,np.linalg.inv(np.matmul(A,A.T))),(ExpY - np.matmul(A,X0)))

#Defining other variables for stochastic Kaczmarz
elements = range(6) # Range of RV
prob = [ i.sum() for i in A ] / A.sum() # probability of chosing a path w.r.t the euclidean norm of rows in A

# Number of iterations we expect required to converge to a solution
noOfIteration = 500
# Setting the Random VAriable Z to calculate \sY(Z_k)
Z = np.random.choice(elements,noOfIteration,p = prob)

# step size Yeta = (1/k)

for k in range(noOfIteration):
    print(k)
    Y_kplus1 = np.dot(A[Z[k+1]],X[k % noOfObservation]
