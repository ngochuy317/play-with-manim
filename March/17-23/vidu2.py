import os
from pathlib import Path
from manim import *


class ExampleSecondScene(Scene):
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
        problem = MathTex(
            r"\textbf{Ví dụ 2.}",
            r"\text{ Cho hai hàm số }y = 4x - x^2\text{và }y = x\text{lần lượt có đồ thị là }(P)\text{ và }d\text{ như}"
            ).to_corner(UL, buff=0.3)
        problem[0].set_color(RED)

        question_a_1 = MathTex(
            r"\textbf{a) }",
            r"\text{ Tính diện tích }S_1\text{ của hình phẳng giới hạn bởi }(P)"
            )
        question_a_1[0].set_color(BLUE)
        question_a_2 = MathTex(
            r"\text{trục hoành và hai đường thẳng }x = 0\text{, }x = 2\text{.}"
            ).next_to(question_a_1, DOWN, aligned_edge=LEFT, buff=0.2)

        question_b_1 = MathTex(
            r"\textbf{b) }",
            r"\text{ Tính diện tích }S\text{ của hình phẳng giới hạn bởi }(P)\text{,}"
            ).next_to(question_a_2, DOWN, aligned_edge=LEFT, buff=0.3)
        question_b_1[0].set_color(BLUE)
        question_b_2 = MathTex(
            r"d\text{ và hai đường thẳng }x = 0\text{, }x = 2\text{.}"
            ).next_to(question_b_1, DOWN, aligned_edge=LEFT, buff=0.3)
        question_vgroup = VGroup(
            question_a_1,
            question_a_2,
            question_b_1,
            question_b_2,
        ).next_to(problem, DOWN, aligned_edge=LEFT, buff=0.2)

        axes = Axes(
            x_range=[-2, 6, 1],
            x_length=8,
            y_range=[-2, 5, 1],
            y_length=7,
            axis_config={
                "tip_shape": StealthTip,
                "font_size": 16,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_ticks": False,
            }
        ).scale(0.7)
        label_x = MathTex(r"x").next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        label_y = MathTex(r"y").next_to(axes.y_axis.get_end(), LEFT, buff=0.1)
        label_O = MathTex(r"O").next_to(axes.c2p(0, 0), DR, buff=0.1)
        label_d = MathTex(r"d").next_to(axes.c2p(-1.5, -1.5), UL, buff=0.1)
        point_0_4 = Dot(point=axes.c2p(0, 4))
        label_0_4 = MathTex("4").next_to(point_0_4, LEFT, buff=0.1)
        point_2__1 = Dot(point=axes.c2p(2, -1))
        label_x_equal_2 = MathTex("x = 2").next_to(point_2__1, RIGHT, buff=0.1)
        point_2_0 = Dot(point=axes.c2p(2, 0))
        label_2_0 = MathTex("2").next_to(point_2_0, DR, buff=0.1)
        point_4_0 = Dot(point=axes.c2p(4, 0))
        label_4_0 = MathTex("4").next_to(point_4_0, DL, buff=0.1)
        point_2_2 = Dot(point=axes.c2p(2, 2))
        label_S = MathTex("S").next_to(point_2_2, LEFT, buff=0.2)
        point_1_5__3_5 = Dot(point=axes.c2p(3.5, 1.5))
        label_P = MathTex("(P)").next_to(point_1_5__3_5, RIGHT, buff=0.1)
        dashline_1 = axes.get_horizontal_line(axes.c2p(2, 4))

        def f(x):
            return 4 * x - x ** 2

        def g(x):
            return x

        graph_fx = axes.plot(lambda x: f(x), x_range=[-0.4, 4.4, 0.001], stroke_width=2)
        graph_gx = axes.plot(lambda x: g(x), x_range=[-2, 5, 0.001], stroke_width=2).set_color(RED)
        graph_x_equal_2 =  Line(
            start=axes.c2p(2, -2),
            end=axes.c2p(2, 5),
            color=WHITE,
        )

        area = axes.get_area(graph=graph_fx, bounded_graph=graph_gx, x_range=[0, 3]).set_color(YELLOW)

        area_vgroup = VGroup(
            axes,
            graph_fx,
            graph_gx,
            graph_x_equal_2,
            area,
            label_x,
            label_y,
            label_O,
            label_d,
            label_0_4,
            label_2_0,
            label_4_0,
            label_x_equal_2,
            dashline_1,
            label_S,
            label_P,
        )

        # GIẢI
        
        text_1 = Tex(r"a)").next_to(question_b_2, DOWN, aligned_edge=LEFT, buff=0.8)
        text_2 = MathTex(r"(H)").next_to(text_1, DOWN, aligned_edge=LEFT, buff=0.3)
        text_3 = MathTex(
            r"\begin{cases}"
            r"y = 4x - x^2 \\"
            r"y = 0 \\"
            r"x = 0 \\"
            r"x = 2"
            r"\end{cases}"
        ).next_to(text_2, RIGHT, buff=0.3)
        text_4 = MathTex(
            r"S_{(H)} = \int_{0}^{2} |4x - x^2| \,dx = \frac{16}{3}\text{ (Bấm máy)}"
        ).next_to(text_3, DOWN, buff=0.3)
        text_5 = Tex(r"b)").next_to(text_1, DOWN, aligned_edge=LEFT, buff=3)
        text_6 = MathTex(r"(H)").next_to(text_5, DOWN, aligned_edge=LEFT, buff=0.3)
        text_7 = MathTex(
            r"\begin{cases}"
            r"y = 4x - x^2 \\"
            r"y = x \\"
            r"x = 0 \\"
            r"x = 2"
            r"\end{cases}"
        ).next_to(text_6, RIGHT, buff=0.3)
        arrow_1 = MathTex(r"\Rightarrow").next_to(text_7, DOWN, buff=0.3)
        text_8 = MathTex(
            r"S_{(H)} = \int_{0}^{2} |(4x - x^2) - (x)| \,dx"
        ).next_to(arrow_1, RIGHT, buff=0.3)
        arrow_2 = MathTex(r"\Rightarrow").next_to(text_8, RIGHT, buff=0.3)
        text_9 = MathTex(
            r"\begin{cases}"
            r"\text{Bấm máy} \\"
            r"\int_{0}^{2} |3x - x^2| \,dx = \frac{10}{3} \\"
            r"\end{cases}"
        ).next_to(arrow_2, RIGHT, buff=0.3)

        text_vgroup = VGroup(
            text_1,
            text_2,
            text_3,
            text_4,
            text_5,
            text_6,
            text_7,
            arrow_1,
            text_8,
            arrow_2,
            text_9,
        )

        area_vgroup.next_to(text_1, RIGHT, aligned_edge=RIGHT, buff=10)

        self.add(
            problem,
            question_vgroup,
            area_vgroup,
            text_vgroup,
        )


FLAGS = f"-pqm"
SCENE = "ExampleSecondScene"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
