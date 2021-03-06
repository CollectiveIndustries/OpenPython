# micropython
"access and control MicroPython internals"
from typing import Any, Optional, Callable


def const(expr: Any) -> Any:
    """Used to declare that the expression is a constant so that the compile can optimise it.
    Constants declared this way are still accessible as global variables from outside the module they are declared in. On the other hand, if a constant begins with an underscore then it is hidden, it is not available as a global variable, and does not take up any memory during execution.
    This const function is recognised directly by the MicroPython parser and is provided as part of the micropython module mainly so that scripts can be written which run under both CPython and MicroPython, by following the above pattern.
    """


def opt_level(level: int = None) -> Optional[int]:
    "If level is given then this function sets the optimisation level for subsequent compilation of scripts, and returns None. Otherwise it returns the current optimisation level."
    pass


def alloc_emergency_exception_buf(size):
    """Allocate size bytes of RAM for the emergency exception buffer (a good size is around 100 bytes). The buffer is used to create exceptions in cases when normal RAM allocation would fail (eg within an interrupt handler) and therefore give useful traceback information in these situations.
    A good way to use this function is to put it at the start of your main script (eg boot.py or main.py) and then the emergency exception buffer will be active for all the code following it.
    """
    pass


def mem_info(verbose: int = None):
    """
    Print information about currently used memory. If the verbose argument is given then extra information is printed.
    The information that is printed is implementation dependent, but currently includes the amount of stack and heap used. In verbose mode it prints out the entire heap indicating which blocks are used and which are free.
    """
    pass


def qstr_info(verbose: int = None):
    """
    Print information about currently interned strings. If the verbose argument is given then extra information is printed.
    The information that is printed is implementation dependent, but currently includes the number of interned strings and the amount of RAM they use. In verbose mode it prints out the names of all RAM-interned strings.
    """
    pass


def stack_use():
    "Return an integer representing the current amount of stack that is being used. The absolute value of this is not particularly useful, rather it should be used to compute differences in stack usage at different points."
    pass


def heap_lock():
    """
    Lock or unlock the heap. When locked no memory allocation can occur and a MemoryError will be raised if any heap allocation is attempted.
    These functions can be nested, ie heap_lock() can be called multiple times in a row and the lock-depth will increase, and then heap_unlock() must be called the same number of times to make the heap available again.
    """
    pass


def heap_unlock():
    """
    Lock or unlock the heap. When locked no memory allocation can occur and a MemoryError will be raised if any heap allocation is attempted.
    These functions can be nested, ie heap_lock() can be called multiple times in a row and the lock-depth will increase, and then heap_unlock() must be called the same number of times to make the heap available again.
    """
    pass


def kbd_intr(chr):
    """
    Set the character that will raise a KeyboardInterrupt exception. By default this is set to 3 during script execution, corresponding to Ctrl-C. Passing -1 to this function will disable capture of Ctrl-C, and passing 3 will restore it.
    This function can be used to prevent the capturing of Ctrl-C on the incoming stream of characters that is usually used for the REPL, in case that stream is used for other purposes.
    """
    pass


def schedule(func: Callable, arg: Any):
    """
    Schedule the function func to be executed “very soon”. The function is passed the value arg as its single argument. “Very soon” means that the MicroPython runtime will do its best to execute the function at the earliest possible time, given that it is also trying to be efficient, and that the following conditions hold:

    A scheduled function will never preempt another scheduled function.
    Scheduled functions are always executed “between opcodes” which means that all fundamental Python operations (such as appending to a list) are guaranteed to be atomic.
    A given port may define “critical regions” within which scheduled functions will never be executed. Functions may be scheduled within a critical region but they will not be executed until that region is exited. An example of a critical region is a preempting interrupt handler (an IRQ).
    A use for this function is to schedule a callback from a preempting IRQ. Such an IRQ puts restrictions on the code that runs in the IRQ (for example the heap may be locked) and scheduling a function to call later will lift those restrictions.

    There is a finite stack to hold the scheduled functions and schedule will raise a RuntimeError if the stack is full.
    """
    pass
