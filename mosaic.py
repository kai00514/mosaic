import cv2
import sys
import os
import glob
import numpy


cascade_path = "/home/fujishima0514/fujishima/.local/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml"

#def usage(arg):


def topical_mosaic(img,rect,size):  

    # topical 関数を呼ぶ
    # i_rect を返す
    tpcl = topical(rect,img)
     
    tpcl_mos = mosaic(tpcl)
    #tpcl_mos = mosaic(tpcl,size)
    

    (x1,y1,x2,y2)=rect  
    img2=img.copy()   # normal image
    img2[y1:y2,x1:x2]=tpcl_mos  # only mosaic

    # insert new func here?
    return img2  

def mosaic(src, ratio=.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def topical(rect,img):
    (x1,y1,x2,y2)=rect  
    i_rect = img[y1:y2,x1:x2,:]  
    print(i_rect)
    return i_rect

def image2gray(image):
     
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray
    

    
#　人の顔を検出する関数
def image2cascade(img):

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(
	image_gray,
	scaleFactor=1.1,
	minNeighbors=2,
	minSize=(30, 30))
    return facerect 

if __name__ =="__main__":
    arg = sys.argv
   
            
    if len(arg) < 3: 
        usage(arg)
        quit(-1)
    elif len(arg) == 3:
        input_dir = arg[1]
        output_dir = arg[2]
    if not os.path.exists(output_dir):
        output_img_dir = os.mkdir(output_dir)
    else:
        print("Allready exist ")

    
    if os.path.isfile(input_dir) == True:
        usage(arg)
        quit(-2)



    input_dir = sys.argv[1]
    glb_path = glob.glob(input_dir + "*.png")
    for fname in glb_path:

        image = cv2.imread(fname)
        facerect = image2cascade(image) 
        #print(image.shape)
		#color = (0, 0, 255)
        basename = os.path.basename(fname)
        #output = os.path.join(output_img_dir ,basename)
        output = os.path.join("./out",basename)
        output2 = os.path.join("./output",basename)
        output3 = os.path.join("./gray_out",basename)

        #for (x,y,w,h) in facerect:
        #    img = topical_mosaic(image,(x,y,x+w,y+h),10)
        #    cv2.imwrite(output3,img)
        
    if len(facerect) > 0:
        
        for rect in facerect:

            #img_gray = img.copy()
           #gray_mosaic = image2gray(gray)
            tpcl_image = topical(rect,image)
            gray_image = image2gray(tpcl_image)
            mosaic_gray = mosaic(gray_image)

            (x1,y1,x2,y2)=rect  
            img2=image.copy()   # normal image
            img2[y1:y2,x1:x2,0]=mosaic_gray # only mosai
            img2[y1:y2,x1:x2,1]=mosaic_gray # only mosai
            img2[y1:y2,x1:x2,2]=mosaic_gray # only mosai
            
            color = (0, 0, 255)

            #cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
           # cv2.rectangle(gray_mosaic, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
            print("complete")
            print("outputted in " + output)
            print("outputted in " + output3)
      #  cv2.imwrite(output, img)
        #cv2.imwrite(output3,gray_mosaic)
            pv2.imwrite(output3,img2)
        
        
        
# here yet
#	src = cv2.imread(fname)
#	dst_01 = mosaic(src)
#  
#	basename = os.path.basename(fname)
#	output = os.path.join(output_dir ,basename)
#
#        cv2.imwrite(output , dst_01)

