from abc import ABC, abstractmethod


class State(ABC):
    """
    Abstract base class for a state in a state machine.
    """

    @abstractmethod
    def handle(self, context):
        """
        Handle the state logic and transition to the next state if necessary.

        :param context: The context in which the state operates.
        """
        pass


class ProcessContext:
    """
    Context class that holds the current state and allows for state transitions.
    """

    def __init__(self, initial_state: State):
        self._state = initial_state

    def set_state(self, new_state: State):
        """
        Set a new state for the context.

        :param new_state: The new state to transition to.
        """
        self._state = new_state

    def request(self):
        """
        Delegate the handling of the current state.
        """
        self._state.handle(self)


class StartState(State):
    def handle(self, context: ProcessContext):
        print("Initial state: Starting process.")
        context.set_state(RunningState())


class RunningState(State):
    def handle(self, context: ProcessContext):
        print("Running state: Process is running.")
        # Transition to the next state
        context.set_state(EndState())


class EndState(State):
    def handle(self, context: ProcessContext):
        print("End state: Process has ended.")
        # No further transitions, could reset or end the process here


process = ProcessContext(StartState())
process.request()
process.request()
process.request()
process.request()

# The output will show the transitions through the states
# Initial state: Starting process.
# Running state: Process is running.
# End state: Process has ended.
# No further transitions, could reset or end the process here
# The last request will not change the state anymore.
