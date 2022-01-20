import pygame as p
import time

p.init()
screen = p.display.set_mode((450, 510))
p.display.set_caption("sudoku solver")

def precheck():
    global cantsolve, sol, used, lt
    for y in range(9):
        for x in range(9):
            if mat[y][x] == 0:
                used.append((x, y))
            elif not check(x, y, mat[y][x], False):
                cantsolve = True
                lt = time.time()
                sol = False
                used = []
                return

def solve():
    global positiontosolve, lastvalue
    cansolve = False
    b, c = used[positiontosolve]
    for i in range(lastvalue + 1, 10):
        cansolve = check(b, c, i, True)
        if cansolve == True:
            break
    if cansolve == True:
        positiontosolve += 1
        lastvalue = 0
    elif cansolve == False:
        mat[c][b] = 0
        positiontosolve -= 1
        a1, b1 = used[positiontosolve]
        val = mat[b1][a1]
        if val > 9:
            val = val // 10
        lastvalue = val


def check(x, y, i, ss):
    x1, y1 = x // 3 * 3, y // 3 * 3
    maxx, maxy = x1 + 3, y1 + 3
    while True:
        val = mat[y1][x1]
        if val != 0 and (x != x1 and y != y1):
            if val > 9:
                val = val // 10
            if i == val:
                return False
        x1 += 1
        if x1 == maxx:
            x1 -= 3
            y1 += 1
        if y1 == maxy:
            break
    for k in range(9):
        if k != x:
            val = mat[y][k]
            if val != 0:
                if val > 9:
                    val = val // 10
                if i == val:
                    return False
        if k != y:
            val = mat[k][x]
            if val != 0:
                if val > 9:
                    val = val // 10
                if i == val:
                    return False
    if ss:
        mat[y][x] = i * 10
    return True


class button:
    def __init__(self, x, y, st):
        self.x, self.y, self.st, self.bool = x, y, st, True
        if self.st == "Solve":
            self.color1 = (246, 208, 77)
            self.color2 = (139, 194, 76)
        else:
            self.color1 = (46, 148, 185)
            self.color2 = (91, 231, 196)

    def check(self, x1, y1, click):
        global sol, used, entering, hassolved, mat, positiontosolve, lastvalue
        if self.x - 75 < x1 < self.x + 75 and self.y - 20 < y1 < self.y + 20:
            self.bool = False
            if click == 1:
                if self.st == "Solve" and not(sol or hassolved):
                    sol = True
                    entering = False
                    precheck()
                if self.st == "Reset" and (not sol or hassolved):
                    sol,hassolved = False,False
                    positiontosolve, lastvalue = 0, 0
                    used = []
                    mat = [[0 for i in range(9)] for j in range(9)]
        else:
            self.bool = True

    def draw_button(self):
        if self.bool:
            c1 = self.color1
            c2 = self.color2
        else:
            c2 = self.color1
            c1 = self.color2
        font = p.font.Font("freesansbold.ttf", 32)
        text = font.render(self.st, True, c1)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        p.draw.rect(screen, c2, [(self.x - 75, self.y - 20), (150, 40)])
        screen.blit(text, textRect)


def grid_draw():
    for x in range(1, 10):
        if x % 3 == 0:
            p.draw.line(screen, (0, 0, 0), (0, x * 50), (450, x * 50), 3)
        else:
            p.draw.line(screen, (0, 0, 0), (0, x * 50), (450, x * 50), 2)
    for y in range(1, 9):
        if y % 3 == 0:
            p.draw.line(screen, (0, 0, 0), (y * 50, 0), (y * 50, 450), 3)
        else:
            p.draw.line(screen, (0, 0, 0), (y * 50, 0), (y * 50, 450), 2)


def draw_no(num, x, y):
    if num != 0:
        font = p.font.Font("freesansbold.ttf", 32)
        if num > 9:
            num = num // 10
            text = font.render(str(num), True, (0, 200, 0))
        else:
            text = font.render(str(num), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (25 + 50 * x, 25 + 50 * y)
        screen.blit(text, textRect)


positiontosolve = 0
lastvalue = 0
sol = False
hassolved = False
cantsolve = False
used = []
mat = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
solv = button(365, 482, "Solve")
rese = button(85, 482, "Reset")
timer = 0
lt = 0
done = False
entering = False
mm0, mm1 = None, None

while not done:
    for event in p.event.get():
        if event.type == p.QUIT:
            done = True
    mo = p.mouse.get_pressed()
    mo0, mo1 = p.mouse.get_pos()
    if (mo[0] == 1 and mo1 < 450) and not (sol or hassolved):
        entering = True
        mm0, mm1 = mo0, mo1
    if entering:
        keypress = p.key.get_pressed()
        if keypress[p.K_BACKSPACE]:
            mat[mm1 // 50][mm0 // 50] = 0
            entering = False
        for i in range(p.K_0, p.K_9 + 1):
            if keypress[i]:
                mat[mm1 // 50][mm0 // 50] = i - p.K_0
                entering = False
        keypad = [
            p.K_KP0,
            p.K_KP1,
            p.K_KP2,
            p.K_KP3,
            p.K_KP4,
            p.K_KP5,
            p.K_KP6,
            p.K_KP7,
            p.K_KP8,
            p.K_KP9,
        ]
        for i in range(len(keypad)):
            if keypress[keypad[i]]:
                mat[mm1 // 50][mm0 // 50] = i
                entering = False

    screen.fill((250, 250, 250))
    grid_draw()
    if sol:
        solve()
        if positiontosolve == len(used):
            sol = False
            hassolved = True

    for x in range(9):
        for y in range(9):
            draw_no(mat[y][x], x, y)

    if cantsolve:
        timer += time.time() - lt
        lt = time.time()
        if timer > 4:
            timer, cantsolve = 0, False
        font = p.font.Font("freesansbold.ttf", 32)
        text = font.render("can't solve this sudoku", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (225, 275)
        p.draw.rect(screen, (255, 50, 50), [(225 - 200, 275 - 20), (400, 40)])
        screen.blit(text, textRect)
    if entering:
        p.draw.rect(
            screen, (0, 0, 255), [(mm0 // 50 * 50, mm1 // 50 * 50), (51, 51)], 3
        )
    solv.check(mo0, mo1, mo[0])
    solv.draw_button()
    rese.check(mo0, mo1, mo[0])
    rese.draw_button()
    p.display.update()
p.quit()
