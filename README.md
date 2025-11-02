# 🛠️ Minmathii

Minmathii is an automation project designed to **update empty fields automatically with synthesized values** for the Tamil Nadu Government’s portal.  
It uses Selenium to interact with the website and Pandas to process data from Excel files.

---

## 🚀 Features

-   Automatically detects and fills empty fields such as:
    -   Date of Birth
    -   Contact Number
    -   Aadhaar Number
    -   Address
    -   Husband Name
    -   PDS Number
    -   and more...
-   Generates **realistic random data** for missing fields.
-   Reads data dynamically from Excel.
-   Submits the form and handles confirmation pop-ups automatically.

---

## 🧰 Tech Stack

-   **Python 3.x**
-   **Selenium**
-   **Pandas**
-   **WebDriver (ChromeDriver)**
-   **datetime** and **random** for data generation

---

## ⚙️ Setup & Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/<your-username>/Minmathii.git
    cd Minmathii

    ```

2. **Install dependencies**

```bash
pip install -r requirements.txt

3. **Place your dataset**
Save your Excel file as dataset.xlsx in the same directory.

4. **Run the project**
python main.py
```
