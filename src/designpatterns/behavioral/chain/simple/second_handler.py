from .abstract_handler import AbstractHandler


class SecondHandler(AbstractHandler):

    def handle(self) -> None:
        print("second handler")
        self.handle_next()
