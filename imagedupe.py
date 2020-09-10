import os
import cv2
from matplotlib import image

def findupes(files):
	n = os.listdir(files)
	for i in range(n):
		temp1 = image.imread(i)
		for j in range(i,n+1):
			temp2 = image.imread(j)
			if(np.array_equal(temp1,temp2)):
				print(i+" "+j)



	


