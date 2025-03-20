import os
from pathlib import Path
from manim import *
import math


DOT_RADIUS = 0.05


class ExampleFifthScene(Scene):
    def construct(self):
        self.camera.frame_width *= 1.5
        self.camera.frame_height *= 1.5
        self.camera.frame_center = ORIGIN

        # Set global LaTeX preamble for Vietnamese support
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"""
            \usepackage[utf8]{vietnam}
            \usepackage[left=3cm,right=3cm,top=2cm,bottom=2cm]{geometry}
        """)
        Tex.set_default(tex_template=tex_template, font_size=30, tex_environment="flushleft")
        MathTex.set_default(tex_template=tex_template, font_size=30)

        # ĐỀ
        problem_1 = MathTex(
            r"\textbf{Ví dụ 5.}",
            r"\text{ Trong mặt phẳng cho Parabol }(P): y = x^2"
            ).to_corner(UL, buff=0.3)
        problem_1[0].set_color(RED)
        problem_2 = MathTex(
            r"\text{ và đường tròn }(C): x^2 + y^2 = 2\text{ (Xem hình vẽ). }"
            ).next_to(problem_1, RIGHT, buff=0.1)

        axes = Axes(
            x_range=[-2, 2, 1],
            x_length=4,
            y_range=[-2, 2, 1],
            y_length=4,
            axis_config={
                "tip_shape": StealthTip,
                "font_size": 16,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_ticks": False,
            }
        )

        circle = Circle(radius=math.sqrt(2), color=WHITE).move_to(axes.c2p(0, 0))
        label_x = MathTex(r"x").next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        label_y = MathTex(r"y").next_to(axes.y_axis.get_end(), RIGHT, buff=0.1)
        label_O = MathTex(r"O").next_to(axes.c2p(0, 0), DL, buff=0.1)

        def f(x):
            return x ** 2

        def upper_circle(x):
            return math.sqrt(abs(2 - x ** 2))

        graph_fx = axes.plot(lambda x: f(x), x_range=[-1.5, 1.5, 0.001], stroke_width=2)
        graph_upper_circle = axes.plot(lambda x: upper_circle(x), x_range=[-1, 1, 0.001], stroke_width=2, color=RED)
        label_fx = MathTex(r"f(x)").next_to(graph_fx.get_end(), UP, buff=0.1)
        area = axes.get_area(graph=graph_upper_circle, bounded_graph=graph_fx, x_range=[-1, 1]).set_color(GRAY)

        point__1_0 = Dot(point=axes.c2p(-1, 0), radius=DOT_RADIUS, color=RED)
        point_1_0 = Dot(point=axes.c2p(1, 0), radius=DOT_RADIUS, color=RED)
        label__1_0 = MathTex("-1").next_to(point__1_0, DOWN, buff=0.1).set_color(RED)
        label_1_0 = MathTex("1").next_to(point_1_0, DOWN, buff=0.1).set_color(RED)
        dashline_1 = axes.get_vertical_line(axes.c2p(1, 1), color=RED)
        dashline_2 = axes.get_vertical_line(axes.c2p(-1, 1), color=RED)

        area_vgroup = VGroup(
            axes,
            circle,
            graph_fx,
            graph_upper_circle,
            area,
            label_x,
            label_y,
            label_O,
            label_fx,
            point__1_0,
            point_1_0,
            dashline_1,
            dashline_2,
            label__1_0,
            label_1_0,
        ).next_to(problem_1, DOWN, aligned_edge=LEFT, buff=0.3)
        problem_3 = Tex(
            r"Tính diện tích phần tô đậm (làm tròn"
            ).next_to(area_vgroup, DOWN, aligned_edge=LEFT, buff=0.3)
        problem_4 = Tex(
            r" đến chữ số hàng phần chục)"
            ).next_to(problem_3, DOWN, aligned_edge=LEFT, buff=0.3)

        # GIẢI
        text_1 = MathTex(r"y^2 = 2 - x^2").next_to(problem_2, DOWN, aligned_edge=LEFT, buff=0.5)
        arrow_1 = MathTex(r"\Rightarrow").next_to(text_1, RIGHT, buff=0.3)
        text_2 = MathTex(
            r"\begin{cases}"
            r"y = \sqrt{2 - x^2} \\"
            r"y = - \sqrt{2 - x^2} \\"
            r"\end{cases}"
        ).next_to(arrow_1, RIGHT, buff=0.3)
        text_3 = MathTex(
            r"\text{gọi }y = f(x) = x^2"
        ).next_to(text_1, DOWN, aligned_edge=LEFT, buff=0.5)
        text_4 = MathTex(
            r"y = g(x)\text{ là 1 phần của đường tròn }(C)"
        ).next_to(text_3, DOWN, aligned_edge=LEFT, buff=0.1)
        text_5 = MathTex(
            r"\text{ nằm phía trên trục hoành nên }y = g(x) = \sqrt{2 - x^2}"
        ).next_to(text_4, DOWN, aligned_edge=LEFT, buff=0.1)
        text_6 = MathTex(
            r"\begin{cases}"
            r"y = f(x) = x^2 \\"
            r"y = g(x) = \sqrt{2 - x^2} \\"
            r"\end{cases}"
        ).next_to(text_5, DOWN, aligned_edge=LEFT, buff=0.1)
        text_7 = MathTex(
            r"\text{Pthđgđ: }x^2 = \sqrt{2 - x^2}\text{ }(x^2 \leq 2)"
        ).next_to(text_6, DOWN, aligned_edge=LEFT, buff=0.1)
        text_8 = MathTex(
            r"\Leftrightarrow x^4 + x^2 - 2 = 0"
        ).next_to(text_7, DOWN, aligned_edge=LEFT, buff=0.1)
        text_9 = MathTex(
            r"\Leftrightarrow"
            r"\begin{cases}"
            r"x^2 = 1 \Leftrightarrow x = \pm 1 \\"
            r"x^2 = -2 \text{( VN)} \\"
            r"\end{cases}"
        ).next_to(text_8, DOWN, aligned_edge=LEFT, buff=0.1)
        text_10 = MathTex(
            r"S_{(H)} = \int_{-1}^{1} |(x^2 - \sqrt{2 - x}| \,dx \approx 1.9"
        ).next_to(text_9, DOWN, aligned_edge=LEFT, buff=0.1)

        text_vgroup = VGroup(
            text_1,
            arrow_1,
            text_2,
            text_3,
            text_4,
            text_5,
            text_6,
            text_7,
            text_8,
            text_9,
            text_10,
        )

        self.add(
            problem_1,
            problem_2,
            problem_3,
            problem_4,
            area_vgroup,
            text_vgroup,
        )


FLAGS = f"-pqm"
SCENE = "ExampleFifthScene"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
