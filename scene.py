import pygame

pygame.init()


class Scene_Manager:
    def __init__(self, screen_size=(800, 600), screen_caption='new scene', FPS=60):
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(screen_caption)
        self.clock = pygame.time.Clock()

        self.game_run = True
        self.FPS = FPS

        self.scene_list = {}
        self.scenes = None

    def set_screen_size(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    def set_screen_caption(self, caption):
        pygame.display.set_caption(caption)

    def set_FPS(self, FPS):
        self.FPS = FPS

    def add_scene(self, scene_name, scene_class):
        self.scene_list[scene_name] = scene_class

    def set_scene(self, scene_name, **kwargs):
        self.scenes = self.scene_list[scene_name](self, **kwargs)

    def run_scene(self):
        self.scenes.run_game()
