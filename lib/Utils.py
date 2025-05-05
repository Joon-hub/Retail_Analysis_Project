# it will help create spark session

from pyspark.sql import SparkSession
from lib.ConfigReader import get_spark_config

def get_spark_session(env):
    """
    This function creates a SparkSession object.

    The env parameter decides which Spark configuration to use and whether to use
    the local master or a remote one.
    """
    if env == 'LOCAL':
        # In local mode, the master is set to 'local[*]' which means as many
        # threads as there are cores on the local machine will be used.
        # The SparkSession is given the name 'retail-local'.
        return SparkSession.builder \
            .appName("RetailAnalysis") \
            .config(conf=get_spark_config(env)) \
            .config("spark.driver.extraJavaOptions", 
                    "-Dlog4j.configuration=file:log4j.properties") \
            .master("local[2]") \
            .getOrCreate()
    else:
        # In non-local mode, the master is set to whatever is specified in the
        # Spark configuration file for the given environment.
        return SparkSession.builder \
            .config(conf=get_spark_config(env)) \
            .enableHiveSupport() \
            .getOrCreate()
    
