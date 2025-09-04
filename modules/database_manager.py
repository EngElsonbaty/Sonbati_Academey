# The user requested documentation and comments for the provided Python code without any modifications.
# The following code is a Python class for managing a SQLite database connection,
# attempting to implement the Singleton design pattern.
import os  # Used for interacting with the operating system, specifically for file paths.
import sys  # Provides access to system-specific parameters and functions.
import sqlite3  # The standard library module for working with SQLite databases.

# Get the absolute path of the project's root directory.
# This ensures that modules can be imported correctly regardless of where the script is executed.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Add the project's root directory to the Python path if it's not already there.
# This allows for module imports (e.g., from 'core' or 'modules') to work correctly.
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now, import the log_utils module from the core directory.
from core.log_utils import log_and_execute_time_with, log_and_execute_time_without


class DatabaseManager:
    """Manages a single connection to a SQLite database, following the Singleton pattern."""

    # A private class variable to store the single database connection instance.
    # It is initialized to None and will hold the connection object once created.
    __conn_db = None

    # The constructor method for the class.
    def __init__(self):
        """Initializes the DatabaseManager.

        It ensures that only one instance of the class can be created.
        If an instance already exists, it raises an exception.
        """
        # Check if the private connection variable has already been set.
        if self.__conn_db is not None:
            # If an instance exists, raise an exception to prevent a second one from being created.
            raise Exception(
                "An instance already exists. A second instance cannot be created."
            )
        else:
            # If this is the first instance, print a message indicating creation.
            print("Create Instance")

    # Apply a decorator to this static method to log its execution time.
    # The `log_and_execute_time_without` decorator is used because this method takes no arguments.
    @log_and_execute_time_without
    @staticmethod
    def get_path():
        """Returns the absolute path to the SQLite database file."""
        # Builds the path by joining the directory of the current file with the subdirectories and filename.
        # os.path.dirname(__file__) gets the directory of the current script.
        # os.path.dirname(os.path.dirname(__file__)) moves up two directories to reach the project root.
        return os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "config", "database", "app.db"
        )

    # Apply a decorator to this static method to log its execution time.
    # The `log_and_execute_time_without` decorator is used because this method takes no arguments.
    @log_and_execute_time_without
    @staticmethod
    def get_connection():
        """Connects to the database if a connection does not already exist."""
        # Check if the class's private connection variable is None.
        if DatabaseManager.__conn_db is None:
            # If there is no active connection, establish a new one.
            DatabaseManager.__conn_db = sqlite3.connect(DatabaseManager.get_path())

    # Apply a decorator to this property to log its execution time.
    # The `log_and_execute_time_without` decorator is used as a property method does not take arguments beyond `self`.
    @log_and_execute_time_without
    @property
    def save(self):
        """Placeholder for a method to commit changes to the database."""
        pass

    # Apply a decorator to this property to log its execution time.
    # The `log_and_execute_time_without` decorator is used as a property method does not take arguments beyond `self`.
    @log_and_execute_time_without
    @property
    def close(self):
        """Placeholder for a method to close the database connection."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def create_table(self):
        """Placeholder for a method to create a new table."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def insert(self):
        """Placeholder for a method to insert data."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def delete(self):
        """Placeholder for a method to delete data."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def update(self):
        """Placeholder for a method to update data."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def get(self):
        """Placeholder for a method to retrieve a specific row or rows."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def search(self):
        """Placeholder for a method to search for data."""
        pass

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def get_last_row(self):
        """Placeholder for a method to get the last row from a table."""
        pass


# Create a single instance of the DatabaseManager class.
# This will execute the __init__ method and print "Create Instance".
db = DatabaseManager()

# Call the get_connection method directly from the class.
# This is the correct way to call a static method.
DatabaseManager.get_connection()


print(db._DatabaseManager__conn_db)
