# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Basic Scratch3 reimplementation in Python."""

__all__ = ["List", "Variable"]


class List:
    def __init__(self):
        self.list = []

    def __iter__(self):
        yield from self.list

    def add(self, value):
        self.list.append(value)

    def remove(self, value):
        self.list.pop(value - 1)

    def clear(self):
        self.list.clear()

    def get(self, index):
        try:
            index_get = self.list[index - 1]
            return index_get
        except IndexError:
            return None


class Variable:
    def __init__(self, value):
        self.value = value

    def change(self, value):
        self.value = value

    def get(self):
        return self.value


def test_list():
    l = List()
    l.add("value 1")
    l.add("value 2")
    l.add("value 3")
    l.remove(2)  # should remove "value 2"
    assert l.get(2) == "value 3"


def test_variable():
    v = Variable("value")
    v.change("new value")
    assert v.get() == "new value"
