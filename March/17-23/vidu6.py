import os
from pathlib import Path
from manim import *
import math


DOT_RADIUS = 0.05


class ExampleSixthScene(Scene):
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
            r"\textbf{Ví dụ 6.}",
            r"\text{ Cho }(H)\text{ là hình phẳng được tô đậm trong hình vẽ và được giới hạn bởi các đường}"
            ).to_corner(UL, buff=0.3)
        problem_1[0].set_color(RED)
        problem_2 = MathTex(
            r"\text{có phương trình }y = \frac{10}{3}x - x^2\text{, }y = \begin{cases}"
            r"-x\text{ khi }x \leq 1 \\"
            r"x - 2\text{ khi }x > 1\\"
            r"\end{cases}"
            r"\text{. Diện tích của }(H)\text{ bằng ?}"
            ).next_to(problem_1, DOWN, aligned_edge=LEFT, buff=0.1)

        axes = Axes(
            x_range=[-1, 4, 1],
            x_length=5,
            y_range=[-2, 3, 1],
            y_length=5,
            axis_config={
                "tip_shape": StealthTip,
                "font_size": 16,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_ticks": False,
            }
        )

        label_x = MathTex(r"x").next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        label_y = MathTex(r"y").next_to(axes.y_axis.get_end(), RIGHT, buff=0.1)
        label_O = MathTex(r"O").next_to(axes.c2p(0, 0), DL, buff=0.1)
        label_s1 = MathTex(r"S_{1}").next_to(axes.c2p(2, 1), DL, buff=0.1).set_color(RED)
        label_s2 = MathTex(r"S_{2}").next_to(axes.c2p(0.5, 0.5), DOWN, buff=0.1).set_color(RED)

        def f(x):
            return 10 / 3 * x - x ** 2

        def g(x):
            return -x if x <= 1 else x - 2

        graph_fx = axes.plot(lambda x: f(x), x_range=[-0.2, 3.6, 0.001], stroke_width=2)
        graph_gx = axes.plot(lambda x: g(x), x_range=[-1, 4, 0.001], stroke_width=2)
        label_gx_1 = Tex(r"y = x - 2").move_to(axes.c2p(4.5, 1)).set_color(RED)
        label_gx_2 = MathTex(r"y = - x^2").move_to(axes.c2p(-2, 0.5)).set_color(RED)
        label_fx = MathTex(r"y = \frac{10}{3}x - x^2").move_to(axes.c2p(4.5, 3)).set_color(RED)
        arrow_graph_1 = CurvedArrow(
            start_point=axes.c2p(3.4, 1.4),
            end_point=label_gx_1.get_top(), 
            angle=-PI/4,
            color=RED,
            tip_length=0.2
        )
        arrow_graph_2 = CurvedArrow(
            start_point=axes.c2p(-0.4, 0.4),
            end_point=label_gx_2.get_right(), 
            angle=-PI/4,
            color=RED,
            tip_length=0.2
        )
        arrow_graph_3 = CurvedArrow(
            start_point=axes.c2p(2, 8/3),
            end_point=label_fx.get_left(), 
            angle=-PI/4,
            color=RED,
            tip_length=0.2
        )
        area = axes.get_area(graph=graph_fx, bounded_graph=graph_gx, x_range=[0, 3]).set_color(GRAY)

        point_1_0 = Dot(point=axes.c2p(1, 0), radius=DOT_RADIUS, color=RED)
        point__1_0 = Dot(point=axes.c2p(0, -1), radius=DOT_RADIUS, color=RED)
        point_2_0 = Dot(point=axes.c2p(2, 0), radius=DOT_RADIUS, color=RED)
        point_3_0 = Dot(point=axes.c2p(3, 0), radius=DOT_RADIUS, color=RED)
        label__1_0 = Tex("-1").next_to(point__1_0, LEFT, buff=0.1)
        label_1_0 = Tex("1").next_to(point_1_0, UR, buff=0.1).set_color(RED)
        label_2_0 = Tex("2").next_to(point_2_0, DOWN, buff=0.1)
        label_3_0 = Tex("3").next_to(point_3_0, DOWN, buff=0.1)
        dashline_1 = axes.get_vertical_line(axes.c2p(3, 1))
        dashline_2 = axes.get_horizontal_line(axes.c2p(1, -1))
        graph_x_equal_1 =  Line(
            start=axes.c2p(1, -2),
            end=axes.c2p(1, 3),
            color=BLUE,
        )

        area_vgroup = VGroup(
            axes,
            graph_fx,
            graph_gx,
            graph_x_equal_1,
            area,
            label_x,
            label_y,
            label_O,
            label_s1,
            label_s2,
            label_gx_1,
            label_gx_2,
            label_fx,
            point_1_0,
            label__1_0,
            label_1_0,
            label_2_0,
            label_3_0,
            dashline_1,
            dashline_2,
            arrow_graph_1,
            arrow_graph_2,
            arrow_graph_3,
        ).next_to(problem_2, DOWN, aligned_edge=LEFT, buff=0.3)

        answer_a = Tex(r"\textbf{A.}", r" $\dfrac{11}{6}$.").next_to(area_vgroup, DOWN, aligned_edge=LEFT, buff=0.4)
        answer_b = Tex(r"\textbf{B.}", r" $\dfrac{13}{2}$.").next_to(answer_a, RIGHT, buff=0.5)
        answer_c = Tex(r"\textbf{C.}", r" $\dfrac{11}{2}$.").next_to(answer_b, RIGHT, buff=0.5)
        answer_d = Tex(r"\textbf{D.}", r" $\dfrac{14}{3}$.").next_to(answer_c, RIGHT, buff=0.5)
        answer_a[0].set_color(BLUE)
        answer_b[0].set_color(BLUE)
        answer_c[0].set_color(BLUE)
        answer_d[0].set_color(BLUE)

        # GIẢI
        text_1 = MathTex(r"S_{(H)}")
        text_2 = MathTex(r" = S_{(H_{1})} + S_{(H_{2})}").next_to(text_1, RIGHT, buff=0.1)
        text_3 = MathTex(r"S_{(H_{1})}").next_to(text_1, DOWN, buff=1)
        text_4 = MathTex(
            r"\begin{cases}"
            r"y = \frac{10}{3}x - x^2 \\"
            r"y = - x \\"
            r"x = 0 \\"
            r"x = 1 \\"
            r"\end{cases}"
        ).next_to(text_3, RIGHT, buff=0.3)
        text_5 = MathTex(r"S_{(H_{1})}").next_to(text_3, DOWN, buff=1)
        text_6 = MathTex(
            r" = \int_{0}^{1} |( \frac{10}{3}x - x^2 ) - (- x)| \,dx = \frac{11}{6}"
        ).next_to(text_5, RIGHT, aligned_edge=LEFT, buff=0.4)
        text_7 = MathTex(r"S_{(H_{2})}").next_to(text_5, DOWN, buff=1)
        text_8 = MathTex(
            r" = \int_{1}^{3} |( \frac{10}{3}x - x^2 ) - (x - 2)| \,dx = \frac{14}{3}"
        ).next_to(text_7, RIGHT, aligned_edge=LEFT, buff=0.4)

        arrow = MathTex(r"\Rightarrow").next_to(text_7, DOWN, buff=1)
        text_9 = MathTex(
            r"S_{(H)} = S_{(H_{1})} + S_{(H_{2})} = \frac{13}{2}"
        ).next_to(arrow, RIGHT, aligned_edge=LEFT, buff=0.3)

        text_vgroup = VGroup(
            text_1,
            text_2,
            text_3,
            text_4,
            text_5,
            text_6,
            text_7,
            text_8,
            text_9,
            arrow,
        ).next_to(area_vgroup, RIGHT, aligned_edge=RIGHT, buff=5)

        self.add(
            problem_1,
            problem_2,
            answer_a,
            answer_b,
            answer_c,
            answer_d,
            area_vgroup,
            text_vgroup,
        )


FLAGS = f"-pqm"
SCENE = "ExampleSixthScene"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
