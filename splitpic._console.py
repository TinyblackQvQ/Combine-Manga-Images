from PIL import Image
import os
import glob
import msvcrt

#classes
class image:
    filename = ""
    image = ""
    def __init__(self,filename):
        self.filename = filename
        self.image = Image.open(filename)

#vari
mode = 1
imagelist = []

#functions

#main while
while True:
    if mode == 1:
        print("Please wait...")
        for filename in glob.glob(os.path.abspath('.')+r"\*.*"):
            if filename.endswith("jpg" or "png" or "jpeg"):
                imagelist.append(image(filename))
        print(str(len(imagelist))+" files founded")
        os.system("cls")
        mode = 2

    if mode == 2:
        show = 0
        select = 0
        while True:
            print("Please select image you want to process:")
            i = show
            if len(imagelist) < 5:
                max = len(imagelist)
            else:
                if show + 5 <= len(imagelist):
                    max = show + 5
                else:
                    max = len(imagelist)
                    i = max - 5
            while i < max:
                print(imagelist[i].filename,end="")
                if select == i:
                    print(" <--Selected")
                else:
                    print("\n",end="")
                i += 1
            tinput = msvcrt.getch()
            if tinput == b'H':
                show -= 1
                select -= 1
            if tinput == b'P':
                show += 1
                select += 1
            if tinput == b'\r':
                mode = 3
                break
            if show + 4 > len(imagelist):
                show = len(imagelist) - 4
            if show < 0:
                show = 0
            if select < 0:
                select = 0
            if select >= len(imagelist):
                select = len(imagelist) - 1
            os.system("cls")

    if mode == 3:
        selectmode = 0
        while True:
            os.system("cls")
            print("Please choose the devide mode:")

            print("left to right",end='')

            if selectmode == 0:
                print(" <--Selected")
            else:
                print("\n",end='')
            
            print("up to down",end='')

            if selectmode == 1:
                print(" <--Selected")
            else:
                print("\n",end='')
            
            tinput = msvcrt.getch()
            if tinput == b'H':
                selectmode = 0
            if tinput == b'P':
                selectmode = 1
            if tinput == b'\r':
                mode = 4
                break
    
    if mode == 4:
        print("Please enter the number you want to divide the picture into")
        a = input()
        try:
            a = int(a)
        except ValueError:
            print("NaN,Please retry!")
            continue
        mode = 5
    
    if mode == 5:
        print("Please enter the beginning number")
        name = input()
        try:
            name = int(name)
        except ValueError:
            print("NaN,Please retry!")
            continue
        mode = 6

    if mode == 6:
        print("Please wait...")
        i = 1
        process = 0
        if selectmode == 0: #left to right
            canvassize = [imagelist[select].image.size[0]/a,imagelist[select].image.size[1]]
        else:
            canvassize = [imagelist[select].image.size[0],imagelist[select].image.size[1]/a]
        if selectmode == 0:
            while i <= a:
                print("width:"+str(process)+","+str(process+canvassize[0]))
                canvas = imagelist[select].image.crop((process,0,process+canvassize[0],canvassize[1]))
                process += canvassize[0]
                canvas.save(str(i+name-1)+".jpg",quality = 100)
                i += 1
        else:
            while i <= a:
                print("height:"+str(process)+","+str(process+canvassize[1]))
                canvas = imagelist[select].image.crop((0,process,canvassize[0],process+canvassize[1]))
                process += canvassize[1]
                canvas.save(str(i+name-1)+".jpg",quality = 100)
                i += 1
        imagelist = []
        mode = 1