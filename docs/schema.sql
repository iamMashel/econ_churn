-- 📦 Customers Table
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    first_order_date DATE,
    region VARCHAR(50),
    gender VARCHAR(10),
    birth_year INT
);

-- 🛒 Orders Table
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    order_date DATE,
    quantity INT,
    price DECIMAL(10,2),
    discount DECIMAL(10,2),
    payment_method VARCHAR(30),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 📋 Products Table
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    category VARCHAR(50),
    subcategory VARCHAR(50),
    product_name VARCHAR(100),
    brand VARCHAR(50)
);

-- 🔁 Returns Table
CREATE TABLE returns (
    order_id VARCHAR(10),
    return_date DATE,
    reason VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 🌐 Sessions Table
CREATE TABLE sessions (
    session_id VARCHAR(12) PRIMARY KEY,
    customer_id VARCHAR(10),
    session_start DATETIME,
    session_duration_min DECIMAL(5,2),
    pages_viewed INT,
    device VARCHAR(20),
    source VARCHAR(30),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 📢 Campaigns Table
CREATE TABLE campaigns (
    customer_id VARCHAR(10),
    campaign_id VARCHAR(20),
    campaign_type VARCHAR(30),
    date_sent DATE,
    clicked BOOLEAN,
    converted BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 📝 Reviews Table
CREATE TABLE reviews (
    review_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    rating INT,
    review_text TEXT,
    review_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
