import numpy as np
import sys
import scipy.io as sio
import scipy.io.wavfile
from scipy.io.wavfile import write

#function from https://people.sc.fsu.edu/~jburkardt/py_src/haar/haar.html to calculate Haar transform
def haar_1d ( n, x ):
    
#*****************************************************************************80
#
## HAAR_1D computes the Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int N, the dimension of the vector.
#
#    Input, double X[N], the vector to be transformed.
#
#    Output, double U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n, dtype = np.float64 )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
  
  while ( 1 < k ):

    k = k // 2

    v[0:k]   = ( u[0:2*k-1:2] + u[1:2*k:2] ) / s
    v[k:2*k] = ( u[0:2*k-1:2] - u[1:2*k:2] ) / s

    u[0:2*k] = v[0:2*k].copy ( )

  return u


#print full numpy array
np.set_printoptions(threshold=sys.maxsize)



#get input
print("Please put desired wav file")
print("Please enter file name:")
fileName = input()
print("Program running on file:", fileName )

#get numpy of wav file
rate, data = scipy.io.wavfile.read(fileName)

print("NUMPY ARRAY: ")
print(data)

#find dimensions then get Haar transform

entries = data.shape[0]
#columns = data.shape[1]

print("Matrix Dimensions")
print(entries)

HaarTransform = haar_1d ( entries, data )

print("Haar Transform is: ")
print(HaarTransform)

#create new wav file
#get input
print("Please put desired new wav file name")
print("Please enter file name:")
fileNametoCreate = input()
print("Program creating", fileNametoCreate )
#convert numpy HaarTransform to wav file
write(fileNametoCreate, rate, HaarTransform)
print(fileNametoCreate, " completed.  Please enjoy!")

