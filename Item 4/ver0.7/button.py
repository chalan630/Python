'''
@Descripttion: 按钮类
@version: ver0.5
@Author: chalan630
@Date: 2020-03-02 23:37:29
@LastEditTime: 2020-03-23 15:08:41
'''
import pygame


class Button:
    NORMAL = 0
    SELECT = 1
    CLICK = 2

    def __init__(self, x, y, text, imgNormal, imgSelect=None, imgClick=None, callBackFunc=None, font=None, rgb=(0, 0, 0)):
        self.imgs = []
        if not imgNormal:
            raise Exception("请设置普通状态的照片")
        self.imgs.append(imgNormal)     # 普通状态显示图片
        self.imgs.append(imgSelect)       # 被选中时显示图片
        self.imgs.append(imgClick)       # 被按下时显示图片
        self.callBackFunc = callBackFunc    # 触发事件
        self.status = Button.NORMAL
        self.x, self.y = x, y
        self.width = imgNormal.get_width()
        self.height = imgNormal.get_height()
        self.text = text
        self.font = font
        self.textSur = self.font.render(self.text, True, rgb)

    def draw(self, destSur):
        dx = (self.width/2) - (self.textSur.get_width() / 2)
        dy = (self.height/2) - (self.textSur.get_height() / 2)
        # 先画按钮背景
        if self.imgs[self.status]:
            destSur.blit(self.imgs[self.status], [self.x, self.y])
        # 再画出文字
        destSur.blit(self.textSur, [self.x + dx, self.y + dy])

    def colli(self, x, y):
        # 碰撞检测
        if self.x < x < self.x+self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False

    def getFocus(self, x, y):
        if self.status == Button.CLICK:
            return
        if self.colli(x, y):
            self.status = Button.SELECT
        else:
            self.status = Button.NORMAL

    def mouseDown(self, x, y):
        if self.colli(x, y):
            self.status = Button.CLICK

    def mouseUp(self):
        if self.status == Button.CLICK:
            self.status = Button.NORMAL
            if self.callBackFunc:
                return self.callBackFunc()
