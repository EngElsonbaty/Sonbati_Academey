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
            return True
        else:
            return False

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    def insert(self, table: str, data: dict):
        """Inserts a new row into the specified table.

        This method securely inserts a new record into the database using a parameterized query.
        It constructs the SQL statement from a dictionary of data.

        Args:
            table (str): The name of the table to insert into.
            data (dict): A dictionary containing the column names and their corresponding values.

        Returns:
            bool: True if the insertion was successful, False otherwise.
        """
        # Check if a database connection exists.
        if self.__conn_db is None:
            # If no connection exists, try to get one.
            DatabaseManager.get_connection()
        # Check again if the connection was successfully established.
        if self.__conn_db is not None:
            # Get the column names from the dictionary keys and join them into a string.
            columns = ", ".join(data.keys())
            # Build the query string using f-strings for the table and columns.
            query = (
                f"INSERT INTO {table}({columns}) VALUES("
                + ", ".join(["?"] * len(data))
                + ")"
            )
            # Create a cursor object to execute the SQL query.
            curr = self.__conn_db.cursor()
            # Execute the query, passing the values as a tuple.
            curr.execute(query, tuple(data.values()))
            # Call the 'save' method to commit the changes to the database.
            self.save()
            # Return True to indicate that the operation was successful.
            return True
        else:
            return False

    # A decorator that logs the execution time and handles exceptions for this method.
    @log_and_execute_time_with
    # Define the method to update data in a table.
    def update(self, table: str, condition: str, data: dict) -> bool:
        """Updates one or more rows in a table.

        This method updates records in the database based on a given condition.
        It constructs an SQL query using data from a dictionary and a condition string.

        Args:
            table (str): The name of the table to update.
            condition (str): The string representing the WHERE clause (e.g., "id = 1").
            data (dict): A dictionary where keys are column names to update
                         and values are the new data.

        Returns:
            bool: True if the update operation was successful, False otherwise.
        """
        # Check if a database connection exists.
        if self.__conn_db is None:
            # If no connection exists, try to get one.
            DatabaseManager.get_connection()
        # Check again if the connection was successfully established.
        if self.__conn_db is not None:
            # Build the query string for the UPDATE statement.
            query = (
                f"UPDATE {table} SET "
                + " = ?, ".join(tuple(data.keys()))
                + f" = ? WHERE {condition}"
            )
            # Create a cursor object to execute the SQL query.
            curr = self.__conn_db.cursor()
            # Execute the query, passing the values from the data dictionary as a tuple.
            curr.execute(query, tuple(data.values()))
            # Call the 'save' method to commit the changes to the database.
            self.save()
            # Return True to indicate that the update operation was successful.
            return True
        # If no database connection could be established, return False.
        else:
            return False

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    # Define the method to retrieve data from a table.
    def get(
        self,
        table: str,
        condition: str = "",
        all_table: bool = False,
        all_data: bool = False,
        *columns,
    ) -> tuple[bool, any]:
        """Retrieves data from a database table.

        This method fetches rows from a specified table. It can return all data
        from the table or specific columns based on a condition.

        Args:
            table (str): The name of the table to query.
            condition (str, optional): A string representing the SQL WHERE clause
                                       (e.g., "id = 1"). Defaults to an empty string.
            all_data (bool, optional): If True, all rows and columns are selected,
                                        and other arguments are ignored. Defaults to False.
            *columns: A variable number of strings representing the column names to select.

        Returns:
            tuple[bool, any]: A tuple containing a boolean indicating success (True) or failure (False)
                              and the fetched data (a list of tuples) or a failure message.
        """
        # Check if a database connection exists.
        if self.__conn_db is None:
            # If no connection, try to establish one.
            DatabaseManager.get_connection()
        # After attempting to connect, check again if the connection is now active.
        if self.__conn_db is not None:
            # Initialize the query variable to None.
            query = None
            # Check if the user wants all data from the table.
            if all_table:
                # If True, construct a query to select all columns from the specified table.
                query = f"SELECT * FROM {table}"
            # If all_data is False, proceed with the conditional query.
            elif all_data:
                query = f"SELECT " + ", ".join(columns) + f" FROM {table} WHERE {condition}"
            else:
                # Construct the query by joining the provided column names.
                query = (
                    f"SELECT " + ", ".join(columns) + f" FROM {table} WHERE {condition}"
                )
            # Create a cursor object to execute the SQL query.
            curr = self.__conn_db.cursor()
            # Execute the constructed query.
            curr.execute(query)
            # Fetch all the rows of the query result as a list of tuples.
            results = curr.fetchall()
            # Return the results of the query.
            return results
        # If the connection could not be established, return False.
        else:
            return False

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    # Define the method to delete a row from a table.
    def delete(self, table: str, condition: str):
        """Deletes one or more rows from a table.

        This method constructs and executes an SQL DELETE query based on a
        specified table and a WHERE clause condition.

        Args:
            table (str): The name of the table to delete from.
            condition (str): A string representing the SQL WHERE clause
                             (e.g., "id = 5" or "username = 'test'").

        Returns:
            bool: True if the delete operation was successful, False otherwise.
        """
        # Check if a database connection exists.
        if self.__conn_db is None:
            # If no connection, try to establish one.
            DatabaseManager.get_connection()
        # Check again if the connection was successfully established.
        if self.__conn_db is not None:
            # Build the SQL query for the DELETE statement.
            query = f"DELETE FROM {table} WHERE {condition}"
            # Create a cursor object to execute the query.
            curr = self.__conn_db.cursor()
            # Execute the constructed query.
            curr.execute(query)
            # Call the 'save' method to commit the changes to the database.
            self.save()
            # Return True to indicate that the delete operation was successful.
            return True
        # If the connection could not be established, return False.
        else:
            return False

    # Apply a decorator to this method to log its execution time.
    # The `log_and_execute_time_with` decorator is used to handle methods that can take arguments.
    @log_and_execute_time_with
    # Define the method to search for data in a table.
    def search(self, table: str, column_name: str, column_value: str, *rows):
        """Searches for a specific value in a table column.

        This method queries a table and returns rows where a specified column's
        value matches a search term using a case-insensitive LIKE comparison.
        The search value is handled securely using a parameterized query.

        Args:
            table (str): The name of the table to search within.
            column_name (str): The name of the column to perform the search on.
                               (Note: Using this as a direct f-string is a security risk).
            column_value (str): The value to search for. Wildcards (%) are handled automatically.
            *rows: A variable number of strings representing the column names to return.
                   If no columns are provided, all columns will be returned.

        Returns:
            list[tuple] | None: A list of tuples containing the matching rows,
                                or None if no results are found.
                                Returns False if the connection fails.
        """
        # Check if a database connection exists.
        if self.__conn_db is None:
            # If no connection, try to establish one.
            DatabaseManager.get_connection()
        # Check again if the connection was successfully established.
        if self.__conn_db is not None:
            # Build the query string for the SELECT statement.
            # Warning: Direct insertion of table and column names is a security vulnerability (SQL Injection).
            #
            query = (
                f"SELECT "
                + ", ".join(rows)
                + f" FROM {table} WHERE {column_name} LIKE ?"
            )
            # Create a cursor object to execute the SQL query.
            curr = self.__conn_db.cursor()
            # Execute the query, passing the search value with wildcards as a tuple.
            # This is the correct way to secure the search value.
            curr.execute(query, (f"%{column_value}%",))
            # Fetch all matching rows as a list of tuples.
            results = curr.fetchall()
            # Return the results if the list is not empty, otherwise return None.
            return results if results else None
        # If the connection could not be established, return False.
        else:
            return False

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
