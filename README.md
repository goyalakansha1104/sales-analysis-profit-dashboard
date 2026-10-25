# Sales Analysis and Profit Dashboard Using MySQL, Python, and Excel

Welcome to the **Sales Analysis and Profit Dashboard** project! This is a beginner-friendly college mini-project designed to demonstrate end-to-end data processing: storing data in a relational database (**MySQL**), analyzing it with **Python**, and generating a clean business dashboard in **Excel**.

---

## 📁 Project Structure

Below is the layout of the project and the purpose of every file:

```text
Sales Analysis project/
├── .env.example            <- Template for database credentials (safe to share)
├── README.md               <- Project documentation and step-by-step guide
├── requirements.txt        <- List of Python packages required for the project
├── main.py                 <- Main entry point to run the entire project
├── database.py             <- Handles MySQL database connection and queries
├── analysis.py             <- Business logic (revenue, profit, top products, trends)
├── excel_report.py         <- Generates formatted Excel reports and dashboard charts
├── sql/
│   ├── create_tables.sql   <- SQL queries to set up database schema & tables
│   └── insert_sample_data.sql <- SQL queries to insert sample sales data
└── output/                 <- Folder where generated Excel reports will be saved
```

---

## 📄 File Descriptions

| File / Folder | Purpose |
| :--- | :--- |
| **`main.py`** | The central program script. Runs the workflow step-by-step: connects to MySQL, fetches data, performs calculations, and exports the Excel dashboard. |
| **`database.py`** | Contains functions to connect to your MySQL server, execute SQL queries, and load query results into Python (using Pandas DataFrames). |
| **`analysis.py`** | Performs data analysis such as calculating total revenue, total profit, profit margins, monthly sales trends, and identifying top-performing products. |
| **`excel_report.py`** | Takes the analyzed data and writes it into an Excel workbook (`.xlsx`) with formatting, summary cards, tables, and charts. |
| **`requirements.txt`** | Lists third-party Python libraries needed (such as `pandas`, `mysql-connector-python`, and `openpyxl`) so they can be installed with a single command. |
| **`.env.example`** | An example configuration file showing what environment variables are needed (e.g., MySQL host, user, password, port). |
| **`sql/create_tables.sql`** | SQL script that creates the project database and necessary tables (`categories`, `products`, `customers`, and `sales_orders`). |
| **`sql/insert_sample_data.sql`**| SQL script with mock sales transactions, products, and customer records to test the project right away. |
| **`output/`** | The destination folder where generated `.xlsx` spreadsheets and reports will be saved. |

---

## 🛠️ High-Level Project Workflow

1. **Database Layer (MySQL)**: Stores raw sales data, product catalogs, customer details, and cost prices.
2. **Data Pipeline Layer (Python)**: Fetches data via SQL, calculates key performance metrics (Revenue, Cost, Profit, Profit Margin %).
3. **Reporting Layer (Excel)**: Automatically creates a formatted executive summary dashboard in Microsoft Excel.

