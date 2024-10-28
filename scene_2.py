import pygame
import sys

from threading import Thread

pygame.init()


class Scene_Manager_2:
    def __init__(self, screen_size=(800, 600), screen_caption='new scene', FPS=60):
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(screen_caption)
        self.clock = pygame.time.Clock()

        self.game_run = True
        self.FPS = FPS

        self.scene_list = {}
        self.scenes = None

        global scene_status
        scene_status = 'None'

        t = Thread(target=self.run_scene)
        t.start()


    def stop_game(self):
        self.game_run = False
        sys.exit()

    def set_screen_size(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    def set_screen_caption(self, caption):
        pygame.display.set_caption(caption)

    def set_FPS(self, FPS):
        """
        设置FPS
        :param FPS: 帧率
        :return:
        """
        self.FPS = FPS

    def add_scene(self, scene_name, scene_class):
        """
        添加场景
        :param scene_name:
        :param scene_class:
        :return:
        """
        self.scene_list[scene_name] = scene_class

    def set_scene(self, scene_name, **kwargs):
        """
        设置场景
        :param scene_name: 场景名称
        :param kwargs:
        """
        self.scenes = self.scene_list[scene_name](self, **kwargs)

    def run_scene(self):
        """
        调用场景运行
        """
        global scene_status
        while self.game_run:
            if scene_status == 'next':
                self.scenes.run_game()
                scene_status = 'None'

