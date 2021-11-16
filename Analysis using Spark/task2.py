#!/usr/bin/env python3

from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.functions import col, isnull ,isnan
import sys

spark_context = SparkContext.getOrCreate()
sql_context = SQLContext(spark_context)

city_file = sys.argv[1].strip()
global_file = sys.argv[2].strip()

data = sql_context.read.csv(city_file,header=True)
data = data.cache()
data = data.withColumn("AverageTemperature",data.AverageTemperature.cast("float"))
data = data.groupBy("dt","Country").max("AverageTemperature").sort("dt")
data = data.withColumnRenamed("max(AverageTemperature)","maxTemp")

data_global = sql_context.read.csv(global_file,header=True)
data_global = data_global.cache()
data_global = data_global.withColumnRenamed("dt","dt2")
data_global = data_global.withColumn("LandAverageTemperature",data_global.LandAverageTemperature.cast("float"))
data_global = data_global.select("dt2","LandAverageTemperature")
3
data = data.join(data_global, data.dt ==  data_global.dt2, "inner")
data = data.filter(data.maxTemp > data.LandAverageTemperature)
data = data.groupby('Country').count().sort(col("Country")).collect()

for i in data:
    print(str(i[0])+'\t'+str(i[1]))