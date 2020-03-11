import cng
import numpy as np

'''
    T=np.array([[1,0,fenetre[0]],[0,1,fenetre[1]],[0,0,1]])
    D=np.array([[(1/winX),0,0],[0,(1/winY),0],[0,0,1]])
    Di=np.array([[vueX,0,0],[0,vueY,0],[0,0,1]])
    Ti=np.array([[1,0,vue[0]],[0,1,vue[1]],[0,0,1]])
    Res=Ti*Di*D*T
'''

WIN_SEL=False
scr_width=1920
scr_height=1000

ex_points=[[5,5]]
fenetre=[-10,-10,10,10]
vue=[260,100,1660,900]

main=cng.init_window('Ecran', scr_width, scr_height)
ex_window=cng.rectangle(260,100,1660,900,5)

def calc_mat(window):#calcule la matrice de projection
    global fenetre
    vue=cng.obj_get_coord(window)
    winX=fenetre[2]-fenetre[0]
    winY=fenetre[3]-fenetre[1]
    vueX=vue[2]-vue[0]#dx=1400
    vueY=vue[3]-vue[1]#dy=800

    #Res=[[(vueX/winX),0,(fenetre[0]-(vueX*fenetre[0]/winX))],[0,(vueY/winY),(fenetre[1]-(vueY*fenetre[1]/winY))],[0,0,1]]
    Res=[[(vueX/winX),0,((vueX*fenetre[0]/winX)-fenetre[0])],[0,(vueY/winY),((vueY*fenetre[1]/winY)-fenetre[1])],[0,0,1]]
    return Res

affic_Mat=calc_mat(ex_window)
print(affic_Mat)

def select():#bool de selection de fenetre
    global WIN_SEL
    x=cng.get_mouse_x()
    y=cng.get_mouse_y()
    pos=cng.obj_get_position(window)
    if cng.obj_picked(window, x, y):
        WIN_SEL=True
    else:
        WIN_SEL=False

def move_up():
    if WIN_SEL:
        cng.obj_move(ex_window, 0,10)

def move_left():
    if WIN_SEL:
        cng.obj_move(ex_window, -10,0)

def move_down():
    if WIN_SEL:
        cng.obj_move(ex_window, 0,-10)

def move_right():
    if WIN_SEL:
        cng.obj_move(ex_window, 10,0)

def calc_points():
    for p in ex_points:
        calc_point(p)

def calc_point(point):
    #projPoint=point*affic_Mat
    #print(projPoint)
    return

cng.assoc_button(1, select)
cng.assoc_key('z', move_up)
cng.assoc_key('q', move_left)
cng.assoc_key('s', move_down)
cng.assoc_key('d', move_right)
cng.assoc_key('r', calc_points)
cng.mainloop()
