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


## Scripts

1. customer_landing_to_trusted.py: This script transfers customer data from the 'landing' to 'trusted' zones. It filters for customers who have agreed to share data with researchers.
2. accelerometer_landing_trusted.py:  This script transfers accelerometer data from the 'landing' to 'trusted' zones. It filters for Accelerometer readings from customers who have agreed to share data with researchers.
3. customer trusted to curated.py: This script transfers customer data from the 'trusted' to 'curated' zones. It filters for customers with Accelerometer readings and have agreed to share data with researchers.
4. trainer landing to trusted.py: This script transfers step trainer data from the 'landing' to 'curated' zones. It filters for curated customers with Step Trainer readings.
5. machine_learning_curated.py: This script combines Step Trainer and Accelerometer data from the 'curated' zone into a single table to train a machine learning model.

## Summary

Data lakehouse solution is designed to give STEDI a robust and flexible data infrastructure that allows us to store, clean, and transform vast amounts of data.

- Amazon S3 for storage, enables us to store large amounts of diverse data cost-effectively. The storage can be scaled as per needs.

- AWS Glue, a fully managed extract, transform, and load (ETL) service, is a user-friendly tool for preparing data for high-quality analytics and machine learning.

- Maintain a single source of truth with versioning in S3 will help structure and identify correct data.

Overall, a data lakehouse solution gives easy adaptation to customer needs and changes in business.




