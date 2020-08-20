# Databricks notebook source
# MAGIC %md
# MAGIC ## Download Taxi Dataset

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/taxi_trips.csv https://data.cityofchicago.org/resource/wrvz-psew.csv?%24limit=1000000000

# COMMAND ----------

dbutils.fs.mkdirs(/home/dave.carlson@databricks.com/datasets/chicago/csv)
dbutils.fs.mkdirs(/home/dave.carlson@databricks.com/datasets/chicago/delta)

# COMMAND ----------

dbutils.fs.cp('file:/tmp/taxi_trips.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/csv/taxi_trips.csv')

# COMMAND ----------

