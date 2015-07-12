# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys

# ボールの動きを計算
def calc_ball(ball_x, ball_y, ball_vx, ball_vy, bar1_x, bar1_y, bar2_x, bar2_y):
        if ball_x <= bar1_x + 10:
            if ball_y >= bar1_y - 8 and ball_y <= bar1_y + 43:
                ball_x = 20.
                ball_vx = -ball_vx
        if ball_x >= bar2_x - 15:
            if ball_y >= bar2_y - 8 and ball_y <= bar2_y + 43:
                ball_x = 605
                ball_vx = -ball_vx
        if ball_x < 5:
            ball_x, ball_y = 320, 233
        elif ball_x > 620:
            ball_x, ball_y = 308, 233
        if ball_y <= 10:
            ball_vy = -ball_vy
            ball_y = 10
        elif ball_y >= 458:
            ball_vy = -ball_vy
            ball_y = 458

        return int(ball_x), int(ball_y), ball_vx, ball_vy

# AIの動きを計算
def calc_ai(ball_x, ball_y, bar2_x, bar2_y):
    dy = ball_y - bar2_y
    if dy > 80: bar2_y += 20
    elif dy > 50: bar2_y += 15
    elif dy > 30: bar2_y += 12
    elif dy > 10: bar2_y += 8
    elif dy < -80: bar2_y -= 20
    elif dy < -50: bar2_y -= 15
    elif dy < -30: bar2_y -= 12
    elif dy < -10: bar2_y -= 8

    if bar2_y >= 420: bar2_y = 420
    elif bar2_y <= 10: bar2_y = 10
    return int(bar2_y)

# プレイヤーの動き
def calc_player(bar1_y, bar1_dy):
    bar1_y += bar1_dy
    if bar1_y >= 420: bar1_y = 420
    elif bar1_y <= 10 : bar1_y = 10
    return int(bar1_y)

# 得点の計算
def calc_score(ball_x, score1, score2):
    if ball_x < 5:
        score2 += 1
    if ball_x > 620:
        score1 += 1
    return score1, score2

def main():
    # 各パラメータ
    bar1_x, bar1_y = 10 , 215
    bar2_x, bar2_y = 620, 215
    ball_x, ball_y = 308, 233
    bar1_dy, bar2_dy = 0 , 0
    ball_vx, ball_vy = 250, 250
    score1, score2 = 0,0

    while (1):
        im = np.zeros((480,640,1), np.uint8)                                # 背景用640*480の黒塗り画像
        # 図形(各物体)の描画
        cv2.rectangle(im,(330,5),(330,475),(255,255,255),-1)                # 中央線の描画
        cv2.rectangle(im,(bar1_x-5,bar1_y-25),(bar1_x+5,bar1_y+25),255,-1)  # プレイヤー側バーの描画
        cv2.rectangle(im,(bar2_x-5,bar2_y-25),(bar2_x+5,bar2_y+25),255,-1)  # CPU側バーの描画
        cv2.circle(im,(ball_x, ball_y), 10, (255,255,255), -1)              # ボールの描画
        cv2.putText(im,str(score1),(220,50),0, 2, 255, 2)                   # プレイヤー側得点を描画
        cv2.putText(im,str(score2),(400,50),0, 2, 255, 2)                   # CPU側得点を描画
        # プレイヤー側バーの位置
        bar1_y = calc_player(bar1_y,bar1_dy)
        # ボールの移動
        ball_x += int(ball_vx * 0.015)
        ball_y += int(ball_vy * 0.015)
        # 得点の計算
        score1, score2 = calc_score(ball_x, score1, score2)
        # CPUのバー速度を計算
        bar2_y = calc_ai(ball_x, ball_y, bar2_x, bar2_y)
        # ボールの速度・位置を計算
        ball_x, ball_y, ball_vx, ball_vy = calc_ball(ball_x, ball_y, ball_vx, ball_vy, bar1_x, bar1_y, bar2_x, bar2_y)
        cv2.imshow("PONG",im)
        k = cv2.waitKey(1)
        if k == 27:              # Escキーが押されたら終了
            cv2.destroyAllWindows()
            break
        elif k == 2490368:       # 矢印上キーが押されたらプレイヤー側バーを上に移動
            bar1_dy = -20
        elif k == 2621440:       # 矢印下キーを押されたらプレイヤー側バーを下に移動
            bar1_dy = 20
        else:
            bar1_dy = 0          # 何も押されなければプレイヤー側バーは停止


if __name__ == "__main__":
    main()