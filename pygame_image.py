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
    bg_img2=pg.transform.flip(bg_img,True,False)#背景を反転
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200
        screen.blit(bg_img, [-x,0])#最初の背景
        screen.blit(bg_img2, [-x+1600,0])#反転させた背景を繋げる
        screen.blit(bg_img, [-x+3200, 0])#反転の隣の、反転を戻した背景

        
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()