import pygame
from Img_class import Img


class FarmGame:
    def __init__(self):
#         1. 게임 초기화
        pygame.init()
        pygame.display.init()
    def setting(self):
#         2. 게임창 옵션 설정
        size = [400, 400]
        self.screen = pygame.display.set_mode(size)

        title = "my game"
        pygame.display.set_caption(title)

        # 3. 게임 내 필요한 설정
        self.clock = pygame.time.Clock()
        self.run = True

    #     3-1) 배경 설정하기 (2way)
        self.background = Img()
        self.background.put_img("_background.png")
        self.background.change_img(size[0], size[1])

    def running(self):
    #         4. 메인이벤트
            while self.run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
    #                 4-4) 그리기
                self.background.show(self.screen)


                    # 4-5) 업데이트
                pygame.display.flip()


    def quit(self):
#         5. 게임 종료
        pygame.quit()


def main():
    mygame = FarmGame()
    mygame.setting()
    mygame.running()
    mygame.quit()

if __name__=="__main__":
    main()