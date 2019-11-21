# -*- coding: UTF-8 -*-
# drawing.py
 
# 导入需要的模块
import pygame, sys
from pygame.locals import *
from math import pi
 
 
# 初始化pygame
pygame.init()
 
# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((400,300))
 
# 设置窗口标题
pygame.display.set_caption('Drawing')
 
# 定义颜色
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
 
# 设置背景颜色
screen.fill(WHITE)
 
 
# 绘制一个圆
pygame.draw.circle(screen, BLUE, [60, 250], 5)
pygame.draw.circle(screen, BLACK, [70, 260], 5)
pygame.draw.circle(screen, BLUE, [80, 250], 5)
pygame.draw.circle(screen, BLACK, [90, 260], 5)
pygame.draw.circle(screen, BLUE, [100, 250], 5)
pygame.draw.circle(screen, BLACK, [110, 260], 5)
pygame.draw.circle(screen, BLUE, [120, 250], 5)
pygame.draw.circle(screen, BLACK, [130, 260], 5)

if y > size[0]:
        y = 0
else:
    y = y + 5
 
# 程序主循环
while True:
 
  # 获取事件
  for event in pygame.event.get():
    # 判断事件是否为退出事件
    if event.type == QUIT:
      # 退出pygame
      pygame.quit()
      # 退出系统
      sys.exit()
 
  # 绘制屏幕内容
  pygame.display.update()
