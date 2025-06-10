import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img=pg.image.load("fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)#こうかとんを左右反転
    bg_img2=pg.transform.flip(bg_img,True,False)#背景を反転]

    kk_rct=kk_img.get_rect()#10-1
    kk_rct.center=300,200#10-2
    
    tmr = 0
    k=[0,0]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst=pg.key.get_pressed()#10-3
        if key_lst[pg.K_UP]:
            k=[-1,-1]
        elif key_lst[pg.K_DOWN]:
            k=[-1,+1]
        elif key_lst[pg.K_LEFT]:
            k=[-1,0]
        elif key_lst[pg.K_RIGHT]:
            k=[+1,0]#10-4
        else:
            k=[-1,0]
        kk_rct.move_ip(k)


        x=tmr%3200
        screen.blit(bg_img, [-x,0])#１枚目　最初の背景
        screen.blit(bg_img2, [-x+1600,0])#２枚目　反転させた背景
        screen.blit(bg_img, [-x+3200, 0])#３枚目　反転の隣の、反転を戻した背景
   
        # screen.blit(kk_img, [300, 200])
        screen.blit(kk_img,kk_rct)#10-5

        pg.display.update()
        tmr += 1        
        clock.tick(200)
        print (key_lst)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
