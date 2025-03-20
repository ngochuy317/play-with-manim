import os
from pathlib import Path
from manim import *


class ExampleThirdScene(Scene):
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
            r"\textbf{Ví dụ 3.}",
            r"\text{ Tính diện tích hình phẳng giới hạn bởi đồ thị của hai hàm số}y = x^2 - 2x -1\text{, }y = x -1"
            ).to_corner(UL, buff=0.3)
        problem_1[0].set_color(RED)
        problem_2 = MathTex(
            r"\text{ và hai đường thẳng }x=1\text{, }x=4"
            ).next_to(problem_1, DOWN, aligned_edge=LEFT, buff=0.3)


        axes = Axes(
            x_range=[-3, 5, 1],
            x_length=8,
            y_range=[-4, 8, 1],
            y_length=12,
            axis_config={
                "tip_shape": StealthTip,
                "font_size": 16,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_ticks": False,
            }
        ).scale(0.5)
        label_x = MathTex(r"x").next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        label_y = MathTex(r"y").next_to(axes.y_axis.get_end(), LEFT, buff=0.1)
        label_O = MathTex(r"O").next_to(axes.c2p(0, 0), DL, buff=0.3)
        label_d = MathTex(r"d").next_to(axes.c2p(-2, -2.4), UL, buff=0.1)
        point_0_7 = Dot(point=axes.c2p(0, 7))
        label_0_7 = MathTex("7").next_to(point_0_7, LEFT, buff=0.1)
        point_0__2 = Dot(point=axes.c2p(0, -2))
        label_0__2 = MathTex("2").next_to(point_0__2, LEFT, buff=0.1)
        point_4__1 = Dot(point=axes.c2p(4, -1))
        label_x_equal_4 = MathTex("x = 4").next_to(point_4__1, RIGHT, buff=0.1)
        point_1__2 = Dot(point=axes.c2p(1, -2))
        label_x_equal_1 = MathTex("x = 1").next_to(point_1__2, DR, buff=0.1)
        point_2_0 = Dot(point=axes.c2p(2, 0))
        label_2_0 = MathTex("2").next_to(point_2_0, DR, buff=0.1)
        point_4_0 = Dot(point=axes.c2p(4, 0))
        label_4_0 = MathTex("4").next_to(point_4_0, DL, buff=0.1)
        dashline_1 = axes.get_horizontal_line(axes.c2p(4, 7))
        dashline_2 = axes.get_horizontal_line(axes.c2p(1, -2))

        def f(x):
            return x ** 2 - 2 * x - 1

        def g(x):
            return x - 1

        graph_fx = axes.plot(lambda x: f(x), x_range=[-1, 4.1, 0.001], stroke_width=2)
        graph_gx = axes.plot(lambda x: g(x), x_range=[-2, 5, 0.001], stroke_width=2).set_color(RED)
        graph_x_equal_1 =  Line(
            start=axes.c2p(1, -3),
            end=axes.c2p(1, 8),
            color=WHITE,
        )
        graph_x_equal_4 =  Line(
            start=axes.c2p(4, -3),
            end=axes.c2p(4, 8),
            color=WHITE,
        )

        area = axes.get_area(graph=graph_fx, bounded_graph=graph_gx, x_range=[1, 4]).set_color(YELLOW)

        area_vgroup = VGroup(
            axes,
            graph_fx,
            graph_gx,
            graph_x_equal_1,
            graph_x_equal_4,
            area,
            label_x,
            label_y,
            label_O,
            label_d,
            label_0_7,
            label_0__2,
            label_2_0,
            label_4_0,
            label_x_equal_4,
            label_x_equal_1,
            dashline_1,
            dashline_2,
        )

        # GIẢI
        text_1 = MathTex(r"(H)").next_to(problem_2, DOWN, aligned_edge=LEFT, buff=1)
        text_2 = MathTex(
            r"\begin{cases}"
            r"y = x^2 - 2x - 1 \\"
            r"y = x - 1 \\"
            r"x = 1 \\"
            r"x = 4"
            r"\end{cases}"
        ).next_to(text_1, RIGHT, buff=0.3)
        arrow = MathTex(r"\Rightarrow").next_to(text_1, DOWN, buff=1.4)
        text_3 = MathTex(
            r"S_{(H)} = \int_{1}^{3} |(x^2 - 2x - 1) - (x - 1)| \,dx"
        ).next_to(arrow, RIGHT, buff=0.3)
        text_4 = MathTex(
            r"= \frac{31}{6}"
        ).next_to(text_3, DOWN, buff=0.3)

        text_vgroup = VGroup(
            text_1,
            text_2,
            text_3,
            text_4,
            arrow,
        )
        area_vgroup.next_to(text_3, RIGHT, aligned_edge=RIGHT, buff=4)

        self.add(
            problem_1,
            problem_2,
            area_vgroup,
            text_vgroup,
        )


FLAGS = f"-pqm"
SCENE = "ExampleThirdScene"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
