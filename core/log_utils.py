import os
import sys
import time
import logging
from functools import wraps

def log_and_execute_time_with(func):
    @wraps
    def wrappers(*arg, **kwd):
        pass

    return wrappers

def log_and_execute_time_without(func):
    @wraps
    def wrappers():
        pass

    return wrappers