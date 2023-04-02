import pygame
import time
import sys
import os
import selectfile
pygame.init()

win=pygame.display.set_mode((600,600))

pygame.display.set_caption("PyPaint")

sys.setrecursionlimit(10000000)


def checksize():
    
    if SIZE==2:
        pygame.draw.circle(win,(0,255,0),(520,100),2)
        pygame.draw.circle(win,(255,255,255),(540,100),4)
        pygame.draw.circle(win,(255,255,255),(560,100),6)
        pygame.draw.circle(win,(255,255,255),(580,100),8)

    elif SIZE==4:
        pygame.draw.circle(win,(255,255,255),(520,100),2)
        pygame.draw.circle(win,(0,255,0),(540,100),4)
        pygame.draw.circle(win,(255,255,255),(560,100),6)
        pygame.draw.circle(win,(255,255,255),(580,100),8)
            
    elif SIZE==6:
        pygame.draw.circle(win,(255,255,255),(520,100),2)
        pygame.draw.circle(win,(255,255,255),(540,100),4)
        pygame.draw.circle(win,(0,255,0),(560,100),6)
        pygame.draw.circle(win,(255,255,255),(580,100),8)

    elif SIZE==8:
        pygame.draw.circle(win,(255,255,255),(520,100),2)
        pygame.draw.circle(win,(255,255,255),(540,100),4)
        pygame.draw.circle(win,(255,255,255),(560,100),6)
        pygame.draw.circle(win,(0,255,0),(580,100),8)
    pygame.display.update()    
def size(ms,mx,my):
    global SIZE
    if ms==(1,0,0) and mx>510 and mx<530 and my<120 and my>80:
        SIZE=2
    if ms==(1,0,0) and mx>530 and mx<550 and my<120 and my>80:
        SIZE=4
    if ms==(1,0,0) and mx>550 and mx<570 and my<120 and my>80:
        SIZE=6
    if ms==(1,0,0) and mx>570 and mx<590 and my<120 and my>80:
        SIZE=8
        
    checksize()
    
    pygame.display.update()    
    
def copycolor():
    
    subwin=win.subsurface((0,0,500,500))
    pygame.image.save(subwin,"tempsurface.png")
    TS=pygame.image.load("tempsurface.png")
    flg=0
    print("colorcopy")
    flag=True
    while flag:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    os.remove("tempsurface.png")
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
                except:
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:
                    print("released")
                    Ccolor=win.get_at((x1,y1))
                    pygame.draw.rect(win,(0,0,0),(0,0,500,500))
                    win.blit(TS,(0,0))
                    pygame.display.update()
                    return Ccolor
                    

        ms=pygame.mouse.get_pressed()
        mx,my=pygame.mouse.get_pos()
        if ms==(1,0,0) and mx<500 and my<500:
            copycolor=win.get_at((mx,my))
            pygame.draw.rect(win,(0,0,0),(0,0,500,500))
            win.blit(TS,(0,0))
            pygame.draw.rect(win,copycolor,(mx,my-25,20,20))
            pygame.draw.rect(win,(255,255,255),(mx,my-25,20,20),1)
            pygame.display.update()
        if ms==(1,0,0) and ((mx>5 and mx<195) or (mx>235 and mx<475)) and my>540 and my<570:
            flag=False
        if my>575 and ms==(1,0,0):
            flag=False
            
def drawline(color):
    time.sleep(0.2)
    checksize()
    subwin=win.subsurface((0,0,500,500))
    pygame.image.save(subwin,"tempsurface.png")
    TS=pygame.image.load("tempsurface.png")
    flg=0
    slp=0.2
    print("linedrawing")
    l,m,n=color
    flag=True
    while flag:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    os.remove("tempsurface.png")
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
                except:
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:
                    framewin=win.subsurface((0,0,500,500))
                    pygame.image.save(framewin,"tempsurface2.png")
                    frames.append(pygame.image.load("tempsurface2.png"))
            
            if event.type == pygame.MOUSEBUTTONUP:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:


                    print("released")
                    drawline(color)
                    slp=0
                
        ms=pygame.mouse.get_pressed()
        mx,my=pygame.mouse.get_pos()
        if mx>500 and my<500 and ms==(1,0,0):
            size(ms,mx,my)
        if ms==(1,0,0) and mx>165 and mx<185 and my>540 and my<570:
            time.sleep(slp)
            flag=False
            break
            
        if flg!=1:
            nx,ny=pygame.mouse.get_pos()
        if ms==(1,0,0) and mx<500 and my<500:
            flg=1
            x,y=nx,ny
            p,q=pygame.mouse.get_pos()
            if p<500 and q<500:
                pygame.draw.rect(win,(0,0,0),(0,0,500,500))
                win.blit(TS,(0,0))
                pygame.draw.line(win,(l,m,n),(x,y),(p,q),SIZE)
                pygame.display.update()

        if ms==(1,0,0) and ((mx>5 and mx<165) or (mx>185 and mx<475)) and my>540 and my<570:
            flag=False
        if my>575 and ms==(1,0,0):
            flag=False    
def drawsquare(color):
    time.sleep(0.2)
    checksize()
    subwin=win.subsurface((0,0,500,500))
    pygame.image.save(subwin,"tempsurface.png")
    TS=pygame.image.load("tempsurface.png")
    flg=0
    slp=0.2
    print("squaredrawing")
    l,m,n=color
    flag=True
    while flag:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    os.remove("tempsurface.png")
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
                except:
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:
                    framewin=win.subsurface((0,0,500,500))
                    pygame.image.save(framewin,"tempsurface2.png")
                    frames.append(pygame.image.load("tempsurface2.png"))

            if event.type == pygame.MOUSEBUTTONUP:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:

                    print("released")
                    drawsquare(color)
                    slp=0
                
        ms=pygame.mouse.get_pressed()
        mx,my=pygame.mouse.get_pos()
        if mx>500 and my<500 and ms==(1,0,0):
            size(ms,mx,my)
        if ms==(1,0,0) and mx>85 and mx<115 and my>540 and my<570:
            time.sleep(slp)
            flag=False
            break
            
        if flg!=1:
            nx,ny=pygame.mouse.get_pos()
        if ms==(1,0,0) and mx<500 and my<500:
            flg=1
            x,y=nx,ny
            p,q=pygame.mouse.get_pos()
            if p<500 and q<500:
                width=p-x
                height=q-y
                pygame.draw.rect(win,(0,0,0),(0,0,500,500))
                win.blit(TS,(0,0))
                pygame.draw.rect(win,(l,m,n),(x,y,width,height),SIZE)
                tempwidth=width
                tempheight=height
                pygame.display.update()
                
        if ms==(1,0,0) and mx>5 and mx<75 and my>540 and my<570:
            flag=False
        if ms==(1,0,0) and mx>125 and mx<475 and my>540 and my<570:
            flag=False
        if my>575 and ms==(1,0,0):
            flag=False
    
def drawcircle(color):
    time.sleep(0.2)
    checksize()
    subwin=win.subsurface((0,0,500,500))
    pygame.image.save(subwin,"tempsurface.png")
    TS=pygame.image.load("tempsurface.png")
    flg=0
    slp=0.2
    print("circledrawing")
    l,m,n=color
    flag=True
    while flag:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    os.remove("tempsurface.png")
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
                except:
                    try:
                        os.remove("tempsurface2.png")
                        pygame.quit()
                    except:
                        pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:
                    framewin=win.subsurface((0,0,500,500))
                    pygame.image.save(framewin,"tempsurface2.png")
                    frames.append(pygame.image.load("tempsurface2.png"))

            if event.type == pygame.MOUSEBUTTONUP:
                x1,y1=pygame.mouse.get_pos()
                if x1<500 and y1<500:
                    print("released")
                    drawcircle(color)
                    slp=0
        ms=pygame.mouse.get_pressed()
        mx,my=pygame.mouse.get_pos()
        if mx>500 and my<500 and ms==(1,0,0):
            size(ms,mx,my)
        if ms==(1,0,0) and mx>45 and mx<75 and my>540 and my<570:
            time.sleep(slp)
            flag=False
            break
        if flg!=1:
            nx,ny=pygame.mouse.get_pos()
        if ms==(1,0,0) and mx<500 and my<500:
            flg=1
            x,y=nx,ny
            p,q=pygame.mouse.get_pos()
            if p<500 and q<500:
                radius=p-x
                if radius<=SIZE:
                    radius=SIZE+1
                pygame.draw.rect(win,(0,0,0),(0,0,500,500))
                win.blit(TS,(0,0))    
                pygame.draw.circle(win,(l,m,n),(x,y),radius,SIZE)
                pygame.display.update()
                    
        if ms==(1, 0, 0) and 5 < mx < 35 and 540 < my < 570:
            flag=False
        if ms==(1,0,0) and mx>85 and mx<475 and my>540 and my<570:
            flag=False
        if my>575 and ms==(1,0,0):
            flag=False
            
def fill(x,y,color,basecolor):
    p,q,r=color
    colour=win.get_at((x,y))
    
    if colour==basecolor and x<500 and y<500 and x>0 and y>0:
        pygame.draw.rect(win,(p,q,r),(x,y,1,1))

        
        fill(x+1,y,color,basecolor)#12ryt
        
        fill(x-1,y,color,basecolor)#10left
        
        fill(x,y-1,color,basecolor)#01up

        fill(x,y+1,color,basecolor)#down
        
        fill(x+1,y+1,color,basecolor)#22downryt
        
        fill(x-1,y-1,color,basecolor)#00upleft

        fill(x+1,y-1,color,basecolor)#02upryt

        fill(x-1,y+1,color,basecolor)#02downleft        


def save(text):
    saveimg=win.subsurface((0,0,499,499))
    pygame.image.save(saveimg,text)
    
def Open():   
    pic=selectfile.Filepath()
    temppic=pygame.image.load(pic)
    pic2=pygame.transform.scale(temppic,(500,500))
    win.blit(pic2,(0,0))
    pygame.display.update()
def Text(st,x,y):
    font = pygame.font.Font('SEASRN__.ttf', 18) 
      
    text = font.render(st, True, (255,255,255), (0,0,0)) 
      
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
      
    # set the center of the rectangular object. 
    textRect.center = (x,y)
    win.blit(text,textRect)
    pygame.display.update()
    
    
eraser=pygame.image.load("eraser2.jpg")
eraser=pygame.transform.scale(eraser,(30,30))
colorpicker=pygame.image.load("colorpicker.jpg")
colorpicker=pygame.transform.scale(colorpicker,(30,30))

count=0
color=[250,0,0]
x,y,z=color
mx=0
my=0
mx2=0
my2=0
imgnum=0
global frames
global SIZE
SIZE=2
frames=[]
run=True
while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                os.remove("tempsurface.png")
                try:
                    os.remove("tempsurface2.png")
                    run=False
                except:
                    run=False
               
                run=False
            except:
                try:
                    os.remove("tempsurface2.png")
                    run=False
                except:
                    run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1,y1=pygame.mouse.get_pos()
            if x1<500 and y1<500:
                framewin=win.subsurface((0,0,500,500))
                pygame.image.save(framewin,"tempsurface2.png")
                frames.append(pygame.image.load("tempsurface2.png"))

        
    checksize()    
    ms=pygame.mouse.get_pressed()
    
    mx,my=pygame.mouse.get_pos()

    
    keys=pygame.key.get_pressed()
    if ((keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_s]) or (ms==(1,0,0) and mx>320 and mx<380 and my>540 and my<570):
        save("img"+str(imgnum)+".png")
        imgnum+=1
        time.sleep(0.2)
        

    if my>575 and ms==(1,0,0):
        mx2,my2=mx,my

        
              
        if mx2<100 and mx2>0:
            color[0]=250
            color[2]=0
            color[1]=round(mx2*2.5)
        elif mx2<200 and mx2>=100:
            x2=mx2%100
            color[1]=250
            color[2]=0
            color[0]=250-round(x2*2.5)
        elif mx2<300 and mx2>=200:
            x2=mx2%100
            color[0]=0
            color[1]=250
            color[2]=round(x2*2.5)
        elif mx2<400 and mx2>=300:
            x2=mx2%100
            color[0]=0
            color[2]=250
            color[1]=250-round(x2*2.5)
        elif mx2<500 and mx2>=400:
            x2=mx2%100
            color[1]=0
            color[2]=250
            color[0]=round(x2*2.5)
        elif mx2<=595 and mx2>=500:
            x2=mx2%100
            color[1]=0
            color[0]=250
            color[2]=250-round(x2*2.5)
        elif mx2>595:
            color[0]=255
            color[1]=255
            color[2]=255
        pygame.draw.circle(win,(color[0],0,0),(500,555),15,3)
        pygame.draw.circle(win,(0,color[1],0),(540,555),15,3)
        pygame.draw.circle(win,(0,0,color[2]),(580,555),15,3)
        pygame.display.update()
    if ms==(0,0,0):
        pygame.draw.rect(win,(0,0,0),(470,500,130,75))
        pygame.display.update()
    if ms==(1,0,0) and mx>5 and mx<35 and my>540 and my<570:
        mx2=0
        my2=0
        color=[0,0,0]
    if ms==(1,0,0) and mx>45 and mx<75 and my>540 and my<570:
        pygame.draw.circle(win,(0,255,0),(60,555),15,2)
        pygame.display.update()
        drawcircle(color)
    if ms==(1,0,0) and mx>85 and mx<115 and my>540 and my<570:
        pygame.draw.rect(win,(0,255,0),(85,540,30,30),2)
        pygame.display.update()
        drawsquare(color)
    if ms==(1,0,0) and mx>125 and mx<155 and my>540 and my<570:
        pygame.draw.rect(win,(0,0,0),(0,0,500,500))
    if ms==(1,0,0) and mx>165 and mx<185 and my>540 and my<570:
        pygame.draw.line(win,(0,255,0),(170,540),(170,570),2)
        pygame.display.update()
        drawline(color)
    if ms==(1,0,0) and mx>205 and mx<235 and my>540 and my<570:
        try:
            CC=copycolor()
            color[0]=CC[0]
            color[1]=CC[1]
            color[2]=CC[2]
        except:
            continue
    if ms==(1,0,0) and mx>400 and mx<460 and my>540 and my<570:
        Open()
    if ms==(1,0,0) and mx>240 and mx<300 and my>540 and my<570:
        try:
            win.blit(frames[-1],(0,0))
            pygame.display.update()
            frames.remove(frames[-1])
            time.sleep(0.2)
        except:
            continue    
    size(ms,mx,my)    
    x,y,z=color
    
    pygame.draw.line(win,(255,255,255),(170,540),(170,570),2)
    pygame.draw.rect(win,(x,y,z),(0,575,600,25))
    pygame.draw.rect(win,(0,0,0),(mx2,575,5,25))
    pygame.draw.circle(win,(255,255,255),(60,555),15,2)
    pygame.draw.rect(win,(255,255,255),(85,540,30,30),2)
    pygame.draw.rect(win,(255,255,255),(0,0,500,500),1)
    pygame.draw.circle(win,(255,255,255),(140,555),15,3)
    pygame.draw.rect(win,(0,0,0),(145,540,15,30))
    Text("Save",350,560)
    Text("Open",430,560)
    Text("Undo",270,560)
    Text("Size",550,75)
   


    
    if (ms==(1,0,0)):
        mx,my=pygame.mouse.get_pos()
        if mx<500 and my<500:
            pygame.draw.circle(win,(x,y,z),(mx,my),SIZE)
    if (ms==(0,0,1)):
        
        bx,by=pygame.mouse.get_pos()
        if mx<500 and my<500:
            try:
                basecolor=win.get_at((bx,by))
                fill(mx,my,color,basecolor)
            except:
                continue
            
    win.blit(colorpicker,(195,540))   
    win.blit(eraser,(5,540))    
    pygame.display.update()
    
pygame.quit()        
    
