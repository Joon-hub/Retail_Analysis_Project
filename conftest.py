from lib.Utils import get_spark_session
import pytest

# FIXTURE

# fixture helps in reduce repetitive code 
# it will create spark session (setup code) once and can be used in multiple tests
# fixture should be added as an argument to the function (signature)
@pytest.fixture
def spark():
    """
    This fixture creates a SparkSession 
    object and returns it.
    """
    spark_session =  get_spark_session('LOCAL')
    yield spark_session
    spark_session.stop()

@pytest.fixture
def expected_results(spark):
    result_schema = "state string, count int"
    return spark.read\
        .format('csv')\
        .option('ignoreLeadingWhiteSpace', True)\
        .option('ignoreTrailingWhiteSpace', True)\
        .option('header', 'true')\
        .schema(result_schema)\
        .load('/Users/sudhirjoon/Desktop/SummitMittalCourse/RetailAnalysisProject/data/test_results/state_aggregate.csv')
