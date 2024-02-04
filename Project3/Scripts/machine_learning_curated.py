import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node acc trusted
acctrusted_node1707041185096 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="accelerometer_trusted",
    transformation_ctx="acctrusted_node1707041185096",
)

# Script generated for node step trainer trusted
steptrainertrusted_node1707041185761 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="step_trainer_trusted",
    transformation_ctx="steptrainertrusted_node1707041185761",
)

# Script generated for node SQL Query
SqlQuery571 = """
select * from st inner join at 
on st.sensorReadingTime = at.timeStamp
"""
SQLQuery_node1707041275014 = sparkSqlQuery(
    glueContext,
    query=SqlQuery571,
    mapping={
        "st": steptrainertrusted_node1707041185761,
        "at": acctrusted_node1707041185096,
    },
    transformation_ctx="SQLQuery_node1707041275014",
)

# Script generated for node SQL Query
SqlQuery572 = """
select count(*) from final
"""
SQLQuery_node1707043089631 = sparkSqlQuery(
    glueContext,
    query=SqlQuery572,
    mapping={"final": SQLQuery_node1707041275014},
    transformation_ctx="SQLQuery_node1707043089631",
)

# Script generated for node Amazon S3
AmazonS3_node1707044152162 = glueContext.getSink(
    path="s3://project3shekhar/ml_curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1707044152162",
)
AmazonS3_node1707044152162.setCatalogInfo(
    catalogDatabase="project3shekhar", catalogTableName="ml_curated"
)
AmazonS3_node1707044152162.setFormat("json")
AmazonS3_node1707044152162.writeFrame(SQLQuery_node1707041275014)
job.commit()
