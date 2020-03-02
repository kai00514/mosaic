import cv2
import sys
import os
import glob


cascade_path = "/home/fujishima0514/fujishima/.local/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)
def usage(arg):
    print(arg[0] + " <inout_dir> <output_dir>")

def mosaic(src, ratio=1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

if __name__ =="__main__":
    arg = sys.argv
   
            
    if len(arg) < 3: 
        usage(arg)
        quit(-1)
    elif len(arg) == 3:
        input_dir = arg[1]
        output_dir = arg[2]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    if os.path.isfile(input_dir) == True:
        usage(arg)
        quit(-2)



    

    glb_path = glob.glob(input_dir + "/*.jpg")

    for fname in glb_path:

        src = cv2.imread(fname)
        dst_01 = mosaic(src)
        gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30)) 
        color = (0,0,255) # blue

        for (x,y,w,h) in facerect:
            img = mosaic(src ,(x,y,x+w,y+h))


        basename = os.path.basename(fname)
        output = os.path.join(output_dir ,basename)
        if len(facerect) > 0:

            for rect in facerect:
                cv2.rectangle(src, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2) 
            cv2.imwrite(output , dst_01)
        print("complete")

