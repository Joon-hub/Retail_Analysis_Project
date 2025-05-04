import configparser
from pyspark import SparkConf

# Loads application-level (non-Spark) configuration settings from `configs/application.conf`.
# Reads the section that matches the provided environment (`env`).
# Returns a dictionary of configuration key-value pairs.
def get_app_config(env):
    config = configparser.ConfigParser()
    config.read('configs/application.conf')
    app_conf = {}
    for (key,val) in config.items(env):
        app_conf[key] = val
    return app_conf

# laoding pyspark configs and creating a spark conf object

# What it does:
# 	Loads Spark-specific configuration settings from `configs/pyspark.conf`.
# 	Reads the section that matches the provided environment (`env`).
# 	Sets each configuration as a property on a `SparkConf` object.
# 	Returns the configured `SparkConf` object.
def get_spark_config(env):
    """
    Loads Spark-specific configuration settings from `configs/pyspark.conf`, 
    reads the section matching the provided environment (`env`), and sets each 
    configuration as a property on a `SparkConf` object.
    Args:
        env (str): The environment name (`LOCAL`, `TEST`, or `PROD`) to read 
                   configurations for.
    Returns:
        SparkConf: A configured `SparkConf` object with settings for the specified environment.
    """
    config = configparser.ConfigParser()
    config.read('configs/pyspark.conf')
    spark_conf = SparkConf()
    for (key,val) in config.items(env):
        spark_conf.set(key, val)
    return spark_conf