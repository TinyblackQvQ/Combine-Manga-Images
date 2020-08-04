# _*_coding:utf-8_*_
#Made by Tinyblack/攸望汉化组/Youwang Translating Group
#Made with Pygame and PIL
#Version alpha 1.01
#Update:Fixed program crash when click the blank area in selecting images
#Completed in 2020.8.4 / UTC+8 15:15:00
#Updated in 2020.8.4 / UTC+8 23:13:00
import pygame
import os
import glob
import time
from PIL import Image

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Combination")
mode = 1
#mode 1 启动时进行
#mode 2 选择文件
#mode 3 处理文件

filelist = []
imagelist = []
#filelist 储存文件列表

font_title = pygame.font.SysFont("FZLTXHJW.TTF",40)
font_small = pygame.font.SysFont("FZLTXHJW.TTF",20)

def copyimage(image,canvas,x,y):
    i , j = 0 , 0
    print(str(x) + "," + str(y))
    while i < image.size[0]:
        while j < image.size[1]:
            canvas.putpixel((x+i,y+j), image.getpixel((i,j)))
            j += 1
        i += 1
        j = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

def updatescreen(screen,nowimage,allimage):
    screen.fill((255,255,255),(0,0,1280,720))
    t = font_title.render("We are processing the picture...("+str(nowimage)+"/"+str(allimage)+")",True,(0,0,0))
    screen.blit(t,(int(640-t.get_width()/2),int(360-t.get_height()/2)))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
try:
    open(u".\images\selected.png","r")
except IOError:
    t = font_title.render(u"Could find file [selected.png],please check or redownload program.",True,(255,255,255))
    screen.blit(t,(int(640-t.get_width()/2),int(360-t.get_height()/2)))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
selectimage = pygame.image.load(".\images\selected.png")

try:
    open(u".\images\icon.png","r")
except IOError:
    t = font_title.render(u"Could find file [icon.png],please check or redownload program.",True,(255,255,255))
    screen.blit(t,(int(640-t.get_width()/2),int(360-t.get_height()/2)))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
pygame.display.set_icon(pygame.image.load(".\images\icon.png"))

class Fileimage:
    image = 0
    filename = ""
    listpic = 0
    pygameimage = 0
    pygamesmallimg = 0
    filenamesurface = 0
    font = pygame.font.SysFont("FZLTXHJW.TTF",25)
    selected = False
    def __init__(self,filename):
        self.filename = filename
        self.image = Image.open(filename)
        self.pygameimage = pygame.image.load(self.filename)
        tlistpic = pygame.image.load(self.filename)
        tlistpic = pygame.transform.scale(tlistpic,(1280,100))
        self.pygamesmallimg = pygame.transform.rotozoom(self.pygameimage,0,100/self.pygameimage.get_width())
        tlistpic.fill((255,255,255),(0,0,10000,10000))
        tlistpic.blit(self.pygamesmallimg,(int(150-self.pygamesmallimg.get_width()/2),0))
        tfilenamesurface = self.font.render(filename,True,(0,0,0))
        self.filenamesurface = tfilenamesurface
        tlistpic.blit(self.filenamesurface,(320,20))
        tlistpic.fill((0,0,0),(0,99,1280,100))
        tlistpic.fill((0,0,0),(300,0,1,100))
        self.listpic = tlistpic
    def update(self):
        tlistpic = self.listpic
        tlistpic.fill((255,255,255),(0,0,10000,10000))
        tlistpic.blit(self.pygamesmallimg,(int(150-self.pygamesmallimg.get_width()/2),0))
        tlistpic.blit(self.filenamesurface,(320,20))
        tlistpic.fill((0,0,0),(0,99,1280,100))
        tlistpic.fill((0,0,0),(300,0,1,100))
        if self.selected == True:
            tlistpic.blit(selectimage,(1100,40))
            tlistpic.blit(self.font.render("Selected",True,(0,0,0)),(1150,40))
        self.listpic = tlistpic

height = 40

while True:
    if mode == 1:
        i = 0
        text_title = font_title.render(u"We are searching for picture file under root...",True,(0,0,0))

        text_small = font_small.render(str(i)+u" Pictures founded",True,(100,100,100))
        screen.fill((255,255,255),(0,0,1280,720))
        screen.blit(text_title,(int(640-text_title.get_width()/2),int(360-text_title.get_height()/2)))
        screen.blit(text_small,(int(640-text_small.get_width()/2),int(370+text_title.get_height()/2)))
        pygame.display.update()
        time.sleep(0.8)

        for filename in glob.glob(os.path.abspath('.')+u"\*.*"):
            print(filename)
            if filename.endswith("jpg" or "png" or "jpeg"):
                filelist.append(filename)
                imagelist.append(Fileimage(filename))
                i = i + 1
                text_small = font_small.render(str(i)+u" Pictures founded ["+ filename + "]",True,(100,100,100))
                screen.fill((255,255,255),(0,0,1280,720))
                screen.blit(text_title,(int(640-text_title.get_width()/2),int(360-text_title.get_height()/2)))
                screen.blit(text_small,(int(640-text_small.get_width()/2),int(370+text_title.get_height()/2)))
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        screen.fill((255,255,255),(0,0,1280,720))
        text_title = font_title.render(str(i)+u" Pictures founded",True,(0,0,0))
        screen.blit(text_title,(int(640-text_title.get_width()/2),int(360-text_title.get_height()/2)))
        pygame.display.update()
        time.sleep(0.5)
        j = 0
        while j <= 255:
            screen.fill((255,255,255),(0,0,1280,720))
            text_title = font_title.render(str(i)+u" Pictures founded",True,(j,j,j))
            screen.blit(text_title,(int(640-text_title.get_width()/2),int(360-text_title.get_height()/2)))
            pygame.display.update()
            j = j + 1
        mode = 2
    if mode == 2:
        nowheight = height
        screen.fill((255,255,255),(0,0,1280,720))
        selectedimg = 0
        for image in imagelist:
            image.update()
            screen.blit(image.listpic,(0,nowheight))
            nowheight = nowheight + 100
            if image.selected == True:
                selectedimg = selectedimg + 1
        screen.fill((255,255,255),(0,0,1280,50))
        screen.fill((0,0,0),(0,49,1280,1))
        screen.blit(font_title.render("Selected Files: "+str(selectedimg),True,(0,0,0)),(10,10))
        screen.fill((0,0,0),(1180,0,1,50))
        screen.blit(image.font.render("Finish",True,(0,0,0)),(1205,16))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    if height < 40:
                        height = height + 40
                elif event.button == 5:
                    if height > -100 * len(filelist) + 720:
                        height = height - 40
                elif event.button == 1:
                    i = pygame.mouse.get_pos()
                    if i[0] >= 1180 and i[1] <= 50:
                        mode = 3
                    elif i[1] <= 50:
                        continue
                    elif i[1] >= len(imagelist)*100 + height:
                        continue
                    elif imagelist[int((i[1]-height)/100)].selected == True:
                        imagelist[int((i[1]-height)/100)].selected = False
                    else:
                        imagelist[int((i[1]-height)/100)].selected = True
    if mode == 3:

		#Check Image Height and Width
        tlist = []	#Save the size of each image
        heightdiff = False #If all selected pictures' height are same
        widthdiff = False #If all selected pictures' width are same
        maxsize = [0,0] #Save the max size during all selected pictures
        allpixel = {'width':[0,0],'height':[0,0]} #Save the image's size if it is blited
        for image in imagelist:
            if image.selected == True:
                allpixel['width'][0] += image.image.size[0]
                allpixel['height'][1] += image.image.size[1]
                if image.image.size[0] >= maxsize[0]:
                    maxsize[0] = image.image.size[0]
                if image.image.size[1] >= maxsize[1]:
                    maxsize[1] = image.image.size[1]
                for size in tlist:
                    if image.image.size[0] != size[0]:
                        widthdiff = True
                    if image.image.size[1] != size[0]:
                        heightdiff = True
                print(image.image.size)
        allpixel['width'][1] = maxsize[1]
        allpixel['height'][0] = maxsize[0]
        print(allpixel)
        #Warning
        #if widthdiff == True or heightdiff == True:
        #    font_title.

        #Choose combine mode
        addmode = 0
        choosed = False
        while True:
            ttext = font_title.render("Please choose combine mode",True,(0,0,0))
            tadd = font_title.render("+",True,(0,0,0))
            screen.fill((255,255,255),(0,0,1280,720))
            screen.fill((100,100,100),(640,100,1,620))
            timg = pygame.transform.scale(screen,(90,160))
            timg.fill((0,0,0),(0,0,90,160))
            timg.fill((255,255,255),(2,2,86,156))
            screen.blit(ttext,(int(640-ttext.get_width()/2),50))
            screen.blit(timg,(200,280))
            screen.blit(timg,(400,280))
            screen.blit(tadd,(335,345))
            screen.blit(timg,(900,180))
            screen.blit(timg,(900,450))
            screen.blit(tadd,(940,380))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.mouse.get_pos()[0] <= 640:
                            addmode = 0
                        if pygame.mouse.get_pos()[0] > 640:
                            addmode = 1
                    choosed = True
            if choosed == True:
                break
        print("addmode:" + str(addmode))
        #Process the Images
        height = 0 #Save the Processed pixel height
        if addmode == 0:
            canvas = Image.new("RGB",allpixel['width'],color=(255,255,255))
        else:
            canvas = Image.new("RGB",allpixel['height'],color=(255,255,255))
        print(canvas.size)

        i = 0
        if addmode == 0:
            for image in imagelist:
                if image.selected == True:
                    i += 1
                    updatescreen(screen,i,selectedimg)
                    copyimage(image.image, canvas, height, 0)
                    height += image.image.size[0]
        else:
            for image in imagelist:
                if image.selected == True:
                    i += 1
                    updatescreen(screen,i,selectedimg)
                    copyimage(image.image, canvas , 0, height)
                    height += image.image.size[1]
        canvas.save("after.jpg",quality=100)
        ttext = font_title.render("Completed!",True,(0,0,0))
        i = 255
        while i >= 0:
            screen.fill((i,i,i),(0,0,1280,720))
            screen.blit(ttext,(int(640-ttext.get_width()/2),int(360-ttext.get_height()/2)))
            pygame.display.update()
            time.sleep(0.005)
            i -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        exit()