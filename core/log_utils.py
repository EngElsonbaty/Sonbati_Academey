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
    """A decorator that logs the execution time of a function and handles any exceptions."""

    @wraps(func)
    def wrappers(*args, **kwd):
        func_name = func.__name__
        class_name = func.__qualname__
        start_time = perf_counter_ns()
        try:
            logger.info(f"[{class_name}]=>[{func_name}] Starting Execution")
            results = func(*args, **kwd)
            end_time = perf_counter_ns()
            execute_time = (end_time - start_time) / 1_000_000
            logger.info(
                f"[{class_name}]=>[{func_name}] Execution of completed in {execute_time:.2f} ms"
            )
            # تم إضافة هذا الجزء
            if execute_time > 100:
                logger.warning(
                    f"[{class_name}]=>[{func_name}] is taking a very long time: {execute_time:.2f} ms"
                )
            return results
        except Exception as e:
            end_time = perf_counter_ns()
            execute_time = (end_time - start_time) / 1_000_000
            logger.info(f"Execution of [{class_name}]=>[{func_name}] failed")
            # تم إضافة هذا الجزء
            if execute_time > 100:
                logger.warning(
                    f"[{class_name}]=>[{func_name}] is taking a very long time: {execute_time:.2f} ms"
                )
            logger.error(f"[{class_name}]=>[{func_name}] => {e}", exc_info=True)
            return False

    return wrappers


def log_and_execute_time_without(func):
    """A decorator that logs the execution time of a function that takes no arguments."""

    @wraps(func)
    def wrappers():
        func_name = func.__name__
        class_name = func.__qualname__
        start_time = perf_counter_ns()
        try:
            logger.info(f"[{class_name}]=>[{func_name}] Starting Execution")
            results = func()
            end_time = perf_counter_ns()
            execute_time = (end_time - start_time) / 1_000_000
            logger.info(
                f"[{class_name}]=>[{func_name}] Execution of completed in {execute_time:.2f} ms"
            )
            # تم إضافة هذا الجزء
            if execute_time > 100:
                logger.warning(
                    f"[{class_name}]=>[{func_name}] is taking a very long time: {execute_time:.2f} ms"
                )
            return results
        except Exception as e:
            end_time = perf_counter_ns()
            execute_time = (end_time - start_time) / 1_000_000
            logger.info(f"Execution of [{class_name}]=>[{func_name}] failed")
            # تم إضافة هذا الجزء
            if execute_time > 100:
                logger.warning(
                    f"[{class_name}]=>[{func_name}] is taking a very long time: {execute_time:.2f} ms"
                )
            logger.error(f"[{class_name}]=>[{func_name}] => {e}", exc_info=True)
            return False

    return wrappers
