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
```

# Contact Us

If you have any questions or need technical support, please contact us through the following methods:

* Email：[a3305587173@outlook.com](mailto:a3305587173@outlook.com)
* Official Website：[yang208115.github.io](yang208115.github.io)
