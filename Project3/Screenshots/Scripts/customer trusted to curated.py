import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
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

# Script generated for node accc landing
accclanding_node1707036668545 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="accelerometer_landing",
    transformation_ctx="accclanding_node1707036668545",
)

# Script generated for node customer trusted
customertrusted_node1707036670697 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="customer_trusted",
    transformation_ctx="customertrusted_node1707036670697",
)

# Script generated for node Join
customertrusted_node1707036670697DF = customertrusted_node1707036670697.toDF()
accclanding_node1707036668545DF = accclanding_node1707036668545.toDF()
Join_node1707036675803 = DynamicFrame.fromDF(
    customertrusted_node1707036670697DF.join(
        accclanding_node1707036668545DF,
        (
            customertrusted_node1707036670697DF["email"]
            == accclanding_node1707036668545DF["user"]
        ),
        "leftsemi",
    ),
    glueContext,
    "Join_node1707036675803",
)

# Script generated for node SQL Query
SqlQuery451 = """
select * from myDataSource
"""
SQLQuery_node1707036904414 = sparkSqlQuery(
    glueContext,
    query=SqlQuery451,
    mapping={"myDataSource": Join_node1707036675803},
    transformation_ctx="SQLQuery_node1707036904414",
)

# Script generated for node Amazon S3
AmazonS3_node1707037296451 = glueContext.getSink(
    path="s3://project3shekhar/customer_curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1707037296451",
)
AmazonS3_node1707037296451.setCatalogInfo(
    catalogDatabase="project3shekhar", catalogTableName="customer_curated"
)
AmazonS3_node1707037296451.setFormat("json")
AmazonS3_node1707037296451.writeFrame(SQLQuery_node1707036904414)
job.commit()
