# Project

Build a data lakehouse solution for sensor data that trains a machine learning model.

Spark and AWS Glue allow you to process data from multiple sources, categorize the data, and curate it to be queried in the future for multiple purposes. In this project you will directly use the skills you have used, including some of the code you have already written.

AWS Glue, AWS S3, Python, and Spark, create or generate Python scripts to build a lakehouse solution in AWS that satisfies these requirements from the STEDI data scientists.

![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/5934fc4e-2eab-4901-aca5-c574c2391d0b)

## Device / Data Source

There are sensors on the device that collect data to train a machine learning algorithm to detect steps. It also has a companion mobile app that collects customer data and interacts with the device sensors. The step trainer is just a motion sensor that records the distance of the object detected.


### Data

Customer Records (from fulfillment and the STEDI website):

**Location:** AWS S3 Bucket URI - s3://project3shekhar/customers/

Contains the following fields:

- serialnumber
- sharewithpublicasofdate
- birthday
- registrationdate
- sharewithresearchasofdate
- customername
- email
- lastupdatedate
- phone
- sharewithfriendsasofdate


Step Trainer Records (data from the motion sensor):

**Location:** AWS S3 Bucket URI - s3://project3shekhar/step_trainer/

Contains the following fields:
sensorReadingTime
serialNumber
distanceFromObject
Accelerometer Records (from the mobile app):

**Location:** AWS S3 Bucket URI - s3://project3shekhar/accelerometer/

Contains the following fields:

- timeStamp
- user
- x
- y
- z

  
## Tasks

- To simulate the data coming from the various sources, create S3 directories for customer_landing, step_trainer_landing, and accelerometer_landing zones, and copy the data there as a starting point.

- Create two Glue tables for the two landing zones. customer_landing.sql and accelerometer_landing.sql script (DDL) shows the schema of these 2 tables.

- Query those tables using Athena, and screenshot of each one showing the resulting data have been saved in Screenshots folder.

## Data Zones

In a data lake architecture, the use of landing, trusted, and curated zones serves specific purposes that can significantly enhance the quality, reliability, and usability.

- **Landing Zone:** The landing zone is often the first point of storage for raw data as it enters the data lake. It serves as a staging area where data from various sources is collected, often in its original format. This zone provides a place to accumulate data before processing occurs ( generally).

- **Trusted Zone:** After data has been landed, it may then be processed and moved to the trusted zone. In this zone, data is cleansed, validated, and often transformed into a structured format. This can include operations like deduplication, handling missing or incorrect data, and ensuring our customers have approved their data to be used for research purposes.

- **Curated Zone:** The curated zone is where data is further transformed, often to meet the specific needs of a particular analysis, application, or group of users. This may involve operations like aggregating data, creating derived metrics, or combining multiple datasets. The curated zone should provide data that's ready-to-use for OLAP team.

The Data Science team has done some preliminary data analysis and determined that the Accelerometer Records each match one of the Customer Records. They would like you to create 2 AWS Glue Jobs that do the following:

- Sanitize the Customer data from the Website (Landing Zone) and only store the Customer Records who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called customer_trusted.

- Sanitize the Accelerometer data from the Mobile App (Landing Zone) - and only store Accelerometer Readings from customers who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called accelerometer_trusted.

-  Verify your Glue job is successful and only contains Customer Records from people who agreed to share their data. Query your Glue customer_trusted table with Athena and take a screenshot of the data. Name the screenshot customer_trusted(.png,.jpeg, etc.).

Data Scientists have discovered a data quality issue with the Customer Data. The serial number should be a unique identifier for the STEDI Step Trainer they purchased. However, there was a defect in the fulfillment website, and it used the same 30 serial numbers over and over again for millions of customers! Most customers have not received their Step Trainers yet, but those who have, are submitting Step Trainer data over the IoT network (Landing Zone). The data from the Step Trainer Records has the correct serial numbers.

The problem is that because of this serial number bug in the fulfillment data (Landing Zone), we don’t know which customer the Step Trainer Records data belongs to.

The Data Science team would like you to write a Glue job that does the following:

- Sanitize the Customer data (Trusted Zone) and create a Glue Table (Curated Zone) that only includes customers who have accelerometer data and have agreed to share their data for research called customers_curated.

Finally, create two Glue Studio jobs that do the following tasks:

- Read the Step Trainer IoT data stream (S3) and populate a Trusted Zone Glue Table called step_trainer_trusted that contains the Step Trainer Records data for customers who have accelerometer data and have agreed to share their data for research (customers_curated).
  
- Create an aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data, and make a glue table called machine_learning_curated.

Refer to the relationship diagram below to understand the desired state.

![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/e12d16e9-ac59-4384-838e-0b57633d1079)



