import cv2
import sys
import os
import glob

cascade_path = "/home/fujishima0514/fujishima/.local/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml"

#def usage(arg):
#    print(arg[0] + " <inout_dir> <output_dir>")
#
def mosaic(img,rect,size):  
    # モザイクをかける領域を取得  
    (x1,y1,x2,y2)=rect  
    w=x2-x1  
    h=y2-y1  
    i_rect = img[y1:y2,x1:x2,:]  
    # 一度縮小して拡大する  
    i_small = cv2.resize(i_rect,(size,size))  
    i_mos = cv2.resize(i_small,(w,h),interpolation=cv2.INTER_AREA)  
    # モザイクに画像を重ねる  
    img2=img.copy()  
    img2[y1:y2,x1:x2]=i_mos  
    return img2  
#def mosaic(src, ratio=g):
#    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
#    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def point2mosaic(img, points):
    roi_img = rect
  #  print(roi_img)
    #mosaiced = mosaic(roi_img)
   # return mosaiced

def sample_func(img):
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
   
            
#    if len(arg) < 3: 
#        usage(arg)
#        quit(-1)
#    elif len(arg) == 3:
#        input_dir = arg[1]
#        output_dir = arg[2]
#    if not os.path.exists(output_dir):
#        output_img_dir = os.mkdir(output_dir)
#    else:
#        print("Allready exist ")
#
    
#    if os.path.isfile(input_dir) == True:
#        usage(arg)
#        quit(-2)



    input_dir = sys.argv[1]
    glb_path = glob.glob(input_dir + "*.png")
    for fname in glb_path:

        image = cv2.imread(fname)
        facerect = sample_func(image) 
        #print(image.shape)
		#color = (0, 0, 255)
        basename = os.path.basename(fname)
        #output = os.path.join(output_img_dir ,basename)
        output = os.path.join("./out",basename)
        for (x,y,w,h) in facerect:
            img = mosaic(image,(x,y,x+w,y+h),10)
            print(img)

    if len(facerect) > 0:
        
        for rect in facerect:

            color = (0, 0, 255)
            cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
#            print(rect)
            print("complete")
            print("outputted in " + output)
        cv2.imwrite(output, img)
        
# here yet
#	src = cv2.imread(fname)
#	dst_01 = mosaic(src)
#  
#	basename = os.path.basename(fname)
#	output = os.path.join(output_dir ,basename)
#
#        cv2.imwrite(output , dst_01)

