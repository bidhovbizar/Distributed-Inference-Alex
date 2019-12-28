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
X = np.zeros(13 * 300).reshape(300,13);
for i in range(5) :
    {
        print(i)
        X[i] = np.ones(13);
    }
RV_X = np.random.exponential(1/3) 

for i in range(5) :
    {
        print(X[i])
        #print(np.ones(13))
    }