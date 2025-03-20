import os
from pathlib import Path
from manim import *


DOT_RADIUS = 0.05


class ExampleFourthScene(Scene):
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
            r"\textbf{Ví dụ 4.}",
            r"\text{ Cho hình phẳng }(H)\text{ giới hạn bởi các đường }y = |x^2 - 4x + 3|\text{, }y = x + 3\text{ phần tô đậm trong hình vẽ).}"
            ).to_corner(UL, buff=0.3)
        problem_1[0].set_color(RED)


        axes = Axes(
            x_range=[-2, 6, 1],
            x_length=8,
            y_range=[-2, 10, 1],
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
        point__1_0 = Dot(point=axes.c2p(-1, 0), radius=DOT_RADIUS)
        point_0_0 = Dot(point=axes.c2p(0, 0), radius=DOT_RADIUS)
        point_0_1 = Dot(point=axes.c2p(0, 1), radius=DOT_RADIUS)
        point_0_2 = Dot(point=axes.c2p(0, 2), radius=DOT_RADIUS)
        point_0_3 = Dot(point=axes.c2p(0, 3), radius=DOT_RADIUS)
        point_0_4 = Dot(point=axes.c2p(0, 4), radius=DOT_RADIUS)
        point_1_0 = Dot(point=axes.c2p(1, 0), radius=DOT_RADIUS)
        point_2_0 = Dot(point=axes.c2p(2, 0), radius=DOT_RADIUS)
        point_3_0 = Dot(point=axes.c2p(3, 0), radius=DOT_RADIUS)
        point_4_0 = Dot(point=axes.c2p(4, 0), radius=DOT_RADIUS)
        point_5_0 = Dot(point=axes.c2p(5, 0), radius=DOT_RADIUS)
        label_0_2 = MathTex("2").next_to(point_0_2, LEFT, buff=0.1)
        label_0_3 = MathTex("3").next_to(point_0_3, LEFT, buff=0.1)
        label_1_0 = MathTex("1").next_to(point_1_0, DOWN, buff=0.1)
        label_2_0 = MathTex("2").next_to(point_2_0, DOWN, buff=0.1)
        label_3_0 = MathTex("3").next_to(point_3_0, DOWN, buff=0.1)
        label_4_0 = MathTex("4").next_to(point_4_0, DOWN, buff=0.1)
        label_5_0 = MathTex("5").next_to(point_5_0, DOWN, buff=0.1)
        dashline_1 = axes.get_vertical_line(axes.c2p(5, 8))

        def f(x):
            return abs(x ** 2 - 4 * x + 3)

        def g(x):
            return x + 3

        graph_fx = axes.plot(lambda x: f(x), x_range=[-1, 5.2, 0.001], stroke_width=2)
        graph_gx = axes.plot(lambda x: g(x), x_range=[-2, 6, 0.001], stroke_width=2).set_color(RED)

        opposite_graph_fx = axes.plot(lambda x: -f(x), x_range=[1, 3, 0.001], stroke_width=2)
        dashed_graph_fx = DashedVMobject(opposite_graph_fx, num_dashes=10).set_color(PURPLE)

        area = axes.get_area(graph=graph_fx, bounded_graph=graph_gx, x_range=[0, 5]).set_color(PURPLE)

        area_vgroup = VGroup(
            axes,
            graph_fx,
            graph_gx,
            dashed_graph_fx,
            area,
            label_x,
            label_y,
            label_O,
            label_0_2,
            label_0_3,
            label_1_0,
            label_2_0,
            label_3_0,
            label_4_0,
            label_5_0,
            dashline_1,
            point__1_0,
            point_0_0,
            point_0_1,
            point_0_2,
            point_0_3,
            point_0_4,
            point_1_0,
            point_2_0,
            point_3_0,
            point_4_0,
            point_5_0,
        ).next_to(problem_1, DOWN, aligned_edge=LEFT, buff=0.3)
        problem_2 = MathTex(
            r"\text{Diện tích của }(H)\text{ bằng}"
            ).next_to(area_vgroup, DOWN, aligned_edge=LEFT, buff=0.3)

        # GIẢI
        text_1 = MathTex(r"(H)").next_to(area_vgroup, RIGHT, aligned_edge=RIGHT, buff=2)
        text_2 = MathTex(
            r"\begin{cases}"
            r"y = |x^2 - 4x + 3| \\"
            r"y = x + 3 \\"
            r"x = 0 \\"
            r"x = 5"
            r"\end{cases}"
        ).next_to(text_1, RIGHT, buff=0.3)
        text_3 = MathTex(
            r"S_{(H)} = \int_{0}^{5} |(x^2 - 4x + 3) - (x + 1)| \,dx"
        ).next_to(text_2, DOWN, buff=1)
        text_4 = MathTex(
            r"= \frac{103}{3}"
        ).next_to(text_3, RIGHT, buff=0.3)

        text_vgroup = VGroup(
            text_1,
            text_2,
            text_3,
            text_4,
        )

        self.add(
            problem_1,
            problem_2,
            area_vgroup,
            text_vgroup,
        )


FLAGS = f"-pqm"
SCENE = "ExampleFourthScene"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
