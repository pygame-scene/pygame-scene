# coding=gbk
# -*- coding: utf-8 -*-
import pygame
import time
import sys
import os

import scene

pygame.init()
pygame.mixer.init()


class MainScreen:
    def __init__(self, scene):
        self.scene = scene
        self.scene.set_screen_size(800, 600)
        self.scene.set_screen_caption('test')
        self.screen = self.scene.screen
        self.clock = self.scene.clock
        self.FPS = self.scene.FPS

    def run_game(self):
        while self.scene.game_run:
            self.screen.fill((135, 180, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    Scene_Manager = scene.Scene_Manager()
    Scene_Manager.add_scene('main', MainScreen)
    print(Scene_Manager.scene_list)
    Scene_Manager.set_scene('main')
    Scene_Manager.run_scene()
