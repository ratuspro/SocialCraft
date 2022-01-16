from pyclbr import Function
import string
from typing import Callable


class CognitiveSocialFrame:
    def __init__(self) -> None:
        self.__salience_functions = []
        self.__affordances = []

    def add_salient_function(
        self, salience_function: Callable[[list[str]], bool]
    ) -> None:
        self.__salience_functions.append(salience_function)

    def add_affordances(self, affordance: str) -> None:
        self.__affordances.append(affordance)

    def is_salient(self, context: list[str]) -> bool:
        for salience_func in self.__salience_functions:
            if salience_func(context):
                return True
        return False

    def get_affordances(self) -> list[str]:
        return self.__affordances


class Manager:
    def __init__(self) -> None:
        self.__frames = set()
        self.__perception_buffer = set()
        self.__salient_frames = set()

    def add_frame(self, frame: CognitiveSocialFrame) -> None:
        self.__frames.add(frame)

    def add_perception_to_buffer(self, perception: str) -> None:
        self.__perception_buffer.add(perception)

    def update_saliences(self) -> None:
        self.__salient_frames.clear()

        for frame in self.__frames:
            if frame.is_salient(self.__perception_buffer):
                self.__salient_frames.add(frame)

        self.__perception_buffer.clear()

    def get_affordances(self) -> list[str]:
        affordances = set()
        for sal_frame in self.__salient_frames:
            affordances = affordances.union(sal_frame.get_affordances())

        return affordances
