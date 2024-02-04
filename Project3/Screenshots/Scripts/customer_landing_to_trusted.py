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

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1706992519632 = glueContext.create_dynamic_frame.from_catalog(
    database="project3shekhar",
    table_name="customer_landing",
    transformation_ctx="AWSGlueDataCatalog_node1706992519632",
)

# Script generated for node SQL Query
SqlQuery632 = """
select * from myDataSource where shareWithResearchAsOfDate is not null;
"""
SQLQuery_node1706992556126 = sparkSqlQuery(
    glueContext,
    query=SqlQuery632,
    mapping={"myDataSource": AWSGlueDataCatalog_node1706992519632},
    transformation_ctx="SQLQuery_node1706992556126",
)

# Script generated for node Amazon S3
AmazonS3_node1706994085059 = glueContext.getSink(
    path="s3://project3shekhar/customer_trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1706994085059",
)
AmazonS3_node1706994085059.setCatalogInfo(
    catalogDatabase="project3shekhar", catalogTableName="customer_trusted"
)
AmazonS3_node1706994085059.setFormat("json")
AmazonS3_node1706994085059.writeFrame(SQLQuery_node1706992556126)
job.commit()
