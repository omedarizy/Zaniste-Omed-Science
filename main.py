from manim import *

class HydrogenScience(Scene):
    def construct(self):
        # Background high-tech space
        grid = NumberPlane(background_line_style={"stroke_opacity": 0.2})
        self.add(grid)

        # Atomic Cell
        box = Square(side_length=3, color=GOLD)
        symbol = Text("H", font_size=120)
        # Using reshaped Kurdish text logic
        kurdish_name = Text("هایدرۆجین", font_size=40, color=GOLD).next_to(symbol, DOWN)
        
        group = VGroup(box, symbol, kurdish_name)
        
        self.play(Create(box), Write(symbol))
        self.play(FadeIn(kurdish_name, shift=UP))
        self.wait(1)
        
        # Transformation to Atom Model
        nucleus = Dot(color=RED).scale(3)
        orbit = Circle(radius=2, color=WHITE).set_stroke(width=1, opacity=0.5)
        electron = Dot(color=BLUE).move_to(orbit.point_from_proportion(0))
        
        self.play(
            ReplacementTransform(box, orbit),
            ReplacementTransform(symbol, nucleus),
            kurdish_name.animate.to_edge(DOWN),
            FadeIn(electron)
        )
        
        # Electron Orbiting animation
        self.play(MoveAlongPath(electron, orbit), run_time=4, rate_func=linear)
        self.wait(2)
