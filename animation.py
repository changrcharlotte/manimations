from manim import *

class HelloWorld(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle)
        self.add(square)

