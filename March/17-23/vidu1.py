import os
from pathlib import Path
from manim import *


class ExampleOneScene(Scene):
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
        question_1 = MathTex(
            r"\textbf{Ví dụ 1.}",
            r"\text{ Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số }y = f(x) = x^2 - 4x + 3"
            r"\text{, trục hoành}",
            ).to_corner(UL, buff=0.3)
        question_1[0].set_color(RED)
        question_2 = MathTex(
            r"\text{và hai đường thẳng }x = 0\text{, }y = 0\text{.}",
        ).next_to(question_1, DOWN, aligned_edge=LEFT, buff=0.1)


        # HÌNH
        axes = Axes(
            x_range=[-1, 4, 1],
            x_length=5,
            y_range=[-2, 4, 1],
            y_length=6,
            axis_config={
                "tip_shape": StealthTip,
                "font_size": 16,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_ticks": False,
            }
        )
        label_x = MathTex(r"x").next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        label_y = MathTex(r"y").next_to(axes.y_axis.get_end(), LEFT, buff=0.1)
        label_O = MathTex(r"O").next_to(axes.c2p(0, 0), DL, buff=0.1)
        point_0_3 = Dot(point=axes.c2p(0, 3), color=WHITE)
        label_0_3 = MathTex("(0, 3)").next_to(point_0_3, LEFT, buff=0.1)
        point_1_0 = Dot(point=axes.c2p(1, 0), color=WHITE)
        label_1_0 = MathTex("(1, 0)").next_to(point_1_0, UP, buff=0.1)
        point_3_0 = Dot(point=axes.c2p(3, 0), color=WHITE)
        label_3_0 = MathTex("(3, 0)").next_to(point_3_0, UP, buff=0.1)

        def f(x):
            return x ** 2 - 4 * x + 3

        def g(x):
            return 0

        graph_fx = axes.plot(lambda x: f(x), x_range=[-1, 4, 0.001], stroke_width=2)
        graph_gx = axes.plot(lambda x: g(x), x_range=[-1, 4, 0.001], stroke_width=2)

        area = axes.get_area(graph=graph_fx, bounded_graph=graph_gx, x_range=[0, 3])

        # GIẢI
        text_1 = MathTex(r"(H)")
        text_2 = MathTex(
            r"\begin{cases}"
            r"y = x^2 - 4x + 3 \\"
            r"y = 0 \\"
            r"x = 0 \\"
            r"x = 3"
            r"\end{cases}"
        ).next_to(text_1, RIGHT, buff=0.3)
        arrow = MathTex(r"\Rightarrow").next_to(text_2, RIGHT, buff=0.3)
        text_3 = MathTex(
            r"S_{(H)} = \int_{0}^{3} |x^2 - 4x + 3| \,dx"
        ).next_to(arrow, RIGHT, buff=0.3)

        text_123 = VGroup(text_1, text_2, arrow, text_3).next_to(question_2, DOWN, aligned_edge=LEFT, buff=0.3)

        text_4 = MathTex(r"x^2 - 4x + 3 = 0")
        equivalence = MathTex(r"\Leftrightarrow").next_to(text_4, RIGHT, buff=0.3)
        text_5 = MathTex(r"x = 1, 3").next_to(equivalence, RIGHT, buff=0.3)
        text_45 = VGroup(text_4, equivalence, text_5).next_to(text_123, DOWN, aligned_edge=LEFT, buff=0.3)

        text_6 = Tex(r"TXD: ")
        number_line = NumberLine(
            x_range=[-1, 4],
        )
        dot_0 = Dot(point=number_line.n2p(0), color=RED)
        dot_1 = Dot(point=number_line.n2p(1))
        dot_3 = Dot(point=number_line.n2p(3))
        label_0 = MathTex("0", color=RED).next_to(dot_0, UP)
        label_1 = MathTex("1").next_to(dot_1, UP)
        label_3 = MathTex("3").next_to(dot_3, UP)
        label_O1 = MathTex("0").next_to(dot_1, DOWN)
        label_O3 = MathTex("0").next_to(dot_3, DOWN)
        plus_left = MathTex("+").next_to(number_line.n2p(-0.5), UP)
        minus_middle = MathTex("-").next_to(number_line.n2p(2), DOWN)
        plus_right = MathTex("+").next_to(number_line.n2p(3.5), UP)
        arrow_1 = ArcBetweenPoints(
            label_O1.get_bottom(), label_O3.get_bottom(),
            angle=PI/2, color=RED
        )
        arrow_2 = ArcBetweenPoints(
            label_0.get_top(), label_1.get_top(),
            angle=-PI/2, color=RED
        )
        chart_elements = VGroup(
            number_line,
            dot_0,
            dot_1,
            dot_3,
            label_0,
            label_1,
            label_3,
            label_O1,
            label_O3,
            plus_left,
            minus_middle,
            plus_right,
            arrow_1,
            arrow_2,
        ).next_to(text_6, RIGHT, buff=0.3)
        text_6_and_chart = VGroup(text_6, chart_elements).next_to(text_45, DOWN, aligned_edge=LEFT, buff=0.3)

        text_7 = MathTex(
            r"\text{Vậy }\int_{0}^{3} |x^2 - 4x + 3| \,dx"
        ).next_to(text_6_and_chart, DOWN, aligned_edge=LEFT, buff=0.3)

        text_8 = MathTex(
            r"= \int_{0}^{1} |x^2 - 4x + 3| \,dx + \int_{1}^{3} |x^2 - 4x + 3| \,dx"
        ).next_to(text_7, DOWN, aligned_edge=LEFT, buff=0.3)
        
        text_9 = MathTex(
            r"= \int_{0}^{1} (x^2 - 4x + 3) \,dx + \int_{1}^{3} (x^2 - 4x + 3) \,dx"
        ).next_to(text_8, DOWN, aligned_edge=LEFT, buff=0.3)
        
        text_10 = MathTex(
            r"= \text{...} = \frac{8}{3}"
        ).next_to(text_9, DOWN, aligned_edge=LEFT, buff=0.3)

        area_vgroup = VGroup(
            axes,
            area,
            label_x,
            label_y,
            label_O,
            point_0_3,
            label_0_3,
            point_1_0,
            label_1_0,
            point_3_0,
            label_3_0,
        ).next_to(text_7, RIGHT, aligned_edge=RIGHT, buff=6)

        self.add(
            question_1,
            question_2,
            text_123,
            text_45,
            text_6_and_chart,
            text_7,
            text_8,
            text_9,
            text_10,
            area_vgroup,
        )


FLAGS = f"-pqm"
SCENE = "ExampleOneScene"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
