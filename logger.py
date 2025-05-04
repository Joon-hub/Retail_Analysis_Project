class Log4j(object):
    def __init__(self, spark):
        self.logger = spark._jvm.org.apache.log4j.LogManager.getLogger("retail_analysis")
    def info(self, message):
        self.logger.info(message)
    def warn(self, message):
        self.logger.warn(message)
    def error(self, message):
        self.logger.error(message)
