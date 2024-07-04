# Pygame Scene Switcher

Pygame Scene Switcher is a tool for managing and switching scenes in Pygame games. It provides a flexible framework that allows developers to easily switch between different game interfaces, thereby facilitating the development of complex Pygame games.

## Features

- **Modular Design**：The game is broken down into independent modules or scenes, which facilitates management and expansion.
- **Easy to Use**: Scenes can be added and switched through a simple API.
- **Flexible Configuration**: Supports custom screen size, title, and frame rate.
- **Event-Driven**: Built-in event handling mechanism to respond to user input and system events.

## System Requirements

- Python (Python 3.x is recommended)
- Pygame library

## Installation

Pygame Scene Switcher requires a Python environment and the Pygame library. To install Pygame, follow these steps:

```bash
pip install pygame
```

## Usage

1. **Initialize the Scene Manager**:
   
   ```python
   Scene_Manager = Scene_Manager()  
   ```

2. **Add a Scene**：
   
   ```python
   Scene_Manager.add_scene('main', MainScreen)
   ```
   
   

3. **Set and Run the Scene**：
   
   ```python
   Scene_Manager.set_scene('main')
   Scene_Manager.run_scene()
   ```

# Example Scene

Here is a simple example of a main screen scene:

```python
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
    Scene_Manager.set_scene('main', a='main')  # The named argument must match the key name used to access it with the "kwargs.get" method inside the class.
    Scene_Manager.run_scene()
```

# Contact Us

If you have any questions or need technical support, please contact us through the following methods:

* Email：[a3305587173@outlook.com](mailto:a3305587173@outlook.com)
* Official Website：[yang208115.github.io](yang208115.github.io)
