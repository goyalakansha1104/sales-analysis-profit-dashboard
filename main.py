"""
Sales Analysis and Profit Dashboard
Main entry point
"""

from analysis import analyze_sales
from excel_report import generate_excel_report


def main():
    print("=" * 50)
    print(" SALES ANALYSIS AND PROFIT DASHBOARD")
    print("=" * 50)

    try:
        print("\nStep 1: Connecting to MySQL and analyzing sales...")

        result = analyze_sales()
        summary = result["summary"]

        print("\n--- SALES SUMMARY ---")
        print(f"Total Revenue : {summary['total_revenue']:.2f}")
        print(f"Total Profit  : {summary['total_profit']:.2f}")
        print(f"Total Orders  : {summary['total_orders']}")
        print(f"Units Sold    : {summary['units_sold']}")
        print(
            f"Average Order Value: "
            f"{summary['average_order_value']:.2f}"
        )

        print("\nStep 2: Generating Excel report...")

        generate_excel_report()

        print("\nSUCCESS! Project completed.")
        print("Check output/sales_report.xlsx for your report.")

    except Exception as error:
        print("\nSomething went wrong.")
        print(f"Error details: {error}")


if __name__ == "__main__":
    main()