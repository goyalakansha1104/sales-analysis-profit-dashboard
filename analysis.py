"""Analyze sales data retrieved from MySQL."""

import pandas as pd
from database import fetch_sales_data


def analyze_sales():
    df = fetch_sales_data()

    if df.empty:
        raise ValueError("No sales data found in the database.")

    for column in ["quantity", "revenue", "profit"]:
        df[column] = pd.to_numeric(df[column])

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    monthly = df.groupby("month", as_index=False).agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        orders=("sale_id", "count")
    )

    category = df.groupby("category_name", as_index=False).agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )

    top_products = (
        df.groupby("product_name", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
            units_sold=("quantity", "sum")
        )
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    summary = {
        "total_revenue": round(float(df["revenue"].sum()), 2),
        "total_profit": round(float(df["profit"].sum()), 2),
        "total_orders": int(df["sale_id"].nunique()),
        "units_sold": int(df["quantity"].sum()),
        "average_order_value": round(
            float(df["revenue"].sum() / df["sale_id"].nunique()), 2
        )
    }

    return {
        "raw_data": df,
        "summary": summary,
        "monthly": monthly,
        "category": category,
        "top_products": top_products
    }


if __name__ == "__main__":
    result = analyze_sales()

    print("\n=== SALES SUMMARY ===")
    for key, value in result["summary"].items():
        print(f"{key}: {value}")

    print("\n=== MONTHLY SALES ===")
    print(result["monthly"].to_string(index=False))

    print("\n=== CATEGORY ANALYSIS ===")
    print(result["category"].to_string(index=False))

    print("\n=== TOP PRODUCTS ===")
    print(result["top_products"].to_string(index=False))