import sys 
from lib import Utils, DataManipulation, DataReader
from pyspark.sql.functions import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an environment (local, test, or prod)")
        sys.exit(-1)

    job_run_env = sys.argv[1]
    
    print("Creating Spark Session")
    spark = Utils.get_spark_session(job_run_env)
    print("Created Spark Session")
    
    print("Reading orders and customers Data")
    orders_df = DataReader.read_orders(spark,job_run_env)
    customers_df = DataReader.read_customers(spark,job_run_env)
    
    print("Filtering Closed Orders")
    orders_df = DataManipulation.filter_closed_orders(orders_df)

    print("Joining Orders and Customers")
    joined_df = DataManipulation.join_orders_customers(orders_df,customers_df)

    print("Counting States")
    state_count_df = DataManipulation.count_orders_state(joined_df)

    print("Displaying Results")
    state_count_df.show()

    spark.stop()

    print("Job Completed")

    