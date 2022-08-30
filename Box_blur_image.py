# Imageio library simplifies reading images, like removing headers
# imageio returns a numpy array
import imageio.v3 as iio
# PIL allows me to quickly remove alpha values
from PIL import Image
# numpy arrays are in general faster than python lists, good for reading 4k images
import numpy
from math import sqrt

def save(img):
    x = img
    namefnew = input("Enter new name of the file: ")
    while True:
        print("Choose extension to store file as: ")
        print("1.JPG (Alpha data will be lost, smaller file size)")
        print("2.PNG (Alpha data will be retained, larger file size)")
        temp1 = input("Choose 1 or 2 ?: ")
        if temp1 == "1":
            img = Image.fromarray(img).convert("RGB")
            img = numpy.array(img)
            newext = ".jpg"
            break
        elif temp1 == "2":
            newext = ".png"
            break
        print("That is not an option. Please try again.")
    newname = namefnew + newext
    iio.imwrite(newname,img)

def blurimage(img,height,width,type):
    tempimage = img.copy()
    sumR = 0
    sumG = 0
    sumB = 0
    for i in range(0,height):
        for j in range(0,width):
            if i == 0 and j == 0: #Top left Corner
                for k in range(0,4):
                    for l in range(0,4):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]

                img[i][j][0] = round(sumR / 4.00)
                img[i][j][1] = round(sumG / 4.00)
                img[i][j][2] = round(sumB / 4.00)
            elif i == 0 and j > 0 and j < width - 1: # Top edge
                for k in range(0,2):
                    for l in range(j-1,j+2):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
                    
                img[i][j][0] = round(sumR / 6.00)
                img[i][j][1] = round(sumG / 6.00)
                img[i][j][2] = round(sumB / 6.00)
            
            elif j == 0 and i > 0 and i < height - 1: # Left edge
                for k in range(i-1,i+2):
                    for l in range(0,2):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
                    
                img[i][j][0] = round(sumR / 6.00)
                img[i][j][1] = round(sumG / 6.00)
                img[i][j][2] = round(sumB / 6.00)

            elif j == 0 and i == height - 1: # Bottom Left corner
                for k in range(i-1,i+1):
                    for l in range(j,j+2):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
                
                img[i][j][0] = round(sumR / 4.00)
                img[i][j][1] = round(sumG / 4.00)
                img[i][j][2] = round(sumB / 4.00)
            elif i == 0 and j == width - 1: # Top right corner
                for k in range(0,2):
                    for l in range(j-1,j+1):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
                    
                img[i][j][0] = round(sumR / 4.00)
                img[i][j][1] = round(sumG / 4.00)
                img[i][j][2] = round(sumB / 4.00)
            
            elif i == height - 1 and j == width - 1: # Bottom right Corner
                for k in range(i-1,i+1):
                    for l in range(j-1,j+1):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
                    
                img[i][j][0] = round(sumR / 4.0)
                img[i][j][1] = round(sumG / 4.0)
                img[i][j][2] = round(sumB / 4.0)
            
            elif i == height - 1 and j > 0 and j < width - 1: # Bottom edge
                for k in range(i-1,i+1):
                    for l in range(j-1,j+2):
                    
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]

                img[i][j][0] = round(sumR / 6.00)
                img[i][j][1] = round(sumG / 6.00)
                img[i][j][2] = round(sumB / 6.00)
            
            elif j == width - 1 and i > 0 and i < height - 1: # Right edge
                for k in range(i-1,i+2):
                    for l in range(j-1,j+1):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
            
                img[i][j][0] = round(sumR / 6.00)
                img[i][j][1] = round(sumG / 6.00)
                img[i][j][2] = round(sumB / 6.00)
            
            else:
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        sumR = sumR + tempimage[k][l][0]
                        sumG = sumG + tempimage[k][l][1]
                        sumB = sumB + tempimage[k][l][2]
                    
                img[i][j][0] = round(sumR / 9.00)
                img[i][j][1] = round(sumG / 9.00)
                img[i][j][2] = round(sumB / 9.00)
            
            sumR = 0
            sumG = 0
            sumB = 0

nameold = str(input("Enter name of the file with the file extension: "))
temp1 = iio.imread(nameold)
img = temp1.copy()
height = img.shape[0]
width = img.shape[1]
type = img.shape[2]
print()
blurimage(img,height,width,type)
save(img)