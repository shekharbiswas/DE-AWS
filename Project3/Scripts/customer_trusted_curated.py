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

# Script generated for node customer_trusted
customer_trusted_node1706998301673 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="customer_trusted",
    transformation_ctx="customer_trusted_node1706998301673",
)

# Script generated for node accelerometer_landing
accelerometer_landing_node1706999856980 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="accelerometer_landing",
    transformation_ctx="accelerometer_landing_node1706999856980",
)

# Script generated for node Join
customer_trusted_node1706998301673DF = customer_trusted_node1706998301673.toDF()
accelerometer_landing_node1706999856980DF = (
    accelerometer_landing_node1706999856980.toDF()
)
Join_node1706998152576 = DynamicFrame.fromDF(
    customer_trusted_node1706998301673DF.join(
        accelerometer_landing_node1706999856980DF,
        (
            customer_trusted_node1706998301673DF["email"]
            == accelerometer_landing_node1706999856980DF["user"]
        ),
        "left",
    ),
    glueContext,
    "Join_node1706998152576",
)

# Script generated for node SQL Query
SqlQuery519 = """
select distinct customerName, email, phone, birthDay, serialNumber, registrationDate, lastUpdateDate, shareWithResearchAsOfDate, shareWithPublicAsOfDate, shareWithFriendsAsOfDate from joined_table ;
"""
SQLQuery_node1706992556126 = sparkSqlQuery(
    glueContext,
    query=SqlQuery519,
    mapping={"joined_table": Join_node1706998152576},
    transformation_ctx="SQLQuery_node1706992556126",
)

# Script generated for node Amazon S3
AmazonS3_node1706994085059 = glueContext.getSink(
    path="s3://project3shekhar/customer_curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1706994085059",
)
AmazonS3_node1706994085059.setCatalogInfo(
    catalogDatabase="project3shekhar", catalogTableName="customer_curated"
)
AmazonS3_node1706994085059.setFormat("json")
AmazonS3_node1706994085059.writeFrame(SQLQuery_node1706992556126)
job.commit()
