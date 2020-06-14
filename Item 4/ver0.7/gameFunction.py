'''
@Descripttion: 游戏函数
@version: ver0.7
@Author: chalan630
@Date: 2020-03-02 23:37:29
@LastEditTime: 2020-06-06 00:37:34
'''
import pygame
import sys
import random
import pymysql
import gameFlag as gl
from hero import Hero
from config import Config
from enemy import Enemy
from wall import Wall
from healthStar import HealthStar
from scoreStar import ScoreStar
from limitStar import LimitStar
from swamp import Swamp
from damage import Damage
from jerry import Jerry
from ice import Ice
from tom import Tom


# TODO: 开始界面方向键报错 √
# TODO: 返回按钮 √
# TODO: 多种英雄角色 技能系统 √
# TODO: 排行榜(区分地图)
# TODO: 登录注册 数据保存 √
# TODO: 减速方块(草地) √
# TODO: 禁止转向方块(雪地) √
# TODO: 伤害方块(沙漠) √
# TODO: 趣味关卡
# TODO: 音效
# TODO: 角色选择 √
# TODO: 难度变化后更改障碍移动速度 √
# TODO: 分数取整数 √
# TODO: 游戏难度显示异常 √
# TODO: 障碍伤害过高 √
# TODO: **在wall和enemy的构造函数中传入当前游戏level**
# TODO: 用户名或密码为空


pygame.mixer.init()
over_sound = pygame.mixer.Sound(Config.get('musicfolder') + "game_over.ogg")
over_sound.set_volume(0.2)


def check_keydown_events(event, mx, my):
    """
    检查按键按下事件(二级函数)
    :param event: 事件
    """
    if gl.get_value('isGameStatus') == 'sign_in':
        name_text_box = gl.get_value('name_text_box')
        pass_text_box = gl.get_value('pass_text_box')
        name_text_box.key_down(mx, my, event)
        pass_text_box.key_down(mx, my, event)
    elif gl.get_value('isGameStatus') == 'register':
        name_text_box = gl.get_value('name_text_box')
        pass_text_box = gl.get_value('pass_text_box')
        again_text_box = gl.get_value('again_text_box')
        name_text_box.key_down(mx, my, event)
        pass_text_box.key_down(mx, my, event)
        again_text_box.key_down(mx, my, event)
    elif gl.get_value('isGameStatus') == 'game_start':
        hero = gl.get_value('hero')
        walls = gl.get_value('walls')
        if event.key == pygame.K_RIGHT:
            hero.setDirect('right', True)
        elif event.key == pygame.K_LEFT:
            hero.setDirect('left', True)
        elif event.key == pygame.K_UP:
            hero.setDirect('up', True)
        elif event.key == pygame.K_DOWN:
            hero.setDirect('down', True)
        elif event.key == pygame.K_q:
            gl.set_value('isGameStatus', 'menu')
        elif event.key == pygame.K_SPACE:
            if hero.skill_count > 0:
                hero.skill()
                hero.skill_count -= 1


def check_keyup_events(event):
    """
    检查按键抬起事件(三级函数)
    :param event: 事件
    """
    if gl.get_value('isGameStatus') == 'game_start':
        hero = gl.get_value('hero')
        if event.key == pygame.K_RIGHT:
            hero.setDirect('right', False)
        elif event.key == pygame.K_LEFT:
            hero.setDirect('left', False)
        elif event.key == pygame.K_UP:
            hero.setDirect('up', False)
        elif event.key == pygame.K_DOWN:
            hero.setDirect('down', False)


def check_event(Btns):
    """
    游戏事件检查(一级函数)
    :param Btns: 按键字典
    :return:
    """
    # 获取鼠标坐标
    mx, my = pygame.mouse.get_pos()
    # 获取键盘输入，并处理事件
    for event in pygame.event.get():  # 事件循环
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mx, my)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)
        elif event.type == pygame.MOUSEMOTION:
            # 判断鼠标是否移动到按钮范围之内
            for key in Btns:
                if gl.get_value('isGameStatus') == 'start':
                    if key == 'register' or key == 'sign_in' or \
                            key == 'quit' or key == 'rank' or \
                            key == 'back':
                        Btns[key].getFocus(mx, my)
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].getFocus(mx, my)

                elif gl.get_value('isGameStatus') == 'sign_in':
                    if key == 'sign_in_check' or key == 'back':
                        Btns[key].getFocus(mx, my)
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'menu':
                    if key == 'start' or key == 'log_out' or key == 'endless' or \
                            key == 'rank':
                        Btns[key].getFocus(mx, my)
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_start':
                    if key == 'pause' and gl.get_value('isPause') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'resume' and gl.get_value('isPause') == True:
                        Btns[key].getFocus(mx, my)
                    elif key == 'back1' and gl.get_value('isPause') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_over':
                    if key == 'restart' or key == 'back1' or key == 'rank':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_map_select':
                    if key == 'Map1' or key == 'Map2' or key == 'Map3' or \
                            key == 'back' or key == 'rank':
                        Btns[key].getFocus(mx, my)
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'select_hero':
                    if key == 'tom' or key == 'jerry' or key == 'back':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'register':
                    if key == 'register_check' or key == 'back':
                        Btns[key].getFocus(mx, my)
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'board':
                    if key == 'back':
                        Btns[key].getFocus(mx, my)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键
                for key in Btns:
                    if gl.get_value('isGameStatus') == 'start':
                        if key == 'register' or key == 'sign_in' or \
                                key == 'quit' or key == 'rank' or \
                                key == 'back':
                            Btns[key].mouseDown(mx, my)
                        if key == 'sound_off' and gl.get_value('bgm') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'sound_on' and gl.get_value('bgm') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'sign_in':
                        if key == 'sign_in_check' or key == 'back':
                            Btns[key].mouseDown(mx, my)
                        if key == 'sound_off' and gl.get_value('bgm') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'sound_on' and gl.get_value('bgm') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'menu':
                        if key == 'start' or key == 'log_out' or key == 'endless' or \
                                key == 'rank':
                            Btns[key].mouseDown(mx, my)
                        if key == 'sound_off' and gl.get_value('bgm') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'sound_on' and gl.get_value('bgm') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_start':
                        if key == 'pause' and gl.get_value('isPause') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'resume' and gl.get_value('isPause') == True:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'back1' and gl.get_value('isPause') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_over':
                        if key == 'restart' or key == 'back1' or key == 'rank':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_map_select':
                        if key == 'Map1' or key == 'Map2' or key == 'Map3' or \
                                key == 'back' or key == 'rank':
                            Btns[key].mouseDown(mx, my)
                        if key == 'sound_off' and gl.get_value('bgm') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'sound_on' and gl.get_value('bgm') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'select_hero':
                        if key == 'tom' or key == 'jerry' or key == 'back':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'register':
                        if key == 'register_check' or key == 'back':
                            Btns[key].mouseDown(mx, my)
                        if key == 'sound_off' and gl.get_value('bgm') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'sound_on' and gl.get_value('bgm') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'board':
                        if key == 'back':
                            Btns[key].mouseDown(mx, my)

        elif event.type == pygame.MOUSEBUTTONUP:
            for key in Btns:
                if gl.get_value('isGameStatus') == 'start':
                    if key == 'register' or key == 'sign_in' or \
                            key == 'quit' or key == 'rank' or \
                            key == 'back':
                        Btns[key].mouseUp()
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].mouseUp()
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'sign_in':
                    if key == 'sign_in_check' or key == 'back':
                        Btns[key].mouseUp()
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].mouseUp()
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'menu':
                    if key == 'start' or key == 'log_out' or key == 'endless' or \
                            key == 'rank':
                        Btns[key].mouseUp()
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].mouseUp()
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_start':
                    if key == 'pause' and gl.get_value('isPause') == False:
                        Btns[key].mouseUp()
                    elif key == 'resume' and gl.get_value('isPause') == True:
                        Btns[key].mouseUp()
                    elif key == 'back1' and gl.get_value('isPause') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_over':
                    if key == 'restart' or key == 'back1' or key == 'rank':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_map_select':
                    if key == 'Map1' or key == 'Map2' or key == 'Map3' or \
                            key == 'back' or key == 'rank':
                        Btns[key].mouseUp()
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].mouseUp()
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'select_hero':
                    if key == 'tom' or key == 'jerry' or key == 'back':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'register':
                    if key == 'register_check' or key == 'back':
                        Btns[key].mouseUp()
                    if key == 'sound_off' and gl.get_value('bgm') == False:
                        Btns[key].mouseUp()
                    elif key == 'sound_on' and gl.get_value('bgm') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'board':
                    if key == 'back':
                        Btns[key].mouseUp()


def error_message(screen):
    num = gl.get_value('error_type')
    title_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 32)
    if num == 1:
        sign_in_text = title_font.render("用户名或密码错误", True, (0, 0, 0))
        screen.blit(sign_in_text, (112, 460))
    elif num == 2:
        sign_in_text = title_font.render("用户名已存在", True, (0, 0, 0))
        screen.blit(sign_in_text, (112, 190))
    elif num == 3:
        sign_in_text = title_font.render("用户名或密码不能为空", True, (0, 0, 0))
        screen.blit(sign_in_text, (112, 190))
    elif num == 4:
        sign_in_text = title_font.render("两次输入密码不一致", True, (0, 0, 0))
        screen.blit(sign_in_text, (112, 190))

def sign_in(screen):
    """
    登陆页面函数
    :param screen:
    :return:
    """
    pass_text_box = gl.get_value('pass_text_box')
    name_text_box = gl.get_value('name_text_box')
    name_text_box.draw(screen)
    pass_text_box.draw(screen, True)
    title_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 72)
    massage_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 30)
    hint_in_text = massage_font.render("用户名：", True, (255, 255, 255))
    hint1_in_text = massage_font.render("密 码：", True, (255, 255, 255))
    sign_in_text = title_font.render("登 陆", True, (255, 255, 255))
    screen.blit(hint_in_text, (110, 260))
    screen.blit(hint1_in_text, (110, 360))
    screen.blit(sign_in_text, (150, 150))


def register(screen):
    """
    注册页面函数
    :param screen:
    :return:
    """
    pass_text_box = gl.get_value('pass_text_box')
    name_text_box = gl.get_value('name_text_box')
    again_text_box = gl.get_value('again_text_box')
    name_text_box.draw(screen)
    pass_text_box.draw(screen, True)
    again_text_box.draw(screen, True)
    title_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 72)
    massage_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 30)
    hint_in_text = massage_font.render("用户名：", True, (255, 255, 255))
    hint1_in_text = massage_font.render("登录密码：", True, (255, 255, 255))
    hint2_in_text = massage_font.render("确认密码：", True, (255, 255, 255))
    screen.blit(hint_in_text, (110, 220))
    screen.blit(hint1_in_text, (110, 320))
    screen.blit(hint2_in_text, (110, 420))
    register_text = title_font.render("注 册", True, (255, 255, 255))
    screen.blit(register_text, (150, 100))


def callback():
    print("回车测试")


def draw_board(screen):
    if gl.get_value('isGameStatus') == 'board':
        title_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
        font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 30)

        db = pymysql.connect("localhost", "root", "19971231", "hider")
        cursor = db.cursor()
        sql = "SELECT * FROM board ORDER BY score DESC"
        cursor.execute(sql)
        data = cursor.fetchall()

        title_text = title_font.render("Ranking List", True, (255, 255, 255))
        screen.blit(title_text, (150, 50))
        table_text = font.render("No.      Score      Username", True, (255, 255, 255))
        screen.blit(table_text, (70, 120))
        for i in range(len(data)):
            if i <= 10:
                no_text = font.render(str(i+1)+'.', True, (255, 218, 185))
                screen.blit(no_text, (70, 160 + i * 40))
                score_text = font.render(str(data[i][1]), True, (139, 69, 19))
                screen.blit(score_text, (175, 160 + i * 40))
                name_text = font.render(str(data[i][2]), True, (255, 218, 185))
                screen.blit(name_text, (315, 160 + i * 40))
        db.close()


def game_over(screen):
    """
    游戏结束时触发(二级函数)
    :param screen:
    :return:
    """
    # 最高分
    db = pymysql.connect("localhost", "root", "19971231", "hider")
    cursor = db.cursor()
    sql = "SELECT * FROM board ORDER BY score DESC"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        record_score = data[1]
    else:
        record_score = 0

    # 当前分数
    score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
    score = gl.get_value('score')
    if not gl.get_value('score_save'):
        sql = "INSERT INTO BOARD(score, nickname) VALUES(%d, '%s')" % (score, gl.get_value('username'))
        cursor.execute(sql)
        gl.set_value('score_save', True)
    db.close()
    width = screen.get_rect().width
    height = screen.get_rect().height

    best_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
    screen.blit(best_score_text, (50, 50))

    your_score_text = score_font.render("Your Score", True, (255, 255, 255))
    your_score_text_rect = your_score_text.get_rect()
    your_score_text_rect.left, your_score_text_rect.top = \
        (width - your_score_text_rect.width) // 2, height // 3
    screen.blit(your_score_text, your_score_text_rect)

    your_score = score_font.render(str(score), True, (255, 255, 255))
    your_score_rect = your_score.get_rect()
    your_score_rect.left, your_score_rect.top = \
        (width - your_score_rect.width) // 2, \
        your_score_text_rect.bottom + 10
    screen.blit(your_score, your_score_rect)
    # again_rect = restartBtns['Normal'].get_rect()
    # again_rect.left, again_rect.top = \
    #     (width - again_rect.width) // 2, \
    #     your_score_rect.bottom + 50
    # print(again_rect.left, again_rect.top)


def create_hero(screen):
    hero_name = gl.get_value('hero_name')
    if hero_name == 'tom':
        hero = Tom('tom', Config.get('imgfolder'), screen)
    elif hero_name == 'jerry':
        hero = Jerry('jerry', Config.get('imgfolder'), screen)
    return hero


def game_endless(screen):
    """
    无尽模式(demo模式)(二级函数)(由game_start调用)
    :param screen:
    :return:
    """
    if gl.get_value('isLoadHero') == False:  # 检测初次运行
        hero = create_hero(screen)
        # hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
        gl.set_value('score', 0)
        gl.set_value('isPause', False)
        wall_function(screen, 1, gl.get_value('load_map'))
        enemy_function(screen, 1)
    else:
        wall_function(screen, 2, gl.get_value('load_map'))
        enemy_function(screen, 2)
        hero = gl.get_value('hero')
        hero.blitMe(not gl.get_value('isPause'))
        score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
        score_text = score_font.render("Score : %s" % str(gl.get_value('score')), True, (255, 255, 255))
        screen.blit(score_text, (10, 5))
        check_collide()


def game_start(screen):
    """
    游戏开始函数(一级函数)
    :param screen: 游戏屏幕数据
    """
    gl.set_value('score_save', False)
    if select_hero(screen):
        if gl.get_value('GameMode') == 'endless':
            game_endless(screen)
        elif gl.get_value('GameMode') == 'normal':
            if gl.get_value('load_map'):
                game_map(screen)


def select_hero(screen):
    if gl.get_value('isSelectHero') == False:
        gl.set_value('isGameStatus', 'select_hero')
        return False
    elif gl.get_value('isSelectHero'):
        return True


def game_map(screen):
    """
        Map1特性(二级函数)(由game_start调用)
        :param screen:
        :return:
    """
    if gl.get_value('isLoadHero') == False:  # 检测初次运行
        hero = create_hero(screen)
        # hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
        gl.set_value('score', 0)
        gl.set_value('isPause', False)
        gift_bag = pygame.sprite.Group()
        special_scene = pygame.sprite.Group()
        gl.set_value('gift_bag', gift_bag)
        gl.set_value('special_scene', special_scene)
        wall_function(screen, 1, gl.get_value('load_map'))
        enemy_function(screen, 1)
        special_scene_function(screen)
        gift_function(screen)
    else:
        wall_function(screen, 2, gl.get_value('load_map'))
        special_scene_function(screen)
        gift_function(screen)
        enemy_function(screen, 2)
        hero = gl.get_value('hero')
        hero.blitMe(not gl.get_value('isPause'))
        score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
        score_text = score_font.render("Score : %s" % str(gl.get_value('score')), True, (255, 255, 255))
        screen.blit(score_text, (10, 5))
        check_collide()


def special_scene_function(screen):
    special_scene = gl.get_value('special_scene')
    step = len(special_scene)
    if step == 0:
        index = gl.get_value('load_map')
        if index == 1:
            swamp_function(screen)
        elif index == 2:
            damage_function(screen)
        elif index == 3:
            ice_function(screen)
    elif step != 0:
        draw_group(screen, special_scene)


def ice_function(screen):
    num = 1 + int(gl.get_value('level') / 5)
    special_scene = gl.get_value('special_scene')
    add_star(screen, num, special_scene, 'ice')
    gl.set_value('special_scene', special_scene)


def damage_function(screen):
    num = 1 + int(gl.get_value('level') / 5)
    special_scene = gl.get_value('special_scene')
    add_star(screen, num, special_scene, 'damage')
    gl.set_value('special_scene', special_scene)


def swamp_function(screen):
    num = 1 + int(gl.get_value('level') / 5)
    special_scene = gl.get_value('special_scene')
    add_star(screen, num, special_scene, 'swamp')
    gl.set_value('special_scene', special_scene)


def gift_function(screen):
    gift_bag = gl.get_value('gift_bag')
    step = len(gift_bag)
    if step == 0:
        gift_list = ['health', 'score', 'limit']
        # index = random.randint(0, 2)
        index = 0
        if gift_list[index] == 'health':
            health_function(screen)
        elif gift_list[index] == 'score':
            score_function(screen)
        elif gift_list[index] == 'limit':
            limit_advance_function(screen)
    elif step != 0:
        draw_group(screen, gift_bag)


def limit_advance_function(screen):
    gift_bag = gl.get_value('gift_bag')
    add_star(screen, 1, gift_bag, 'limit')
    gl.set_value('gift_bag', gift_bag)


def health_function(screen):
    """
    处理游戏中障碍物函数(三级函数)(由game_endless调用)
    :param screen:
    :return:
    """
    gift_bag = gl.get_value('gift_bag')
    add_star(screen, 1, gift_bag, 'health')
    gl.set_value('gift_bag', gift_bag)

    # gift_bag = gl.get_value('gift_bag')
    # if len(gift_bag) == 0:
    #     add_star(screen, 1, gift_bag, 'health')
    # draw_group(screen, gift_bag)


def score_function(screen):
    """
    处理游戏中障碍物函数(三级函数)(由game_endless调用)
    :param step:
    :param screen:
    :return:
    """
    gift_bag = gl.get_value('gift_bag')
    add_star(screen, 1, gift_bag, 'score')
    gl.set_value('gift_bag', gift_bag)

    # gift_bag = gl.get_value('gift_bag')
    # if len(gift_bag) == 0:
    #     add_star(screen, 1, gift_bag, 'score')
    # draw_group(screen, gift_bag)


def add_star(screen, num, group, name):
    """
    生成star(二级函数)
    :param screen:
    :param num:
    :param group:
    :param name:
    :return:
    """
    walls = gl.get_value('walls')
    i = 0
    for i in range(num):
        unit = create_star(screen, name)
        while pygame.sprite.spritecollide(unit, walls, False, pygame.sprite.collide_mask):
            unit = create_star(screen, name)
        group.add(unit)


def create_star(screen, name):
    if name == 'health':
        unit = HealthStar(name, Config.get('imgfolder'), screen, gl.get_value('level'))
    elif name == 'score':
        unit = ScoreStar(name, Config.get('imgfolder'), screen, gl.get_value('level'))
    elif name == 'limit':
        unit = LimitStar(name, Config.get('imgfolder'), screen, gl.get_value('level'))
    elif name == 'swamp':
        unit = Swamp(name, Config.get('imgfolder'), screen, gl.get_value('level'))
    elif name == 'damage':
        unit = Damage(name, Config.get('imgfolder'), screen, gl.get_value('level'))
    elif name == 'ice':
        unit = Ice(name, Config.get('imgfolder'), screen, gl.get_value('level'))
    return unit


def check_collide():
    """
    处理游戏中发生的所有碰撞(三级函数)(由game_endless调用)
    :return:
    """
    hero = gl.get_value('hero')
    # rock 与 rocks 之间的碰撞检测
    rocks = gl.get_value('rocks')
    walls = gl.get_value('walls')
    check_enemy_collide(rocks)
    check_enemy_wall_collide(walls, rocks)
    check_hero_wall_collide(hero, walls)
    check_hero_enemy_collide(hero, rocks)
    if gl.get_value('load_map'):
        special_scene = gl.get_value('special_scene')
        check_hero_special_collide(hero, special_scene)
        gift_bag = gl.get_value('gift_bag')
        check_hero_star_collide(hero, gift_bag)
    HP = hero.getHP()
    if HP <= 0:
        over_sound.play()
        gl.set_value('isGameStatus', 'game_over')


def check_hero_special_collide(hero, special_scene):
    collide_flag = pygame.sprite.spritecollide(hero, special_scene, False, pygame.sprite.collide_mask)
    if collide_flag:
        collide_flag[0].enable(hero)
    elif hero.debuff:
        special_scene.sprites()[0].disable(hero)


def check_hero_star_collide(hero, star_group):
    collide_flag = pygame.sprite.spritecollide(hero, star_group, False, pygame.sprite.collide_mask)
    if collide_flag:
        collide_flag[0].enable(hero, gl.get_value('level'))
        star_group.remove(collide_flag[0])


def check_hero_enemy_collide(hero, enemy):
    collide_flag = pygame.sprite.spritecollide(hero, enemy, False, pygame.sprite.collide_mask)
    if collide_flag:
        hero.lifeControler(collide_flag)


def check_hero_wall_collide(hero, walls):
    if gl.get_value('hero_name') == 'tom' and hero.crossFlag:
        hero.set_direct_move_flag('up', False)
        hero.set_direct_move_flag('down', False)
        hero.set_direct_move_flag('right', False)
        hero.set_direct_move_flag('left', False)
    else:
        temp = pygame.sprite.spritecollide(hero, walls, False, pygame.sprite.collide_mask)
        hero.set_direct_move_flag('up', False)
        hero.set_direct_move_flag('down', False)
        hero.set_direct_move_flag('right', False)
        hero.set_direct_move_flag('left', False)
        if temp:
            # print('hit')
            if len(temp) == 1:
                if temp[0].rect.bottom > hero.rect.bottom > temp[0].rect.top and \
                        hero.rect.right > temp[0].rect.right > hero.rect.left:
                    width = abs(temp[0].rect.right - hero.rect.left)
                    height = abs(temp[0].rect.top - hero.rect.bottom)
                    if width > height:
                        hero.set_direct_move_flag('down', True)
                    elif width < height:
                        hero.set_direct_move_flag('left', True)
                elif hero.rect.bottom > temp[0].rect.bottom > hero.rect.top and \
                        hero.rect.right > temp[0].rect.right > hero.rect.left:
                    width = abs(temp[0].rect.right - hero.rect.left)
                    height = abs(temp[0].rect.bottom - hero.rect.top)
                    if width > height:
                        hero.set_direct_move_flag('up', True)
                    elif width < height:
                        hero.set_direct_move_flag('left', True)
                elif hero.rect.right > temp[0].rect.left > hero.rect.left and \
                        hero.rect.bottom > temp[0].rect.bottom > hero.rect.top:
                    width = abs(hero.rect.right - temp[0].rect.left)
                    height = abs(temp[0].rect.bottom - hero.rect.top)
                    if width > height:
                        hero.set_direct_move_flag('up', True)
                    elif width < height:
                        hero.set_direct_move_flag('right', True)
                elif hero.rect.right > temp[0].rect.left > hero.rect.left and \
                        hero.rect.bottom > temp[0].rect.top > hero.rect.top:
                    width = abs(hero.rect.right - temp[0].rect.left)
                    height = abs(hero.rect.bottom - temp[0].rect.top)
                    if width > height:
                        hero.set_direct_move_flag('down', True)
                    elif width < height:
                        hero.set_direct_move_flag('right', True)
            if hero.directMoveFlag.count(1) == 0:
                if hero.rect.bottom > temp[0].rect.top > hero.rect.top and \
                        temp[0].rect.left <= hero.rect.left <= temp[0].rect.right:
                    hero.set_direct_move_flag('down', True)
                elif hero.rect.bottom > temp[0].rect.bottom > hero.rect.top and \
                        temp[0].rect.left <= hero.rect.left <= temp[0].rect.right:
                    hero.set_direct_move_flag('up', True)


def check_enemy_wall_collide(immutable_group, alterable_group):
    """
    碰到墙壁后触发事件
    :param immutable_group: {group} 不可变组
    :param alterable_group: {group} 可变组
    :return:
    """
    # TODO: 这里存在隐藏bug，同时check_enemy_collide中也存在
    # 如果有两处同时发生碰撞，碰撞检测会失效，待解决
    for i in alterable_group.sprites():
        temp = pygame.sprite.spritecollide(i, immutable_group, False, pygame.sprite.collide_mask)
        if temp:
            # print(temp)
            # print('hit')
            if temp[0].rect.bottom > i.rect.bottom > temp[0].rect.top and \
                    i.rect.right > temp[0].rect.right > i.rect.left:
                width = abs(temp[0].rect.right - i.rect.left)
                height = abs(temp[0].rect.top - i.rect.bottom)
                if width > height:
                    i.speed[0] = -i.speed[0]
                    i.rect.top += i.speed[0]
                elif width < height:
                    i.speed[1] = -i.speed[1]
                    i.rect.left += i.speed[1]
            elif i.rect.bottom > temp[0].rect.bottom > i.rect.top and \
                    i.rect.right > temp[0].rect.right > i.rect.left:
                width = abs(temp[0].rect.right - i.rect.left)
                height = abs(temp[0].rect.bottom - i.rect.top)
                if width > height:
                    i.speed[0] = -i.speed[0]
                    i.rect.top += i.speed[0]
                elif width < height:
                    i.speed[1] = -i.speed[1]
                    i.rect.left += i.speed[1]
            elif i.rect.right > temp[0].rect.left > i.rect.left and \
                    i.rect.bottom > temp[0].rect.bottom > i.rect.top:
                width = abs(i.rect.right - temp[0].rect.left)
                height = abs(temp[0].rect.bottom - i.rect.top)
                if width > height:
                    i.speed[0] = -i.speed[0]
                    i.rect.top += i.speed[0]
                elif width < height:
                    i.speed[1] = -i.speed[1]
                    i.rect.left += i.speed[1]
            elif i.rect.right > temp[0].rect.left > i.rect.left and \
                    i.rect.bottom > temp[0].rect.top > i.rect.top:
                width = abs(i.rect.right - temp[0].rect.left)
                height = abs(i.rect.bottom - temp[0].rect.top)
                if width > height:
                    i.speed[0] = -i.speed[0]
                    i.rect.top += i.speed[0]
                elif width < height:
                    i.speed[1] = -i.speed[1]
                    i.rect.left += i.speed[1]
            else:
                if i.rect.bottom > temp[0].rect.top > i.rect.top or\
                        i.rect.bottom > temp[0].rect.bottom > i.rect.top:
                    # 上下面发生碰撞
                    i.speed[0] = -i.speed[0]
                    if i.speed[0] > 0:      # 防止出现持久碰撞事件
                        i.rect.top += i.speed[0]
                elif i.rect.right > temp[0].rect.left > i.rect.left or\
                        i.rect.right > temp[0].rect.right > i.rect.left:
                    # 左右面发生碰撞
                    i.speed[1] = -i.speed[1]


def check_enemy_collide(group):
    """
    处理游戏中，enemy类元素的碰撞事件(四级函数)(由check_collide调用)
    防止重复对于发生碰撞的精灵重复计算
    :param group: {sprite.Group} enemy类精灵组
    :return:
    """
    collide_list = []  # 存放发生碰撞的精灵组
    # 清点发生碰撞的精灵
    for i in group.sprites():
        if i.isCollide == False:  # 碰撞标志位为False，表名未发生碰撞
            group.remove(i)
            temp = pygame.sprite.spritecollide(i, group, False, pygame.sprite.collide_mask)
            if temp:
                temp[0].isCollide = True
                i.isCollide = True
                collide_list.append(i)
                collide_list.append(temp[0])
            group.add(i)
    if len(collide_list) != 0:
        # print(len(collide_list))
        # stop = input()
        collide_list[0].speed, collide_list[1].speed = collide_list[1].speed, collide_list[0].speed
        collide_list[0].isCollide = False
        collide_list[1].isCollide = False


def wall_function(screen, flag, load_map):
    """
    处理游戏中障碍物函数(三级函数)(由game_endless调用)
    :param screen:
    :param flag:
    :return:
    """
    if load_map == 0:
        name = 'wall'
    elif load_map == 1:
        name = 'grass'
    elif load_map == 2:
        name = 'pool'
    elif load_map == 3:
        name = 'stone'

    if flag == 1:
        walls = pygame.sprite.Group()
        add_wall(screen, walls, name)
        gl.set_value('walls', walls)
    elif flag == 2:
        walls = gl.get_value('walls')
        if len(walls) == 0:
            game_upgrade()
            add_wall(screen, walls, name)
        draw_group(screen, walls)


def game_upgrade():
    new_level = gl.get_value('level') + 1
    bg = gl.get_value('background')
    gl.set_value('level', new_level)
    hero = gl.get_value('hero')
    hero.upgrade(new_level)
    bg[gl.get_value('load_map')].upgrade(new_level)


def add_wall(screen, group, name):
    tmp = 0
    for i in range(30):
        if i % 3 == 1:
            null = random.randint(0, 120) % 5
            if null == tmp:
                if null == 5:
                    null -= 1
                else:
                    null += 1
            tmp = null
            for j in range(6):
                if j != null and j != null + 1:
                    unit = Wall(screen, Config.get('imgfolder'), name, (j * 80, -i * 80), gl.get_value('level'))
                    group.add(unit)


def enemy_function(screen, step):
    """
    管理敌人的行动，清除越界部分(三级函数)(由game_endless调用)
    :param screen:
    :param step: {int}为1时为创建group，为2时为绘制group
    :return:
    """
    if step == 1:
        rocks = pygame.sprite.Group()
        add_enemy(screen, 10, rocks, 'rock', 10)
        gl.set_value('rocks', rocks)
    elif step == 2:
        rocks = gl.get_value('rocks')
        # print(len(rocks))
        if len(rocks) == 0:
            add_enemy(screen, 10, rocks, 'rock', 10)
        draw_group(screen, rocks)


def add_enemy(screen, num, group, name, damage):
    """
    将具有伤害的精灵添加进精灵组(二级函数)
    :param damage: 单个伤害
    :param group:{group}石组
    :param num:{int}石块数量
    :param screen:{screen}游戏屏幕数据
    :param name:{str}文件名
    :param score: {int}分数信息
    :return:
    """
    walls = gl.get_value('walls')
    i = 0
    for i in range(num):
        unit = Enemy(name, Config.get('imgfolder'), screen, damage, gl.get_value('level'))
        while pygame.sprite.spritecollide(unit, group, False, pygame.sprite.collide_mask) or \
                pygame.sprite.spritecollide(unit, walls, False, pygame.sprite.collide_mask):
            unit = Enemy(name, Config.get('imgfolder'), screen, damage, gl.get_value('level'))
        group.add(unit)


def draw_group(screen, group):
    """
    描绘精灵组(二级函数)
    :param group: {group}精灵组
    :param screen: {screen}屏幕信息
    """
    for item in group:
        if item.rect.top >= screen.get_rect().height:
            # 该单位位于窗口下方时，清除单位，增加相应的分数
            group.remove(item)
            temp = gl.get_value('score')
            score = item.score
            gl.set_value('score', temp + score)

        item.blitMe(not gl.get_value('isPause'))


def draw_button(screen, Btns):
    """
    描绘按钮(一级函数)
    :param screen:{screen}屏幕信息
    :param Btns:{dic}按钮
    """
    key_word = gl.get_value('isGameStatus')
    if key_word == 'start':
        Btns['register'].draw(screen)
        Btns['sign_in'].draw(screen)
        Btns['quit'].draw(screen)
        Btns['rank'].draw(screen)
        if gl.get_value('bgm'):
            Btns['sound_on'].draw(screen)
        else:
            Btns['sound_off'].draw(screen)
    elif key_word == 'sign_in':
        Btns['sign_in_check'].draw(screen)
        Btns['back'].draw(screen)
        if gl.get_value('bgm'):
            Btns['sound_on'].draw(screen)
        else:
            Btns['sound_off'].draw(screen)
    elif key_word == 'menu':
        Btns['start'].draw(screen)
        Btns['endless'].draw(screen)
        Btns['log_out'].draw(screen)
        Btns['rank'].draw(screen)
        if gl.get_value('bgm'):
            Btns['sound_on'].draw(screen)
        else:
            Btns['sound_off'].draw(screen)
    elif key_word == 'game_start':
        if gl.get_value('isPause') == False:
            Btns['pause'].draw(screen)
        elif gl.get_value('isPause'):
            Btns['resume'].draw(screen)
            Btns['back1'].draw(screen)
    elif key_word == 'game_over':
        Btns['restart'].draw(screen)
        Btns['back1'].draw(screen)
        Btns['rank'].draw(screen)
    elif key_word == 'game_map_select':
        Btns['Map1'].draw(screen)
        Btns['Map2'].draw(screen)
        Btns['Map3'].draw(screen)
        Btns['rank'].draw(screen)
        Btns['back'].draw(screen)
        if gl.get_value('bgm'):
            Btns['sound_on'].draw(screen)
        else:
            Btns['sound_off'].draw(screen)
    elif key_word == 'select_hero':
        Btns['tom'].draw(screen)
        Btns['jerry'].draw(screen)
        Btns['back'].draw(screen)
        if gl.get_value('bgm'):
            Btns['sound_on'].draw(screen)
        else:
            Btns['sound_off'].draw(screen)
    elif key_word == 'register':
        Btns['register_check'].draw(screen)
        Btns['back'].draw(screen)
        if gl.get_value('bgm'):
            Btns['sound_on'].draw(screen)
        else:
            Btns['sound_off'].draw(screen)
    elif key_word == 'board':
        Btns['back'].draw(screen)
