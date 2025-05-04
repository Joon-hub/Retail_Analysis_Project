import sys
from lib import Utils, DataManipulation, DataReader
from pyspark.sql.functions import *
from logger import Log4j

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        # Early exit should also be logged
        print("Please provide an environment (local, test, or prod)")
        sys.exit(-1)

    job_run_env = sys.argv[1]

    # Create Spark Session
    spark = Utils.get_spark_session(job_run_env)

    log4jLogger = spark._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger("retail_analysis")


    # Set Spark's internal log level to ERROR to avoid INFO level logs from Spark
    spark.sparkContext.setLogLevel("ERROR")

    # Initialize logger after Spark session
    logger = Log4j(spark)

    logger.info("Created Spark Session")

    # Read Data
    logger.info("Reading orders and customers Data")
    orders_df = DataReader.read_orders(spark, job_run_env)
    customers_df = DataReader.read_customers(spark, job_run_env)

    # Filter Orders
    logger.info("Filtering Closed Orders")
    orders_df = DataManipulation.filter_closed_orders(orders_df)

    # Join Data
    logger.info("Joining Orders and Customers")
    joined_df = DataManipulation.join_orders_customers(orders_df, customers_df)

    # Aggregate
    logger.info("Counting Orders by State")
    state_count_df = DataManipulation.count_orders_state(joined_df)

    # Show Results
    logger.info("Displaying Results")
    state_count_df.show()

    # Cleanup
    spark.stop()
    logger.info("Spark Session stopped")
    logger.info("Job Completed")
