


## Data Lakes in the AWS Cloud
Data Lakes are not a specific technology. They can be implemented using many types of file storage systems. In AWS, the most common way to store files is in S3, so we can implement data lakes using S3 storage.

## S3 Data Lakes and Spark on AWS
Like the Hadoop Distributed File System, AWS created S3, the Simple Storage Service. S3 buckets are an abstraction of storage similar to HDFS. They make it possible to store an almost unlimited amount of data and files.

S3 doesn't require the maintenance required by most file storage systems. It is relatively easy to use. The very top level of S3 is called an S3 Bucket. Within a bucket, you can keep many directories and files.

Because S3 has almost unlimited storage capacity and is very inexpensive, it is the ideal location to store data for your data lake. Compared with the cost of other more sophisticated data locations such as RDS, and EC2, S3 is much cheaper. There is no compute cost associated with S3 by default. So if you just need a place to store large amounts of files, this is a great place for them.


## Using Spark on AWS
When you want to rent a cluster of machines on AWS to run Spark, you have several choices:

### EMR - 
EMR is an AWS managed Spark service a scalable set of EC2 machines already configured to run Spark. You don't manage the systems, only configure the necessary cluster resources.

### EC2 - 
Use AWS Elastic Compute (EC2) machines and install and configure Spark and HDFS yourself.

### Glue -
Glue is a serverless Spark environment with added libraries like the Glue Context and Glue Dynamic Frames. It also interfaces with other AWS data services like Data Catalog and AWS Athena.


![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/b1fa3b90-cc9a-4f63-85a8-6cab4a3afc6f)

![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/696ae8bd-1843-453c-b6a2-124e3545ac00)

- Routing Table
A routing table is an entity that stores the network paths to various locations. For example, it will store the path to S3 from within your VPC. You'll need a routing table to configure with your VPC Gateway. You will most likely only have a single routing table if you are using the default workspace.

- VPC Gateway
Your cloud project runs resources within a Virtual Private Cloud (VPC). This means your Glue Job runs in a Secure Zone without access to anything outside your Virtual Network. For security reasons, this is very sensible. You don't want your glue job accessing resources on the internet, for example, unless you specifically require it.

A VPC Gateway is a network entity that gives access to outside networks and resources. Since S3 doesn't reside in your VPC, you need a VPC Gateway to establish a secure connection between your VPC and S3. This allows your Glue Job, or any other resources within the VPC, to utilize S3 for data storage and retrieval.

- S3 Gateway Endpoint
By default, Glue Jobs can't reach any networks outside of your Virtual Private Cloud (VPC). Since the S3 Service runs in different network, we need to create what's called an S3 Gateway Endpoint. This allows S3 traffic from your Glue Jobs into your S3 buckets. Once you have created the endpoint, your Glue Jobs will have a network path to reach S3.

- S3 Buckets
Buckets are storage locations within AWS, that have a hierarchical directory-like structure. Once you create an S3 bucket, you can create as many sub-directories, and files as you want. The bucket is the "parent" of all of these directories and files.


![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/f61db511-fe17-467a-bc1f-759f0fecd5de)


[Spark Repo](https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises)


![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/436e32a5-1b06-4fbe-95bd-10f2f1746057)




![image](https://github.com/shekharbiswas/DE-AWS/assets/32758439/cd5a869d-9ca9-4d86-b33d-83195068bc4a)


