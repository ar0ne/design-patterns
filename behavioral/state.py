"""
State lets an object alter its behavior when its internal state changes. It appears as if the object
 changed its class.
"""
from abc import ABC, abstractmethod
from time import sleep
from typing import Callable


class TransitionNotAllowed(Exception):
    ...


class State(ABC):

    def __init__(self):
        self.process = None

    @abstractmethod
    def on_load(self) -> str:
        ...

    @abstractmethod
    def on_dispatch(self) -> str:
        ...

    @abstractmethod
    def on_interrupt(self) -> str:
        ...

    @abstractmethod
    def on_wait(self) -> str:
        ...

    @abstractmethod
    def on_complete(self) -> str:
        ...

    @abstractmethod
    def on_exit(self) -> str:
        ...


class ProcessState(State, ABC):

    def on_load(self) -> str:
        raise TransitionNotAllowed

    def on_dispatch(self) -> str:
        raise TransitionNotAllowed

    def on_interrupt(self) -> str:
        raise TransitionNotAllowed

    def on_wait(self) -> str:
        raise TransitionNotAllowed

    def on_complete(self) -> str:
        raise TransitionNotAllowed

    def on_exit(self) -> str:
        raise TransitionNotAllowed


class NewState(ProcessState):

    def on_load(self) -> str:
        self.process.transition_to(ReadyState())
        return "Ready"


class ReadyState(ProcessState):

    def on_dispatch(self) -> str:
        self.process.transition_to(RunningState())
        return "Running"


class RunningState(ProcessState):

    def on_interrupt(self) -> str:
        self.process.transition_to(ReadyState())
        return "Ready"

    def on_wait(self) -> str:
        self.process.transition_to(WaitingState())
        return "Wait"

    def on_exit(self) -> str:
        self.process.transition_to(TerminatedState())
        return "Exit"


class WaitingState(ProcessState):

    def on_complete(self) -> str:
        self.process.transition_to(ReadyState())
        return "Ready"


class TerminatedState(ProcessState):
    ...


class Process:

    def __init__(self, state: State) -> None:
        self._state = None
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        self._state = state
        self._state.process = self

    def load(self) -> None:
        self._state.on_load()
        print("Loaded new process")

    def execute(self, func: Callable) -> None:
        self._state.on_dispatch()
        print("Started processing new task (scheduler dispatch)")
        func()
        # emulate some delay on IO
        process.start_io()
        process.end_io()

    def start_io(self) -> None:
        self._state.on_wait()
        print("I/O")
        sleep(1)

    def end_io(self) -> None:
        self._state.on_complete()
        print("Ended I/O")
        sleep(1)


def run(process: Process, func: Callable) -> None:
    print("Do some work")
    process.load()
    process.execute(func)
    try:
        print("verify we can't transit from ready to wait state")
        process.start_io()
    except TransitionNotAllowed:
        pass


if __name__ == "__main__":
    process = Process(NewState())

    run(process, lambda: print("some func"))
