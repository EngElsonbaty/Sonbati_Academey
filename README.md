# Sonbati_Academey

A comprehensive desktop application designed to manage all operational aspects of a real-world pharmaceutical medicine academy. The system provides a holistic solution for managing employees, students, finances, and data analysis.

---

## **Project Overview**

Sonbati_Academey is a holistic system dedicated to managing all operational aspects of a real-world pharmaceutical academy. The project's scope extends beyond basic data management to include financial analysis and comprehensive reporting, making it an essential tool for academy administration.

---

## **Key Features**

* **Holistic Management:** Manages all core entities, including **employees**, **students**, and **courses**.
* **Financial Oversight:** Tracks and analyzes **profits** and **losses**, providing a clear financial picture of the academy's operations.
* **Data-Driven Insights:** Performs **data analysis** on key metrics to aid in strategic decision-making and operational improvements.
* **Automated Database Generation:** Automatically creates a structured database with all necessary tables.
* **Detailed Performance Logging:** Generates a detailed log file (`Execute_time.log`) that tracks execution times and pinpoints any data insertion failures with timestamps and relevant information.
* **Graphical User Interface (GUI):** Provides a user-friendly graphical interface for all administrative tasks.

---

## **Getting Started**

### **Prerequisites**

This project is built using **Python 3.9** or newer and is designed to run on **Ubuntu/Linux** systems. All required libraries are listed in `requirements.txt`.

### **Installation**

1. **Clone the repository:**

    ```bash
    git clone https://github.com/EngElsonbaty/Sonbati_Academey.git
    cd Sonbati_Academey
    ```

2. **Activate the virtual environment:**

    ```bash
    source .venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## **Usage**

To launch the desktop application, use the following command from the project's root directory:

```bash
Sonbati_Academey/.venv/bin/python main.py
```

---

## **Project Structure**

Below is the updated project directory structure based on the latest file listing, with a brief description of each folder and file:

```
Sonbati_Academey/
├── asstes/                 # Contains static assets like images, icons, or other resources used in the GUI
├── config/                 # Configuration files for the application (e.g., database settings, app configurations)
├── controllers/            # Logic for handling user inputs and coordinating between views and models
├── core/                   # Core functionality and business logic of the application
├── log/                    # Directory for log files, including execution logs
├── modules/                # Reusable modules or libraries specific to the project
├── services/               # Service layer for handling external integrations or backend logic
├── views/                  # GUI components and templates for the desktop application
├── Execute_time.log        # Log file tracking execution times and data insertion failures
├── main.py                 # Entry point of the application
├── README.md               # Project documentation (this file)
├── requirements.txt        # List of Python dependencies for the project
├── test1.py                # Temporary or experimental script for testing purposes
├── test.py                 # Main test script for testing application functionality
└── .venv/                  # Virtual environment for Python dependencies
├── .git/                   # Git repository metadata (not included in distribution)
```

### **Directory and File Descriptions**

- **asstes/**: Stores static assets like images, fonts, or icons used in the GUI of the application.
* **config/**: Contains configuration files such as database connection settings or application parameters.
* **controllers/**: Includes scripts that handle user interactions, process inputs, and manage communication between the UI and backend logic.
* **core/**: Houses the core business logic and essential functionalities of the academy management system.
* **log/**: Stores log files, including `Execute_time.log`, which tracks performance metrics and errors.
* **modules/**: Contains modular code or libraries that can be reused across different parts of the application.
* **services/**: Manages external services or backend logic, such as database queries or API integrations.
* **views/**: Includes the GUI components, such as Tkinter or PyQt templates, for the desktop application.
* **Execute_time.log**: A log file that records execution times and details of any data insertion failures with timestamps.
* **main.py**: The main script to launch the application, serving as the entry point.
* **README.md**: The main documentation file for the project, providing an overview and instructions.
* **requirements.txt**: Lists all required Python libraries and their versions for the project.
* **test1.py**: A temporary or experimental script, likely used for testing small features or debugging.
* **test.py**: The primary test script for validating the application's functionality.
* **.venv/**: The virtual environment directory containing Python dependencies and configurations.
* **.git/**: Contains Git repository metadata (not included in the final distribution).

---

## **Author**

**Name:** Mahmoud Elsonbaty  
**Version:** 1.0.0  
**GitHub:** [EngElsonbaty](https://github.com/EngElsonbaty)  
**LinkedIn:** [Mahmoud Elsonbaty](https://www.linkedin.com/in/mahmoud-elsonbaty-50a393315/)  
**Facebook:** [Mahmoud Elsonbaty](https://www.facebook.com/Eng.Elsonbty12)  
**Email:** [mahmoudelsonbaty43@gmail.com](mailto:mahmoudelsonbaty43@gmail.com)  
**Phone:** 01064480148  
**Copyright:** © 2025 Mahmoud Elsonbaty. All rights reserved.

---

## **License**

This project is open-source and available under the MIT License.

**Copyright (c) 2025 Mahmoud Elsonbaty**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
