#suduko solver
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

def grid(x,y):
    pass
box=[]
def check(x,y,i):
    hor=[]
    ver=[]
    for ho in range(9):
        if mat[y][ho]!=0:
            hor.append(mat[y][ho])
    for ve in range(9):
        if mat[ve][x]!=0:
            ver.append(mat[ve][x])
    grid(x,y)
    if i not in (hor+ver):
        mat[y][x]=i
        return True
    else:
        return False
            
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
while done:
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
        c12=mat[b1][a1]
    if ok1==len(used):
        break

for k in mat:
    str1=""
    for l in k:
        str1+=str(l)+" "
    print(str1)
