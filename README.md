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

## License

The **AcademyManager** software is available under multiple licensing options to suit different use cases. Below, we outline the available licenses, their terms, and their implications. By using this software, you agree to comply with the terms of the chosen license.

### 1. Proprietary License (Default)

This is the default license for **AcademyManager**, ensuring maximum protection for the intellectual property of Mahmoud Elsonbati. This license is suitable for private or commercial use with explicit permission from the author.

**International Software License Agreement**  
This Agreement is entered into as of September 18, 2025, between Mahmoud Elsonbati (the "Licensor"), located in Egypt, and any user or entity (the "Licensee").

#### RECITALS

WHEREAS, the Licensor has developed the **AcademyManager** software and related documentation (the "Software");  
WHEREAS, the Licensee wishes to use the Software under the terms herein.

#### 1. DEFINITIONS

- **Software**: The AcademyManager application in object code form, including student management, course enrollment, employee management, financial operations, and analytics features.
* **License**: A non-exclusive, non-transferable right to use the Software for internal purposes only.
* **Territory**: Worldwide, subject to applicable export control laws (e.g., U.S. Export Administration Regulations).
* **Designated Environment**: Python 3.x on Ubuntu Linux or compatible systems.
* **Documentation**: User manuals, installation guides, and other materials provided with the Software.

#### 2. GRANT OF LICENSE

The Licensor grants the Licensee a non-exclusive, non-transferable license to:  
(a) Use the Software solely for internal educational academy management at the Licensee's designated locations;  
(b) Make one backup copy for archival purposes, retaining all copyright notices.  
This License is limited to the number of users specified (initially 1 for evaluation).

#### 3. RESTRICTIONS

The Licensee shall not:  
(a) Copy, modify, adapt, translate, reverse engineer, decompile, or disassemble the Software;  
(b) Distribute, sublicense, rent, lease, or loan the Software to any third party;  
(c) Use the Software in a service bureau, time-sharing, or outsourcing environment;  
(d) Remove or alter any proprietary notices, labels, or marks;  
(e) Export or re-export the Software in violation of applicable international export laws.

#### 4. OWNERSHIP AND INTELLECTUAL PROPERTY

The Licensor retains all right, title, and interest in the Software, including all copyrights, patents, trade secrets, and trademarks. This Agreement does not transfer any ownership rights to the Licensee.

#### 5. CONFIDENTIALITY

The Licensee agrees to maintain the confidentiality of the Software and not disclose it to third parties. This obligation survives termination of the Agreement.

#### 6. WARRANTY AND LIMITATION OF LIABILITY

The Software is provided "AS IS" without warranties of any kind, express or implied, including merchantability or fitness for a particular purpose. The Licensor shall not be liable for any indirect, incidental, or consequential damages arising from use of the Software, including loss of data (e.g., student records).

#### 7. TERM AND TERMINATION

This License is effective until terminated. The Licensor may terminate upon breach by the Licensee. Upon termination, the Licensee must destroy all copies of the Software.

#### 8. GOVERNING LAW AND DISPUTE RESOLUTION

This Agreement shall be governed by the laws of Egypt and international treaties (e.g., Berne Convention). Any disputes shall be resolved in the courts of Cairo, Egypt, or through international arbitration under the rules of the International Chamber of Commerce (ICC) for cross-border disputes.

#### 9. MISCELLANEOUS

This Agreement constitutes the entire understanding between the parties and supersedes all prior agreements. It may only be amended in writing signed by both parties. If any provision is held invalid, the remainder shall remain in effect.

**Licensor**: Mahmoud Elsonbati  
**Date**: September 18, 2025

### 2. Open Source License Options

For users interested in contributing to or using **AcademyManager** in an open-source context, the following licenses are available upon request from the Licensor. Each license has different terms, and you must contact Mahmoud Elsonbati to obtain permission for open-source use.

#### a. MIT License

The MIT License is a permissive open-source license, allowing users to use, modify, and distribute the Software with minimal restrictions, provided they include the original copyright notice.

**Example MIT License**:  

```
Copyright (c) 2025 Mahmoud Elsonbati

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Use Case**: Suitable for developers who want to use **AcademyManager** in personal or commercial projects while giving credit to Mahmoud Elsonbati. Example: React (github.com/facebook/react) uses MIT License.

#### b. GNU General Public License (GPL) v3

The GPLv3 is a copyleft license, requiring any derivative works to be distributed under the same license, ensuring the Software remains open source.

**Example GPLv3 License**:  

```
AcademyManager - A Python-based educational academy management system
Copyright (C) 2025 Mahmoud Elsonbati

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

**Use Case**: Ideal for open-source communities who want to contribute to **AcademyManager** and ensure all modifications remain open source. Example: Linux Kernel (github.com/torvalds/linux) uses GPLv2.

#### c. Apache License 2.0

The Apache License is a permissive license with additional patent protection, suitable for commercial use with attribution.

**Example Apache License 2.0**:  

```
Copyright 2025 Mahmoud Elsonbati

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

**Use Case**: Suitable for companies integrating **AcademyManager** into larger systems, with patent protections. Example: Apache Kafka (github.com/apache/kafka) uses Apache 2.0.

#### d. BSD 3-Clause License

The BSD License is another permissive license, similar to MIT but with an additional clause preventing endorsement without permission.

**Example BSD 3-Clause License**:  

```
Copyright (c) 2025 Mahmoud Elsonbati. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.
```

**Use Case**: Suitable for academic or research use of **AcademyManager**, with attribution. Example: Pandas (github.com/pandas-dev/pandas) uses BSD 3-Clause.

### Choosing a License

- **Proprietary License**: Use this for maximum control and commercial purposes. Contact Mahmoud Elsonbati for licensing inquiries.
* **MIT License**: Use for permissive open-source use with minimal restrictions.
* **GPLv3**: Use for open-source projects where modifications must remain open source.
* **Apache 2.0**: Use for commercial projects with patent protection.
* **BSD 3-Clause**: Use for permissive use with no endorsement clause.
To use an open-source license, you must obtain explicit permission from Mahmoud Elsonbati via [email](mailto:mahmoudelsonbaty43@gmail.com).

### International Considerations

The Proprietary License complies with international intellectual property laws, including:
* **Berne Convention**: Ensures copyright protection in 180+ countries.
* **GDPR (EU)**: Protects student and employee data processed by **AcademyManager**.
* **U.S. Export Controls**: Complies with export regulations for software distribution.
Disputes will be resolved under Egyptian law or ICC arbitration for international parties.
