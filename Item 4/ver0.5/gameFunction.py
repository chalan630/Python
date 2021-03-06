'''
@Descripttion: 游戏函数
@version: ver0.5
@Author: chalan630
@Date: 2020-03-02 23:37:29
@LastEditTime: 2020-03-24 23:01:55
'''
import pygame
import sys
import gameFlag as gl
from hero import Hero
from config import Config
from enemy import Enemy
from textbox import TextBox

# TODO: 1.游戏暂停功能bug修复 √
# TODO: 2.游戏人物死亡后重置游戏 √
# TODO: 3.石块之间的碰撞检测
# TODO: 4.生命值系统 √
# TODO: 5.开始界面方向键报错

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
    elif gl.get_value('isGameStatus') == 'game_start':
        hero = gl.get_value('hero')
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
                    if key == 'register' or key == 'sign_in' or key == 'quit':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'sign_in':
                    if key == 'sign_in_check':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'menu':
                    if key == 'start' or key == 'log_out':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_start':
                    if key == 'pause' and gl.get_value('isPause') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'resume' and gl.get_value('isPause') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_over':
                    if key == 'restart':
                        Btns[key].getFocus(mx, my)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键
                for key in Btns:
                    if gl.get_value('isGameStatus') == 'start':
                        if key == 'register' or key == 'sign_in' or key == 'quit':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'sign_in':
                        if key == 'sign_in_check':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'menu':
                        if key == 'start' or key == 'log_out':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_start':
                        if key == 'pause' and gl.get_value('isPause') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'resume' and gl.get_value('isPause') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_over':
                        if key == 'restart':
                            Btns[key].mouseDown(mx, my)

        elif event.type == pygame.MOUSEBUTTONUP:
            for key in Btns:
                if gl.get_value('isGameStatus') == 'start':
                    if key == 'register' or key == 'sign_in' or key == 'quit':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'sign_in':
                    if key == 'sign_in_check':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'menu':
                    if key == 'start' or key == 'log_out':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_start':
                    if key == 'pause' and gl.get_value('isPause') == False:
                        Btns[key].mouseUp()
                    elif key == 'resume' and gl.get_value('isPause') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_over':
                    if key == 'restart':
                        Btns[key].mouseUp()


def btn_start():
    """
    开始按钮按下时触发函数(二级函数)
    :return:
    """
    print("我被按下了")
    gl.set_value('isGameStatus', 'game_start')


def btn_quit():
    """
    退出按钮按下时触发函数(二级函数)
    :return:
    """
    print('See you next time!')
    sys.exit()


def btn_pause():
    """
    切换暂停状态(三级函数)
    :return:
    """
    if gl.get_value('isPause'):
        gl.set_value('isPause', False)
    else:
        gl.set_value('isPause', True)


def btn_restart():
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('isLoadHero', False)
    print("再来一次")


def btn_log_out():
    gl.set_value('isGameStatus', 'start')


def btn_sign_in():
    gl.set_value('isGameStatus', 'sign_in')
    font = pygame.font.Font(Config.get('fontfolder') + 'pf.ttf', 36)
    name_text_box = TextBox(250, 50, 112, 300, font, callback=callback)
    pass_text_box = TextBox(250, 50, 112, 400, font, callback=callback)
    gl.set_value('name_text_box', name_text_box)
    gl.set_value('pass_text_box', pass_text_box)
    print('sign_in')


def btn_sign_in_check():
    pass_text_box = gl.get_value('pass_text_box')
    name_text_box = gl.get_value('name_text_box')
    password = pass_text_box.get_text()
    username = name_text_box.get_text()
    with open('user.txt', 'r') as f:
        r_username, r_password = f.readline().split('/')
    if r_username == username and r_password == password:
        gl.set_value('error_type', 0)
        gl.set_value('isGameStatus', 'menu')
    else:
        gl.set_value('error_type', 1)
        pass_text_box.clean_text()
        name_text_box.clean_text()


def btn_register():
    print('register')


def error_message(screen):
    num = gl.get_value('error_type')
    if num == 1:
        title_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 16)
        sign_in_text = title_font.render("用户名或密码错误", True, (255, 255, 255))
        screen.blit(sign_in_text, (112, 270))


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
    sign_in_text = title_font.render("登 陆", True, (255, 255, 255))
    screen.blit(sign_in_text, (150, 150))


def callback():
    print("回车测试")


def game_over(screen):
    """
    游戏结束时触发(二级函数)
    :param screen:
    :return:
    """
    score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
    score = gl.get_value('score')
    record_score = 0
    with open("record.txt", "r") as f:
        record_score = int(f.read())
    if gl.get_value('score') > record_score:
        with open("record.txt", "w") as f:
            f.write(str(gl.get_value('score')))

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


def game_start(screen, Btns):
    """
    游戏开始函数(一级函数)
    :param screen: 游戏屏幕数据
    """
    if gl.get_value('isLoadHero') == False:  # 检测初次运行
        hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
        gl.set_value('score', 0)
        gl.set_value('isPause', False)
        enemy_function(screen, 1)
    else:
        hero = gl.get_value('hero')
        hero.blitMe(not gl.get_value('isPause'))
        score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
        score_text = score_font.render("Score : %s" % str(gl.get_value('score')), True, (255, 255, 255))
        screen.blit(score_text, (10, 5))
        enemy_function(screen, 2)
        check_collide()


def check_collide():
    hero = gl.get_value('hero')
    rocks = gl.get_value('rocks')
    collide_flag = pygame.sprite.spritecollide(hero, rocks, False, pygame.sprite.collide_mask)
    is_alive = hero.lifeControler(collide_flag)
    if not is_alive:
        gl.set_value('isGameStatus', 'game_over')


def enemy_function(screen, step):
    if step == 1:
        rocks = pygame.sprite.Group()
        add_group(screen, 20, rocks, 'rock', 10, 0)
        gl.set_value('rocks', rocks)
    elif step == 2:
        rocks = gl.get_value('rocks')
        if len(rocks) == 0:
            add_group(screen, 20, rocks, 'rock', 10, 1)
        draw_group(screen, rocks)


def add_group(screen, num, group, name, score, levelUP):
    """
    将something添加进精灵组(二级函数)
    :param group:{group}石组
    :param num:{int}石块数量
    :param screen:{screen}游戏屏幕数据
    :param name:{str}文件名
    :param score: {int}分数信息
    :return:
    """
    i = 0
    for i in range(num):
        unit = Enemy(name, Config.get('imgfolder'), screen, score)
        if levelUP == 1:
            unit.levelUp()
        group.add(unit)


def draw_group(screen, group):
    """
    描绘精灵组(二级函数)
    :param group: {group}精灵组
    :param screen: {screen}屏幕信息
    """
    for item in group:
        if item.rect.bottom >= screen.get_rect().height:
            group.remove(item)
            # 计算分数
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
    if gl.get_value('isGameStatus') == 'start':
        Btns['register'].draw(screen)
        Btns['sign_in'].draw(screen)
        Btns['quit'].draw(screen)
    elif gl.get_value('isGameStatus') == 'sign_in':
        Btns['sign_in_check'].draw(screen)
    elif gl.get_value('isGameStatus') == 'menu':
        Btns['start'].draw(screen)
        Btns['log_out'].draw(screen)
    elif gl.get_value('isGameStatus') == 'game_start':
        if gl.get_value('isPause') == False:
            Btns['pause'].draw(screen)
        elif gl.get_value('isPause'):
            Btns['resume'].draw(screen)
    elif gl.get_value('isGameStatus') == 'game_over':
        Btns['restart'].draw(screen)
