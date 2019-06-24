import pygame
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)

class MainGame():
    window = None
    def __init__(self):
        pass

    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption("坦克大战1.03")

        while True:
            # 给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            pygame.display.update()

    def endGame(self):
        print("谢谢使用，欢迎再次使用")
        exit()

    # 左上角文字的绘制
    def getTextSurface(self):
        pygame.font.init()
        # 获取文字信息
        # print(pygame.font.get_fonts())
        font = pygame.font.Sysfont('georgia', 18)

    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        for event in eventList:
            # 判断按下的键是关闭还是键盘按下
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.KEYDOWN:
                # 判断按下的是上/下/左/右
                if event.key == pygame.K_LEFT:
                    print("按下左键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:
                    print("按下右键，坦克向右移动")
                elif event.key == pygame.K_UP:
                    print("按下上键，坦克向上移动")
                elif event.key == pygame.K_DOWN:
                    print("按下下键，坦克向下移动")




class Tank():
    def __init__(self):
        pass

    def move(self):
        pass

    def shot(self):
        pass

    def displayTank(self):
        pass

class MyTank(Tank):
    def __init__(self):
        pass

class EnemyTank(Tank):
    def __init__(self):
        pass

class Bullet():
    def __init__(self):
        pass

    def move(self):
        pass

    def displayBullet(self):
        pass

class Wall():
    def __init__(self):
        pass

    def displayWll(self):
        pass

class Explode():
    def __init__(self):
        pass

    def displayExplode(self):
        pass

class Music():
    def __init__(self):
        pass

    def play(self):
        pass

if __name__ == "__main__":
    # MainGame().startGame()
    MainGame().getTextSurface()