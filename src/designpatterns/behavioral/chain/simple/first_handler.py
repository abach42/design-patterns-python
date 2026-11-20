from .abstract_handler import AbstractHandler


class FirstHandler(AbstractHandler):

    def handle(self) -> None:
        print("first handler")
        self.handle_next()
