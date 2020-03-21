import pygame as p
p.init()
screen=p.display.set_mode((450,550))
p.display.set_caption("sudoku solver")

def precheck():
    x=0
    y=0
    done=True
    while done:
        if mat[y][x]==0:
            used.append((x,y))
        x+=1
        if x==9:
            x=0
            y+=1
        if y==9:
            break
ok1=0
c12=0
done1=True
def solve():
    global ok1,c12,done1
    b,c=used[ok1]
    for i in range(c12+1,10):
        done1=check(b,c,i)
        if done1==True:
            break
    if done1==True:
        ok1+=1
        c12=0
    elif done1==False:
        mat[c][b]=0
        ok1-=1
        a1,b1=used[ok1]
        ok=mat[b1][a1]
        if ok>9:
            ok=ok//10
        c12=ok

ok=True
sol=False
class button:
    def __init__(self,x,y,st):
        self.x=x
        self.y=y
        self.st=st
        self.bool=True
        if self.st=="Solve":
            self.color1=(246,208,77)
            self.color2=(139,194,76)
        else :
            self.color1=(46,148,185)
            self.color2=(91,231,196)
    def check(self,x1,y1,click):
        global ok,sol
        if self.x-75<x1<self.x+75 and self.y-20<y1<self.y+20:
            self.bool=False
            if click==1:
                if self.st=="Solve"  and ok:
                    ok=False
                    precheck()
                    sol=True
                if self.st=="Reset":
                    ok=True
                    x=0
                    y=0
                    while True:
                        mat[y][x]=0
                        x+=1
                        if x==9:
                            x=0
                            y+=1
                        if y==9:
                            break
        else :
            self.bool=True
    def draw_button(self):
        if self.bool:
            c1=self.color1
            c2=self.color2
        else :
            c2=self.color1
            c1=self.color2
        font = p.font.Font('freesansbold.ttf',32)
        text = font.render(self.st, True, c1) 
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        p.draw.rect(screen,c2,[(self.x-75,self.y-20),(150,40)])
        screen.blit(text, textRect)

def grid_draw():
    for x in range (1,10):
        if x%3==0:
            p.draw.line(screen,(0,0,0),(0,x*50),(450,x*50),3)
        else:
            p.draw.line(screen,(0,0,0),(0,x*50),(450,x*50),2)
    for y in range(1,9):
        if y%3==0:
            p.draw.line(screen,(0,0,0),(y*50,0),(y*50,450),3)
        else :
            p.draw.line(screen,(0,0,0),(y*50,0),(y*50,450),2)

used=[]
mat=[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def draw_no(ok,x,y):
    if ok!=0:
        font=p.font.Font('freesansbold.ttf',32)
        if ok>9:
            ok=ok//10
            text=font.render(str(ok),True,(0,200,0))
        else :
            text=font.render(str(ok),True,(0,0,0))
        textRect=text.get_rect()
        textRect.center=(25+50*x,25+50*y)
        screen.blit(text,textRect)

def check(x,y,i):
    hor=[]
    ver=[]
    box=[]
    x1=x//3*3
    y1=y//3*3
    maxx=x1+3
    maxy=y1+3
    while True:
        ok=mat[y1][x1]
        if ok!=0:
            if ok>9:
                ok=ok//10
            box.append(ok)
        x1+=1
        if x1==maxx:
            x1-=3
            y1+=1
        if y1==maxy:
            break
    for ho in range(9):
        ok=mat[y][ho]
        if ok!=0:
            if ok>9:
                ok=ok//10
            hor.append(ok)
    for ve in range(9):
        ok = mat[ve][x]
        if ok!=0:
            if ok>9:
                ok=ok//10
            ver.append(ok)
    if i not in (set(box+hor+ver)):
        mat[y][x]=i*10
        return True
    else:
        return False

solv=button(337,500,"Solve")
rese=button(112,500,"Reset")
done=False
while not done:
    for event in p.event.get():
        if event.type==p.QUIT:
            done=True
    mo=p.mouse.get_pressed()
    mo0,mo1=p.mouse.get_pos()
    if mo[0]==1 and mo1<450:
        done1=True
        while done1:
            keypress=p.key.get_pressed()
            p.draw.rect(screen,(0,0,255),[(mo0//50*50,mo1//50*50),(51,51)],3)
            p.display.update()
            for event in p.event.get():
                if event.type==p.QUIT:
                    done1=False
            for i in range(48,58):
                if keypress[i]:
                    mat[mo1//50][mo0//50]=i-48
                    done1=False
    screen.fill((250,250,250))
    grid_draw()
    if sol:
        solve()
        if ok1==len(used):
            sol=False
    x=0
    y=0
    while True:
        draw_no(mat[y][x],x,y)
        x+=1
        if x==9:
            x=0
            y+=1
        if y==9:
            break
    solv.check(mo0,mo1,mo[0])
    solv.draw_button()
    rese.check(mo0,mo1,mo[0])
    rese.draw_button()
    p.display.update()
p.quit()