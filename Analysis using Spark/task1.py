#!/usr/bin/env python3

#importing modules
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.functions import col
import sys

spark_context = SparkContext.getOrCreate()
sql_context = SQLContext(spark_context)

#taking command line arguements as input
country = sys.argv[1].strip()
city_file = sys.argv[2].strip()

#reading csv file
data = sql_context.read.csv(city_file,header=True)
data = data.cache()
#typecasting
data = data.withColumn("AverageTemperature",data.AverageTemperature.cast("double"))
data = data.filter(data.Country==country).select('City',"AverageTemperature")
data_avg = data.groupby("City").avg("AverageTemperature")
data_avg = data_avg.withColumnRenamed("avg(AverageTemperature)","avgTemp_allTym")
data_avg = data_avg.withColumnRenamed("City","City2")
data = data.join(data_avg,data.City ==  data_avg.City2,"inner")
data = data.filter(data.AverageTemperature > data.avgTemp_allTym)
data = data.groupby('City').count().sort(col("City")).collect()
#printing out collected table in required format.
for i in data:
    print(str(i[0])+'\t'+str(i[1]))
