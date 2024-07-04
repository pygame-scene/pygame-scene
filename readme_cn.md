# Pygame Scene Switcher

Pygame Scene Switcher 是一个用于管理和切换Pygame游戏场景的工具。它提供了一个灵活的框架，允许开发者在不同的游戏界面之间轻松切换，从而促进复杂Pygame游戏的开发。

## 特点

- **模块化设计**：将游戏分解为独立的模块或场景，便于管理和扩展。
- **易于使用**：通过简单的API添加和切换场景。
- **灵活配置**：支持自定义屏幕大小、标题和帧率。
- **事件驱动**：内置事件处理机制，响应用户输入和系统事件。

## 系统要求

- Python (推荐使用Python 3.x)
- Pygame 库

## 安装

Pygame Scene Switcher 需要Python环境和Pygame库。安装Pygame的步骤如下：

```bash
pip install pygame
```

## 使用方法

1. **初始化场景管理器**：
   
   ```python
   Scene_Manager = Scene_Manager()  
   ```

2. **添加场景**：
   
   ```python
   Scene_Manager.add_scene('main', MainScreen)
   ```
   
   

3. **设置并运行场景**：
   
   ```python
   Scene_Manager.set_scene('main')
   Scene_Manager.run_scene()
   ```

# 示例场景

以下是一个简单的主屏幕场景示例：

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
    Scene_Manager.set_scene('main', a='main')  # 命名参数必须和类内 kwargs.get 方法访问时使用的键名称一致
    Scene_Manager.run_scene()
```

# 联系我们

如果您有任何问题或需要技术支持，请通过以下方式联系我们：

* 电子邮件：[a3305587173@outlook.com](mailto:a3305587173@outlook.com)
* 官方网站：[yang208115.github.io](yang208115.github.io)
