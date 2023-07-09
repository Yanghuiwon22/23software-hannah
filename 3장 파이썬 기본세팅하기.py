import pygame
from test import Obj

class FarmGame:
    def __init__(self):
        # 1. 게임 초기화
        pygame.init()
        pygame.display.init()

    def running(self):
        # 4. 메인 이벤트
        while self.SB == 0:
            # 4-1) FPS
            self.clock.tick(60)
            # 4-2) 각종 입력 방지
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SB = 1
            # 4-4) 그리기
            self.screen.fill(self.color)
            self.ss.showself(self.screen)

            # 4-5) 업데이트
            pygame.display.flip()

    def setting(self):
        # 2. 게임창 옵션 설정
        size = [400, 900]
        self.screen = pygame.display.set_mode(size)

        title = "my game"
        pygame.display.set_caption(title)

        # 3. 게임 내 필요한 설정
        self.clock = pygame.time.Clock()
        self.SB = 0
        color = (255, 0, 0)

        self.ss = Obj()
        self.ss.put_img("_ss.png")
        self.ss.change_img(50, 80)

    def quit(self):
        # 5. 게임 종료
        pygame.quit()

def main(self):
    mygame = FarmGame()
    mygame.setting()
    mygame.running()
    mygame.quit()

if __name__=="__main__":
    main()
