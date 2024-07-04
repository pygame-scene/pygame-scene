# coding=gbk
# -*- coding: utf-8 -*-
import pygame
import sys

import scene

pygame.init()


class MainScreen:
    def __init__(self, scene, **kwargs):
        self.scene = scene
        self.a = kwargs.get('a')
        self.scene.set_screen_size(800, 600)
        self.scene.set_screen_caption('test')
        self.screen = self.scene.screen
        self.clock = self.scene.clock
        self.FPS = self.scene.FPS
        self.start = pygame.image.load('start.png')

    def run_game(self):
        while self.scene.game_run:
            self.screen.fill((135, 180, 255))
            self.screen.blit(self.start, (400, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 400 < pos[0] < 400 + 50 and 300 < pos[1] < 300 + 50:
                        print(self.a)
                        self.scene.set_scene('game', a='game')
                        self.scene.run_scene()

            pygame.display.update()
            self.clock.tick(self.FPS)


class GameScreen:
    def __init__(self, scene, **kwargs):
        self.scene = scene
        self.a = kwargs.get('a')
        self.scene.set_screen_size(800, 600)
        self.scene.set_screen_caption('game')
        self.screen = self.scene.screen
        self.clock = self.scene.clock
        self.FPS = self.scene.FPS
        self.return_img = pygame.image.load('return.png')

    def run_game(self):
        while self.scene.game_run:
            self.screen.fill((135, 180, 255))
            self.screen.blit(self.return_img, (400, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 400 < pos[0] < 400 + 50 and 300 < pos[1] < 300 + 50:
                        print(self.a)
                        self.scene.set_scene('main', a='main')
                        self.scene.run_scene()

            pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    Scene_Manager = scene.Scene_Manager()
    Scene_Manager.add_scene('main', MainScreen)
    Scene_Manager.add_scene('game', GameScreen)
    # print(Scene_Manager.scene_list)
    Scene_Manager.set_scene('main', a='main')  # 命名参数必须和类内 kwargs.get 方法访问时使用的键名称一致
    Scene_Manager.run_scene()
