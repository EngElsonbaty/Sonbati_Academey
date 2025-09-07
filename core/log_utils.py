# The user asked me to add comprehensive documentation and comments in English to the provided Python function.
# The request specifies that every line of code should have a comment.
# I will also write a docstring that accurately describes the function's purpose.

# All comments and documentation will be in English as requested.

import os
import sys
import logging
from functools import wraps
from time import perf_counter_ns

# Get the logger instance for the current module.
# The __name__ variable ensures the logger is named after the module,
# which helps in tracing the log source in a large application.
logger = logging.getLogger(__name__)

ROOT_LOG_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "log", "application.log"
)
FORMAT_LOGGER = "%(levelname)s:%(lineno)s:%(asctime)s:%(message)s"
logging.basicConfig(
    filename=ROOT_LOG_FILE, filemode="a", format=FORMAT_LOGGER, level=logging.DEBUG
)


def log_and_execute_time_with(func):
    """A decorator that logs the execution time of a function and handles any exceptions.

    This decorator wraps a function, measuring the time it takes to run in milliseconds.
    It logs the start and end of the function's execution. In case of an error,
    it logs a detailed error message with a full traceback and returns False.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function (a new function with the added logging and timing features).
    """

    # Use @wraps to preserve the original function's name, docstring, etc.
    @wraps(func)
    # Define the wrapper function that will replace the original function.
    # It accepts any number of positional (*args) and keyword (**kwd) arguments.
    def wrappers(*args, **kwd):
        # Store the original function's name for use in log messages.
        func_name = func.__name__
        class_name = func.__qualname__
        # Record the start time using a high-resolution performance counter.
        start_time = perf_counter_ns()
        # Begin a try-except block to handle any potential errors during execution.
        try:
            # Log an informational message indicating the start of the function's execution.
            logger.info(
                f"[{class_name}]=>[{func_name}] Starting Execution"
            )
            # Execute the original function with its arguments and store the result.
            results = func(*args, **kwd)
            # Record the end time after the function has successfully completed.
            end_time = perf_counter_ns()
            # Calculate the total execution time in milliseconds.
            execute_time = (end_time - start_time) / 1_000_000
            # Log an informational message with the exact execution time.
            logger.info(
                f"[{class_name}]=>[{func_name}] Execution of completed in {execute_time:.2f} ms"
            )
            # Return the result of the original function's execution.
            return results
        # Catch any type of exception that might occur.
        except Exception as e:
            # Record the end time even in case of an error.
            end_time = perf_counter_ns()
            # Calculate the execution time up to the point of the error.
            execute_time = (end_time - start_time) / 1_000_000
            # Log an informational message about the failure. Note: This could be `logger.warning`.
            logger.info(f"Execution of [{class_name}]=>[{func_name}] failed")
            # Log a detailed error message with the exception and its full traceback.
            # `exc_info=True` adds the traceback information to the log.
            logger.error(f"[{class_name}]=>[{func_name}] => {e}", exc_info=True)
            # Return `False` to signal that the function failed.
            return False

    # Return the new wrapper function, which is now the decorated version of the original.
    return wrappers


def log_and_execute_time_without(func):
    """A decorator that logs the execution time of a function that takes no arguments.

    This decorator measures the execution time of the decorated function and logs it.
    It also provides robust error handling by catching exceptions, logging the details
    with a full traceback, and returning a failure status.

    Args:
        func (callable): The function to be decorated. This function must not accept any arguments.

    Returns:
        callable: The wrapped function (a new function with added logging and timing features).
    """

    # Use @wraps to preserve the original function's metadata (name, docstring, etc.).
    @wraps(func)
    # Define the wrapper function that will replace the original function.
    # It does not accept any arguments, matching the behavior of the decorated function.
    def wrappers():
        # Retrieve the name of the original function for clear log messages.
        func_name = func.__name__
        class_name = func.__qualname__
        # Capture the high-resolution start time of the function's execution.
        start_time = perf_counter_ns()
        # Start a try-except block to gracefully handle any potential errors.
        try:
            # Log an informational message to indicate the beginning of execution.
            logger.info(f"[{class_name}]=>[{func_name}] Starting Execution")
            # Call the original function without any arguments and store its return value.
            results = func()
            # Record the end time after a successful execution.
            end_time = perf_counter_ns()
            # Calculate the total execution time and convert it from nanoseconds to milliseconds.
            execute_time = (end_time - start_time) / 1_000_000
            # Log a success message that includes the function's execution time.
            logger.info(
                f"[{class_name}]=>[{func_name}] Execution of completed in {execute_time:.2f} ms"
            )
            # Return the value that the original function returned.
            return results
        # Catch any and all exceptions to prevent the program from crashing.
        except Exception as e:
            # Capture the end time at the moment the exception occurred.
            end_time = perf_counter_ns()
            # Calculate the elapsed time until the error.
            execute_time = (end_time - start_time) / 1_000_000
            # Log a message indicating the function's failure.
            logger.info(f"Execution of [{class_name}]=>[{func_name}] failed")
            # Log a detailed error message with the exception and its full traceback for debugging.
            logger.error(f"[{class_name}]=>[{func_name}] => {e}", exc_info=True)
            # Return False to signify that the function did not complete successfully.
            return False

    # Return the new wrapper function, which is now the decorated version of the original.
    return wrappers
