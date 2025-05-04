from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import col

def filter_closed_orders(orders_df):
    return orders_df.filter(col('order_status') == 'CLOSED')

def join_orders_customers(orders_df, customers_df):
    return orders_df.join(
        customers_df,
        orders_df["order_customer_id"] == customers_df["customer_id"],
        "inner"
    )

def count_orders_state(joined_df):
    return joined_df.groupBy('state').count()

def filter_order_generic(orders_df, status):
    return orders_df.filter(col('order_status') == status)