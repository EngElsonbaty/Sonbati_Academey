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
    def __init__(self) -> None:
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
    def get_connection() -> None:
        """Connects to the database if a connection does not already exist."""
        # Check if the class's private connection variable is None.
        if DatabaseManager.__conn_db is None:
            # If there is no active connection, establish a new one.
            DatabaseManager.__conn_db = sqlite3.connect(DatabaseManager.get_path())

    # Apply a decorator to this property to log its execution time.
    # The `log_and_execute_time_without` decorator is used as a property method does not take arguments beyond `self`.
    @log_and_execute_time_with
    # @property
    def save(self) -> None:
        """Placeholder for a method to commit changes to the database."""
        if DatabaseManager.__conn_db is not None:
            DatabaseManager.__conn_db.commit()

    # Apply a decorator to this property to log its execution time.
    # The `log_and_execute_time_without` decorator is used as a property method does not take arguments beyond `self`.
    @log_and_execute_time_without
    @property
    def close(self) -> None:
        """Placeholder for a method to close the database connection."""
        if DatabaseManager.__conn_db is not None:
            DatabaseManager.__conn_db.commit()
            DatabaseManager.__conn_db.close()

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def create_table(self, table: str, columns: dict) -> bool:
        """Placeholder for a method to create a new table."""
        if self.__conn_db is None:
            DatabaseManager.get_connection()
        if self.__conn_db is not None:
            query = f"CREATE TABLE IF NOT EXISTS {table}("
            counter = 0
            for key, value in columns.items():
                query += (
                    f"{key} {value} {", " if counter < (len(columns) - 1) else ")"}"
                )
                counter += 1
            curr = self.__conn_db.cursor()
            curr.execute(query)
            return False

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def insert(self, table: str, data: dict):
        """Placeholder for a method to insert data."""
        if self.__conn_db is None:
            DatabaseManager.get_connection()
        if self.__conn_db is not None:
            columns = ", ".join(data.keys())
            query = (
                f"INSERT INTO {table}({columns}) VALUES("
                + ", ".join(["?"] * len(data))
                + ")"
            )
            curr = self.__conn_db.cursor()
            curr.execute(query, tuple(data.values()))
            self.save()
            return True

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def update(self):
        """Placeholder for a method to update data."""
        if self.__conn_db is None:
            DatabaseManager.get_connection()

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def get(self):
        """Placeholder for a method to retrieve a specific row or rows."""
        if self.__conn_db is None:
            DatabaseManager.get_connection()

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def delete(self):
        """Placeholder for a method to delete data."""
        if self.__conn_db is None:
            DatabaseManager.get_connection()

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def search(self):
        """Placeholder for a method to search for data."""
        if self.__conn_db is None:
            DatabaseManager.get_connection()

    # The user wants documentation and comments for the get_last_row method.
    # The following code is the user's function with added docs and line-by-line comments.

    # Define the method to get the last (highest) ID from a given table.
    # The @log_and_execute_time_with decorator is already applied to this method.
    @log_and_execute_time_with
    def get_last_row(self, table: str, column: str = "id") -> int:
        """Gets the highest ID from a specified table.

        This method queries a database table and retrieves the highest value
        from the specified ID column. It returns 0 if the table is empty.

        Args:
            table (str): The name of the table to query.
            column (str): The name of the ID column (defaults to "id").

        Returns:
            int: The highest ID as an integer, or 0 if the table contains no rows.
        """
        # Initialize the last_id variable to None.
        last_id = None
        # Check if a database connection exists.
        if self.__conn_db is None:
            # If no connection exists, try to establish one using the static method.
            DatabaseManager.get_connection()
        # After attempting to connect, check if the connection is now active.
        if self.__conn_db is not None:
            # Build the SQL query to select the highest ID from the table.
            # This query orders by the specified column in descending order and returns only the first row.
            query = f"SELECT {column} FROM {table} ORDER BY {column} DESC LIMIT 1"
            # Create a cursor object to execute the SQL query.
            curr = self.__conn_db.cursor()
            # Execute the SQL query.
            curr.execute(query)
            # Fetch the single result row. It will be a tuple or None if no rows were returned.
            results = curr.fetchone()
            # Check if the fetched result is None (meaning the table is empty).
            if results == None:
                # If no result was found, set the last_id to 0.
                last_id = 0
            else:
                # If a result was found, get the ID value from the first element of the tuple.
                last_id = results[0]
            # Return the final last_id value.
            return last_id


# Create a single instance of the DatabaseManager class.
# This will execute the __init__ method and print "Create Instance".
db = DatabaseManager()

# Call the get_connection method directly from the class.
# This is the correct way to call a static method.
DatabaseManager.get_connection()

# DatabaseManager.close

last_id = db.get_last_row("users") + 1
users = {
    "id": last_id,
    "emp_id": 3,
    "username": "elsonbaty2",
    "password": "12345",
    # "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
}
print(db.insert("users", users))
print(db._DatabaseManager__conn_db)
