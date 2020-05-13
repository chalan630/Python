import pygame
# 自定义部分
import btnFunction as bf
import gameFlag as gl
from config import Config
from button import Button


def init_button():
    """
    设置游戏中用到的所有Button
    :return: {dic}包含所有按钮的字典
    """
    # 暂停按钮图片
    pauseBtns = dict()
    pauseBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'pause_0.png').convert_alpha()
    pauseBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'pause_1.png').convert_alpha()
    pauseBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'pause_2.png').convert_alpha()

    resumeBtns = dict()
    resumeBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'resume_0.png').convert_alpha()
    resumeBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'resume_1.png').convert_alpha()
    resumeBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'resume_2.png').convert_alpha()
    stdBtns = dict()
    stdBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'button_restart_0.png').convert_alpha()
    stdBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'button_restart_1.png').convert_alpha()
    stdBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'button_restart_2.png').convert_alpha()

    pause_rect = pauseBtns['Normal'].get_rect()
    pause_rect.left, pause_rect.top = Config.get('WIDTH') - pause_rect.width - 10, 10
    # 初始化按钮字体
    btnFont = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 40)
    # 初始化按钮
    # 开始按钮
    Btns = dict()
    Btns['pause'] = Button(pause_rect.left, pause_rect.top, "", pauseBtns['Normal'], \
                           pauseBtns['Select'], pauseBtns['Click'], bf.btn_pause, btnFont)
    Btns['resume'] = Button(pause_rect.left, pause_rect.top, "", resumeBtns['Normal'], \
                            resumeBtns['Select'], resumeBtns['Click'], bf.btn_pause, btnFont)
    Btns['start'] = Button(90, 300, "开始游戏", stdBtns['Normal'], stdBtns['Select'], \
                           stdBtns['Click'], bf.btn_start, btnFont)
    Btns['restart'] = Button(90, 400, "重新开始", stdBtns['Normal'], stdBtns['Select'], \
                             stdBtns['Click'], bf.btn_restart, btnFont)
    Btns['sign_in'] = Button(90, 300, "登  陆", stdBtns['Normal'], stdBtns['Select'], \
                             stdBtns['Click'], bf.btn_sign_in, btnFont)
    Btns['register'] = Button(90, 400, "注  册", stdBtns['Normal'], stdBtns['Select'], \
                              stdBtns['Click'], bf.btn_register, btnFont)
    Btns['quit'] = Button(90, 500, "退出游戏", stdBtns['Normal'], stdBtns['Select'], \
                          stdBtns['Click'], bf.btn_quit, btnFont)
    Btns['sign_in_check'] = Button(90, 500, "登  陆", stdBtns['Normal'], stdBtns['Select'], \
                                   stdBtns['Click'], bf.btn_sign_in_check, btnFont)
    Btns['register_check'] = Button(90, 500, "注  册", stdBtns['Normal'], stdBtns['Select'], \
                                    stdBtns['Click'], bf.btn_register_check, btnFont)
    Btns['log_out'] = Button(90, 500, "退出登陆", stdBtns['Normal'], stdBtns['Select'], \
                             stdBtns['Click'], bf.btn_log_out, btnFont)
    Btns['endless'] = Button(90, 400, "无尽模式", stdBtns['Normal'], stdBtns['Select'], \
                             stdBtns['Click'], bf.btn_endless_mode, btnFont)
    Btns['Map1'] = Button(90, 300, "Map 1", stdBtns['Normal'], stdBtns['Select'], \
                          stdBtns['Click'], bf.btn_map1, btnFont)
    Btns['Map2'] = Button(90, 400, "Map 2", stdBtns['Normal'], stdBtns['Select'], \
                          stdBtns['Click'], bf.btn_map2, btnFont)
    Btns['Map3'] = Button(90, 500, "Map 3", stdBtns['Normal'], stdBtns['Select'], \
                          stdBtns['Click'], bf.btn_map3, btnFont)
    Btns['back1'] = Button(90, 500, "返回菜单", stdBtns['Normal'], stdBtns['Select'], \
                           stdBtns['Click'], bf.btn_back, btnFont)
    rank_img = pygame.image.load(Config.get('imgfolder') + 'rank.png').convert_alpha()

    Btns['rank'] = Button(430, 670, "", rank_img, rank_img, rank_img, bf.btn_rank, btnFont)

    back = dict()
    back['Normal'] = pygame.image.load(Config.get('imgfolder') + 'back_0.png').convert_alpha()
    back['Normal'] = pygame.transform.smoothscale(back['Normal'], (40, 40))
    back['Select'] = pygame.image.load(Config.get('imgfolder') + 'back_1.png').convert_alpha()
    back['Select'] = pygame.transform.smoothscale(back['Select'], (40, 40))
    back['Click'] = pygame.image.load(Config.get('imgfolder') + 'back_2.png').convert_alpha()
    back['Click'] = pygame.transform.smoothscale(back['Click'], (40, 40))
    Btns['back'] = Button(10, 670, "", back['Normal'], back['Select'], back['Click'], bf.btn_back, btnFont)
    tom = dict()
    tom['Normal'] = pygame.image.load(Config.get('imgfolder') + 'tom_skill_1.png').convert_alpha()
    tom['Select'] = pygame.image.load(Config.get('imgfolder') + 'tom_skill.png').convert_alpha()
    tom['Click'] = pygame.image.load(Config.get('imgfolder') + 'tom_skill.png').convert_alpha()
    Btns['tom'] = Button(90, 300, "", tom['Normal'], tom['Select'], \
                         tom['Click'], bf.btn_tom, btnFont)
    jerry = dict()
    jerry['Normal'] = pygame.image.load(Config.get('imgfolder') + 'jerry_skill_1.png').convert_alpha()
    jerry['Select'] = pygame.image.load(Config.get('imgfolder') + 'jerry_skill.png').convert_alpha()
    jerry['Click'] = pygame.image.load(Config.get('imgfolder') + 'jerry_skill.png').convert_alpha()
    Btns['jerry'] = Button(90, 500, "", jerry['Normal'], jerry['Select'], \
                           jerry['Click'], bf.btn_jerry, btnFont)

    return Btns
