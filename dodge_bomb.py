import random
import sys

import pygame as pg

#練習４
delta = {
    pg.K_UP : (0,-1),
    pg.K_DOWN : (0,+1),
    pg.K_LEFT : (-1,0),
    pg.K_RIGHT : (+1,0),
}#↓トップレベルの後は空行２行


def check_bound(scr_rct :pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面外or画面内を判定し、真理値タプルを返す
    引数１　画面surfceのrect
    引数２　コウカトンまたは、爆弾のsurfceのrect
    戻り値：横方向、縦方向のはみ出し判定結果（画面内：True/画面外：False）
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko,tate

    


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect() #練習４
    kk_rct.center = 900, 400 #練習４
    #爆弾を作る
    bb_img = pg.Surface((20,20)) #黒い正方形を作る
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)#中心に赤い円を描画
    bb_img.set_colorkey((0,0,0))#黒を透過させる
    x = random.randint(0,1600)
    y = random.randint(0,900)
    vx, vy = +1, +1
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
        if check_bound(screen.get_rect(), kk_rct) != (True, True):#練習５
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)#こうかとん画像を900,440の位置にblit(貼り付ける)
        #screen.blit(bb_img, [x, y])　#練習問題２
        bb_rct.move_ip(vx, vy)
        
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko: #横方向にはみ出ていたら
            vx *= -1
        if not tate: #縦方向にはみ出ていたら
            vy *= -1
        screen.blit(bb_img,bb_rct) #練習問題３
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()