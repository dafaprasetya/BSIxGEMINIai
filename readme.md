# BSIxGEMINIai

**BSIxGEMINIai by dafa_prstya**

## Features

- **Auto Collect Cookie Gemini AI**: Automatically collects cookies from Gemini AI (Google login required).
- **Answer Accuracy**: Provides answers with 90% accuracy.

## How To Use

1. **Install Microsoft Edge**:
   - Download and install Microsoft Edge from the [official website](https://www.microsoft.com/edge).

2. **Install Python**:
   - Download and install Python from the [official website](https://www.python.org/downloads/).

3. **Clone the Repository**:
   - Open a terminal and run the following command:
     ```sh
     git clone https://github.com/dafaprasetya/BSIxGEMINIai
     cd BSIxGEMINIai
     ```

4. **Install Requirements**:
   - Run the following command to install the required Python packages:
     ```sh
     pip install -r requirements.txt
     ```

5. **Run the Application**:
   - Execute the main script:
     ```sh
     python Main.py
     ```

6. **Login with Google**:
   - Follow the instructions to log in with your Google account to receive the cookie.
   - If Google detects Selenium, try the following steps:
     - Change the port.
     - Delete the "ujang shelby" folder.
     - Run the script again.

7. **Wait for 10 Seconds**:
   - Allow the script to initialize.

8. **Get Answers**:
   - Use the `/` command to get answers.

## For Windows Users (if it crashes)

1. **Download Edge WebDriver**:
   - Download Edge WebDriver from the [official website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

2. **Modify the Script**:
   - Change the line:
     ```python
     service=EdgeService(EdgeChromiumDriverManager().install())
     ```
     to:
     ```python
     service="PATH TO EDGEWEBDRIVER"
     ```

## Tested On

- KALI LINUX

Thanks
