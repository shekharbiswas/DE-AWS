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
