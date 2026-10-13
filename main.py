from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
import math

class CyberRadarWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        Clock.schedule_interval(self.animate, 1/60)

    def update_graphics(self, *args):
        self.canvas.clear()
        cx, cy = self.center_x, self.center_y
        radius = min(self.width, self.height) * 0.4

        with self.canvas:
            Color(0, 1, 0.8, 0.3)
            Line(circle=(cx, cy, radius), width=1.5)
            Line(circle=(cx, cy, radius * 0.7), width=1)
            Line(circle=(cx, cy, radius * 0.4), width=1)

            Color(0, 1, 0.8, 0.2)
            Line(points=[cx - radius, cy, cx + radius, cy], width=1)
            Line(points=[cx, cy - radius, cx, cy + radius], width=1)

            Color(0, 1, 0.8, 1)
            Ellipse(pos=(cx - 4, cy - 4), size=(8, 8))

            rad = math.radians(self.angle)
            lx = cx + radius * math.cos(rad)
            ly = cy + radius * math.sin(rad)
            Color(0, 1, 0.5, 0.9)
            Line(points=[cx, cy, lx, ly], width=2)

    def animate(self, dt):
        self.angle = (self.angle - 2) % 360
        self.update_graphics()

class CyberRadarApp(App):
    def build(self):
        Window.clearcolor = (0.02, 0.04, 0.06, 1)
        return CyberRadarWidget()

if __name__ == '__main__':
    CyberRadarApp().run()
      
