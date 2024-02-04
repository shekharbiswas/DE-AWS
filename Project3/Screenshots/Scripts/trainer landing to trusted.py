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

# Script generated for node trainer landing
trainerlanding_node1707038372837 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="step_trainer_landing",
    transformation_ctx="trainerlanding_node1707038372837",
)

# Script generated for node customer curated
customercurated_node1707038374192 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="customer_curated",
    transformation_ctx="customercurated_node1707038374192",
)

# Script generated for node Join
trainerlanding_node1707038372837DF = trainerlanding_node1707038372837.toDF()
customercurated_node1707038374192DF = customercurated_node1707038374192.toDF()
Join_node1707038540025 = DynamicFrame.fromDF(
    trainerlanding_node1707038372837DF.join(
        customercurated_node1707038374192DF,
        (
            trainerlanding_node1707038372837DF["serialnumber"]
            == customercurated_node1707038374192DF["serialnumber"]
        ),
        "leftsemi",
    ),
    glueContext,
    "Join_node1707038540025",
)

# Script generated for node SQL Query
SqlQuery541 = """
select count(*) from DataSource
"""
SQLQuery_node1707039909310 = sparkSqlQuery(
    glueContext,
    query=SqlQuery541,
    mapping={"DataSource": Join_node1707038540025},
    transformation_ctx="SQLQuery_node1707039909310",
)

# Script generated for node SQL Query
SqlQuery542 = """
select * from DataSource
"""
SQLQuery_node1707038620915 = sparkSqlQuery(
    glueContext,
    query=SqlQuery542,
    mapping={"DataSource": Join_node1707038540025},
    transformation_ctx="SQLQuery_node1707038620915",
)

# Script generated for node Amazon S3
AmazonS3_node1707038681435 = glueContext.getSink(
    path="s3://project3shekhar/step_trainer_trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1707038681435",
)
AmazonS3_node1707038681435.setCatalogInfo(
    catalogDatabase="project3shekhar", catalogTableName="step_trainer_trusted"
)
AmazonS3_node1707038681435.setFormat("json")
AmazonS3_node1707038681435.writeFrame(SQLQuery_node1707038620915)
job.commit()
