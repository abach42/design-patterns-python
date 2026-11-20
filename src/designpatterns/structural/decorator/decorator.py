from abc import ABC

from .component import Component


class Decorator(ABC, Component):

    def __init__(self, component: Component) -> None:
        self.component = component
