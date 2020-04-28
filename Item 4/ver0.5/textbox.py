import pygame


class TextBox:
    def __init__(self, w, h, x, y, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        :param callback:在文本框按下回车键之后的回调函数
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        self.callback = callback
        self.size = 10  # 文本框长度
        # 创建
        self.__surface = pygame.Surface((w, h))
        # 如果font为None,那么效果可能不太好，建议传入font，更好调节
        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font

    def colli(self, x, y):
        # 碰撞检测
        if self.x < x < self.x+self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False

    def draw(self, dest_surf, is_hidden=False):
        if is_hidden:
            hidden_text = "*" * len(self.text)
            text_surf = self.font.render(hidden_text, True, (255, 255, 255))
        else:
            text_surf = self.font.render(self.text, True, (255, 255, 255))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))

    def key_down(self, x, y, event):
        if self.colli(x, y):    # 鼠标放入框内，使输入框使能
            if len(self.text) <= self.size:
                unicode = event.unicode
                key = event.key
                # 退位键
                if key == 8:
                    self.text = self.text[:-1]
                    return
                # 切换大小写键
                if key == 301:
                    return
                # 回车键
                if key == 13:
                    if self.callback is not None:
                        self.callback()
                    return
                if unicode != "":
                    char = unicode
                else:
                    char = chr(key)
                self.text += char

    def get_text(self):
        return self.text

    def clean_text(self):
        self.text = ""
