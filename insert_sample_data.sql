-- ==============================================================
-- Sales Analysis and Profit Dashboard
-- Sample Data Insertion
-- ==============================================================

USE sales_analysis_db;

-- 1. Insert Categories
INSERT INTO categories (category_name) VALUES
('Electronics'),
('Office Supplies'),
('Furniture'),
('Accessories')
ON DUPLICATE KEY UPDATE category_name = category_name;

-- 2. Insert Products (Cost and Selling Price)
INSERT INTO products (product_name, category_id, unit_cost, unit_price) VALUES
('Wireless Mouse', 1, 12.00, 25.00),
('Mechanical Keyboard', 1, 35.00, 70.00),
('27-inch Monitor', 1, 140.00, 220.00),
('Ergonomic Office Chair', 3, 90.00, 180.00),
('Standing Desk', 3, 160.00, 310.00),
('Gel Pens Pack', 2, 3.50, 8.00),
('Notebook Spiral Bound', 2, 2.00, 5.50),
('USB-C Multiport Hub', 4, 18.00, 39.99),
('Laptop Backpack', 4, 22.00, 49.99),
('Noise Cancelling Headphones', 1, 85.00, 160.00);

-- 3. Insert Customers
INSERT INTO customers (customer_name, email, city, state) VALUES
('Aarav Sharma', 'aarav.sharma@example.com', 'Mumbai', 'Maharashtra'),
('Priya Patel', 'priya.patel@example.com', 'Ahmedabad', 'Gujarat'),
('Rohan Verma', 'rohan.verma@example.com', 'Bengaluru', 'Karnataka'),
('Sneha Reddy', 'sneha.reddy@example.com', 'Hyderabad', 'Telangana'),
('Ananya Gupta', 'ananya.gupta@example.com', 'Delhi', 'Delhi');

-- 4. Insert Sales Records
INSERT INTO sales (order_date, customer_id, product_id, quantity, discount_percent) VALUES
('2024-01-15', 1, 1, 2, 0.00),
('2024-01-18', 2, 3, 1, 5.00),
('2024-01-22', 3, 4, 1, 10.00),
('2024-02-05', 4, 2, 2, 0.00),
('2024-02-12', 5, 8, 3, 0.00),
('2024-02-20', 1, 5, 1, 5.00),
('2024-03-02', 2, 10, 1, 0.00),
('2024-03-10', 3, 6, 10, 0.00),
('2024-03-14', 4, 7, 5, 0.00),
('2024-03-22', 5, 9, 2, 5.00),
('2024-04-05', 1, 3, 2, 10.00),
('2024-04-18', 2, 1, 4, 0.00),
('2024-04-25', 3, 10, 2, 5.00);

