# Spark is designed to provide distributed computing power by distributing data across multiple nodes in a cluster and processing it in parallel. This parallel processing capability enables Spark to handle large volumes of data efficiently and perform computations much faster compared to traditional single-node processing systems. Spark achieves this through its resilient distributed dataset (RDD) abstraction and its advanced execution engine, which optimizes task execution and resource utilization across the cluster.
from pyspark.sql import SparkSession
import pandas as pd 

# Create a SparkSession 
spark = SparkSession.builder.appName("Spark-Starter").getOrCreate()

# test set up
data = [("James", 24),("Smith", 19),("Williams", 35)]
df = spark.createDataFrame(data, ["Name","Age"])
# Displays the content of the DataFrame
df.show()

