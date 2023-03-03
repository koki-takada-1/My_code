#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

left = Motor(Port.B)
right = Motor(Port.C)

# wheel_diameterは車輪の直径 単位：ミリ
wheel_diameter = 56
# axle_trackは2つの車輪の中間点の間の距離 単位：ミリ
axle_track = 114
robot = DriveBase(left, right, 56)

# しきい値設定
gray_left = 50
gray_right = 50

black_left = 15
black_right = 15

white_left = 70
white_right = 70

# しきい値の英語はthresholdだから略してth
left_gb_th = (gray_left + black_left) / 2
right_gb_th = (gray_right + black_right) / 2
left_wg_th = (white_left + black_left) / 2
right_wg_th = (white_left + black_left) / 2

left_color = ColorSensor(Port.S1)
right_color = ColorSensor(Port.S2)

# マーカーカウント変数
cnt = 0

def marker_identify(white_left,white_right):
    # マーカーの数が　になったらオブジェクトを置きに行く
    if cnt == 10: 
        brick.sound.file(SoundFile.FORWARD,100)
        robot.drive_time(60,0,2000)
        robot.drive_time(-60,0,2000)
        robot.stop(Stop.BRAKE)
    
    if left_color.reflection() > left_wg_th:
        if right_color.reflection() > right_wg_th:
            #白、白
            robot.drive_time(40,0,1000)
            robot.drive_time(0,0,2000)
            robot.drive_time(0,180,2000)
            robot.stop(Stop.BRAKE)
        else:
            #白、グレー：右折
            cnt += 1
            robot.drive_time(80,0,1000)
            robot.drive_time(0,90,1000)
            robot.stop(Stop.BRAKE)
    else:
        if right_color.reflection() > right_wg_th:
            #グレー、白：左折
            cnt += 1
            robot.drive_time(80,0,1000)
            robot.drive_time(0,-90,1000)
            robot.stop(Stop.BRAKE)
        else:
            #グレー、グレー：前進
            robot.drive_time(80,0,1000)
# 定義終了
# ----------------------------ここからメイン-------------------------------      
# 最初前進
robot.drive_time(40,0,1000)

while True:
    if left_color.reflection() > left_gb_th:
        if right_color.reflection() > right_gb_th:
            
            pass
        else:
            pass
    else:
        if right_color.reflection() > right_gb_th:
            
            pass
        else:
            #黒、黒
            pass
            marker_identify()
            print(f'信号{cnt}回目')
            
    if cnt == 50:
        break
        
    
