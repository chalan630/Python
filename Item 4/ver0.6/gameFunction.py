'''
@Descripttion: 游戏函数
@version: ver0.6
@Author: chalan630
@Date: 2020-03-02 23:37:29
@LastEditTime: 2020-04-21 16:16:47
'''
import pygame
import sys
import random
import gameFlag as gl
from hero import Hero
from config import Config
from enemy import Enemy
from wall import Wall
from healthStar import HealthStar


# TODO: 1.游戏暂停功能bug修复 √
# TODO: 2.游戏人物死亡后重置游戏 √
# TODO: 3.石块之间的碰撞检测 √
# TODO: 4.生命值系统
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
                    if key == 'start' or key == 'log_out' or key == 'endless':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_start':
                    if key == 'pause' and gl.get_value('isPause') == False:
                        Btns[key].getFocus(mx, my)
                    elif key == 'resume' and gl.get_value('isPause') == True:
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_over':
                    if key == 'restart':
                        Btns[key].getFocus(mx, my)
                elif gl.get_value('isGameStatus') == 'game_map_select':
                    if key == 'Map1' or key == 'Map2' or key == 'Map3':
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
                        if key == 'start' or key == 'log_out' or key == 'endless':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_start':
                        if key == 'pause' and gl.get_value('isPause') == False:
                            Btns[key].mouseDown(mx, my)
                        elif key == 'resume' and gl.get_value('isPause') == True:
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_over':
                        if key == 'restart':
                            Btns[key].mouseDown(mx, my)
                    elif gl.get_value('isGameStatus') == 'game_map_select':
                        if key == 'Map1' or key == 'Map2' or key == 'Map3':
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
                    if key == 'start' or key == 'log_out' or key == 'endless':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_start':
                    if key == 'pause' and gl.get_value('isPause') == False:
                        Btns[key].mouseUp()
                    elif key == 'resume' and gl.get_value('isPause') == True:
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_over':
                    if key == 'restart':
                        Btns[key].mouseUp()
                elif gl.get_value('isGameStatus') == 'game_map_select':
                    if key == 'Map1' or key == 'Map2' or key == 'Map3':
                        Btns[key].mouseUp()


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


def game_endless(screen):
    """
    无尽模式(demo模式)(二级函数)(由game_start调用)
    :param screen:
    :return:
    """
    if gl.get_value('isLoadHero') == False:  # 检测初次运行
        hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
        gl.set_value('score', 0)
        gl.set_value('isPause', False)
        wall_function(screen, 1)
        enemy_function(screen, 1)
    else:
        wall_function(screen, 2)
        enemy_function(screen, 2)
        hero = gl.get_value('hero')
        hero.blitMe(not gl.get_value('isPause'), gl.get_value('level'))
        score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
        score_text = score_font.render("Score : %s" % str(gl.get_value('score')), True, (255, 255, 255))
        screen.blit(score_text, (10, 5))
        check_collide()


def game_start(screen):
    """
    游戏开始函数(一级函数)
    :param screen: 游戏屏幕数据
    """
    if gl.get_value('GameMode') == 'endless':
        game_endless(screen)
    elif gl.get_value('GameMode') == 'normal':
        if gl.get_value('load_map') == 1:
            game_map1(screen)


def game_map1(screen):
    """
        Map1特性(二级函数)(由game_start调用)
        :param screen:
        :return:
    """
    if gl.get_value('isLoadHero') == False:  # 检测初次运行
        hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
        gl.set_value('score', 0)
        gl.set_value('isPause', False)
        wall_function(screen, 1)
        enemy_function(screen, 1)
        health_function(screen, 1)
    else:
        wall_function(screen, 2)
        enemy_function(screen, 2)
        health_function(screen, 2)
        hero = gl.get_value('hero')
        hero.blitMe(not gl.get_value('isPause'), gl.get_value('level'))
        score_font = pygame.font.Font(Config.get('fontfolder') + 'text.ttf', 36)
        score_text = score_font.render("Score : %s" % str(gl.get_value('score')), True, (255, 255, 255))
        screen.blit(score_text, (10, 5))
        check_collide()


def health_function(screen, step):
    """
    处理游戏中障碍物函数(三级函数)(由game_endless调用)
    :param screen:
    :param flag:
    :return:
    """
    if step == 1:
        health_bag = pygame.sprite.Group()
        add_star(screen, 1, health_bag, 'health', 10)
        gl.set_value('health_bag', health_bag)
    elif step == 2:
        health_bag = gl.get_value('health_bag')
        if len(health_bag) == 0:
            add_star(screen, 1, health_bag, 'health', 10)
        draw_group(screen, health_bag)


def add_star(screen, num, group, name, value):
    """
    生成star(二级函数)
    :param value:
    :param screen:
    :param num:
    :param group:
    :param name:
    :return:
    """
    walls = gl.get_value('walls')
    i = 0
    for i in range(num):
        unit = HealthStar(name, Config.get('imgfolder'), screen, value, gl.get_value('level'))
        while pygame.sprite.spritecollide(unit, group, False, pygame.sprite.collide_mask) or \
                pygame.sprite.spritecollide(unit, walls, False, pygame.sprite.collide_mask):
            unit = HealthStar(name, Config.get('imgfolder'), screen, value, gl.get_value('level'))
        group.add(unit)


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
    if gl.get_value('load_map') == 1:
        health_bag = gl.get_value('health_bag')
        check_hero_star_collide(hero, health_bag)
    HP = hero.getHP()
    if HP < 0:
        gl.set_value('isGameStatus', 'game_over')


def check_hero_star_collide(hero, star_group):
    collide_flag = pygame.sprite.spritecollide(hero, star_group, False, pygame.sprite.collide_mask)
    if collide_flag:
        collide_flag[0].health(hero)
        star_group.remove(collide_flag[0])


def check_hero_enemy_collide(hero, enemy):
    collide_flag = pygame.sprite.spritecollide(hero, enemy, False, pygame.sprite.collide_mask)
    if collide_flag:
        hero.lifeControler(collide_flag)


def check_hero_wall_collide(hero, walls):
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


def wall_function(screen, flag):
    """
    处理游戏中障碍物函数(三级函数)(由game_endless调用)
    :param screen:
    :param flag:
    :return:
    """
    if flag == 1:
        walls = pygame.sprite.Group()
        add_wall(screen, walls)
        gl.set_value('walls', walls)
    elif flag == 2:
        walls = gl.get_value('walls')
        if len(walls) == 0:
            gl.set_value('level', gl.get_value('level') + 0.1)
            add_wall(screen, walls)
        draw_group(screen, walls)


def add_wall(screen, group):
    tmp = 0
    for i in range(5):
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
                    unit = Wall(screen, Config.get('imgfolder'), (j * 80, -i * 80), 10)
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
        add_enemy(screen, 10, rocks, 'rock', 10, 10)
        gl.set_value('rocks', rocks)
    elif step == 2:
        rocks = gl.get_value('rocks')
        if len(rocks) == 0:
            add_enemy(screen, 10, rocks, 'rock', 10, 10)
        draw_group(screen, rocks)


def add_enemy(screen, num, group, name, score, damage):
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
        unit = Enemy(name, Config.get('imgfolder'), screen, score, damage, gl.get_value('level'))
        while pygame.sprite.spritecollide(unit, group, False, pygame.sprite.collide_mask) or \
                pygame.sprite.spritecollide(unit, walls, False, pygame.sprite.collide_mask):
            unit = Enemy(name, Config.get('imgfolder'), screen, score, damage, gl.get_value('level'))
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
    if gl.get_value('isGameStatus') == 'start':
        Btns['register'].draw(screen)
        Btns['sign_in'].draw(screen)
        Btns['quit'].draw(screen)
    elif gl.get_value('isGameStatus') == 'sign_in':
        Btns['sign_in_check'].draw(screen)
    elif gl.get_value('isGameStatus') == 'menu':
        Btns['start'].draw(screen)
        Btns['endless'].draw(screen)
        Btns['log_out'].draw(screen)
    elif gl.get_value('isGameStatus') == 'game_start':
        if gl.get_value('isPause') == False:
            Btns['pause'].draw(screen)
        elif gl.get_value('isPause'):
            Btns['resume'].draw(screen)
    elif gl.get_value('isGameStatus') == 'game_over':
        Btns['restart'].draw(screen)
    elif gl.get_value('isGameStatus') == 'game_map_select':
        Btns['Map1'].draw(screen)
        Btns['Map2'].draw(screen)
        Btns['Map3'].draw(screen)
