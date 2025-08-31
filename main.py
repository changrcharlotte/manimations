from manim import *

class SquareScene(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.wait()

