-- Run in Pig Grunt. Assumed CSV column order: order_id,state,amount.
-- Change the schema to match the actual Amazon dataset supplied by your college.

amazon = LOAD 'amazon.csv'
USING PigStorage(',')
AS (order_id:chararray, state:chararray, amount:double);

-- Remove a header row if present.
amazon_clean = FILTER amazon BY state IS NOT NULL AND state != 'state';

DESCRIBE amazon_clean;
DUMP amazon_clean;

state_groups = GROUP amazon_clean BY state;
DESCRIBE state_groups;
DUMP state_groups;

-- Count orders per state.
orders_per_state = FOREACH state_groups GENERATE
    group AS state,
    COUNT(amazon_clean) AS order_count;
DUMP orders_per_state;

-- Total sales per state.
sales_per_state = FOREACH state_groups GENERATE
    group AS state,
    SUM(amazon_clean.amount) AS total_sales;
DUMP sales_per_state;

-- Average order amount per state.
average_per_state = FOREACH state_groups GENERATE
    group AS state,
    AVG(amazon_clean.amount) AS average_order_amount;
DUMP average_per_state;

STORE sales_per_state INTO 'amazon_state_sales' USING PigStorage(',');
