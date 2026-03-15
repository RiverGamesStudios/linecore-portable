# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of LineRenderer from LineCore OS in Python."""

from tcolorpy import Color, tcolor
import scratch3


class RenderAgent(scratch3.List):
    def add(self, value):
        super().add(value)
        EmptyLine.change(len(self.list) + 1)
        Function()

    def remove(self, value):
        super().remove(value)
        EmptyLine.change(len(self.list) + 1)
        Function()

    def clear(self):
        super().clear()
        EmptyLine.change(len(self.list) + 1)
        Function()


TerminalRenderAgent = RenderAgent()
EmptyLine = scratch3.Variable(0)
EmptyLineEnabled = scratch3.Variable(True)
TextColor = scratch3.Variable("#FFFFFF")
BgColor = scratch3.Variable("#000000")
InputLine = scratch3.Variable("")


def print_tcolor(to_print: str, color: Color, bg_color: Color, end: str = "\n") -> None:
    print(tcolor(to_print, color=color, bg_color=bg_color), end=end)


def set_title(title: str) -> None:
    """Doesn't work"""
    print(f"\x1b]2;{title}\x07", end="")


def print_ps1(ps1: str) -> None:
    """Print a PS1
    This code is really bad..."""
    print(
        tcolor(f"{ps1}", color=Color(TextColor.get()), bg_color=Color(BgColor.get())),
        end=tcolor(
            f"\r{ps1} ", color=Color(TextColor.get()), bg_color=Color(BgColor.get())
        ),
    )


def Function() -> None:
    print("\x1b[2J\033[H", end="")

    currentline = 1

    for _ in TerminalRenderAgent:
        if TerminalRenderAgent.get(currentline) == EmptyLine.get() and EmptyLineEnabled.get():
            print_ps1(InputLine.get())
        else:
            print_tcolor(
                TerminalRenderAgent.get(currentline),
                Color(TextColor.get()),
                Color(BgColor.get()),
            )
        currentline += 1

    while not currentline == EmptyLine.get():
        currentline += 1

    if EmptyLineEnabled.get():
        print_ps1(InputLine.get())
