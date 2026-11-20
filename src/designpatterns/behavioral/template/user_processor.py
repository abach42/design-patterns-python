from .data_processor import DataProcessor
from .user_data import UserData


class UserProcessor(DataProcessor[UserData]):

    def fetch_data(self) -> list[UserData]:
        # simulates reading users from a database
        return [UserData("John"), UserData("Alice")]

    def process(self, data_list: list[UserData]) -> list[UserData]:
        return sorted(data_list, key=lambda user: user.name)
