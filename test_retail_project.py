import pytest
from lib.Utils import get_spark_session
from lib.DataReader import read_orders, read_customers
from lib.DataManipulation import filter_closed_orders
from lib.DataManipulation import count_orders_state,filter_order_generic
from lib import ConfigReader
from conftest import spark


# Tests
@pytest.mark.transformation
def test_read_customers_df(spark):
    customer_count = read_customers(spark, 'LOCAL').count()
    assert customer_count == 12435

@pytest.mark.transformation
def test_read_orders_df(spark):
    order_count = read_orders(spark, 'LOCAL').count()
    assert order_count == 68884


# Transformations
@pytest.mark.transformation
def test_filter_closed_orders(spark):
    orders_df = read_orders(spark, 'LOCAL')
    closed_orders_count = filter_closed_orders(orders_df).count()
    assert closed_orders_count == 7556
@pytest.mark.config
def test_read_app_config():
    conf = ConfigReader.get_app_config('LOCAL')
    assert conf['orders.file.path'] == 'data/orders.csv'
    assert conf['customers.file.path'] == 'data/customers.csv'

@pytest.mark.data_match
def test_count_order_state(spark,expected_results):
    customers_df = read_customers(spark, 'LOCAL')
    actual_results = count_orders_state(customers_df)
    assert actual_results.collect() == expected_results.collect()

## how to run multiple tests
@pytest.mark.skip()
def test_check_closed_orders_count(spark):
    orders_df = read_orders(spark, 'LOCAL')
    filtered_count = filter_order_generic(orders_df,"CLOSED").count()
    assert filtered_count == 7556

@pytest.mark.skip()
def test_check_PendingPayment_orders_count(spark):
    orders_df = read_orders(spark, 'LOCAL')
    filtered_count = filter_order_generic(orders_df,"PENDING_PAYMENT").count()
    assert filtered_count == 15030

@pytest.mark.skip()
def test_check_Complete_orders_count(spark):
    orders_df = read_orders(spark, 'LOCAL')
    filtered_count = filter_order_generic(orders_df,"COMPLETE").count()
    assert filtered_count == 22900

## parametrize tests
@pytest.mark.latest
@pytest.mark.parametrize("status,count", 
    [
        ("CLOSED", 7556),
        ("PENDING_PAYMENT", 15030),
        ("COMPLETE", 22900)
    ]
)
def test_check_count(spark, status, count):
    orders_df = read_orders(spark, 'LOCAL')
    filtered_count = filter_order_generic(orders_df, status).count()
    assert filtered_count == count