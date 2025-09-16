# # Creating end to end pipeline basic
# import dlt
# from pyspark.sql.functions import *

# @dlt.table(
#     name = "staging_order"
# )

# def staging_order():
#    df = spark.readStream.table("dlt_rahul.source.orders")
#    return df

# #creating Tranformed Area

# @dlt.view(
#     name = "transformed_orders"
# )
# def transformed_orders():
#   df = spark.readStream.table("staging_order")
#   df = df.withColumn("order_status", lower(col('order_status')))
#   return df

# # creating aggrigated area

# @dlt.table(
#     name = "aggregated_orders"
# )
# def aggregated_orders():
#   df = spark.readStream.table("transformed_orders")
#   df = df.groupBy("order_status").count().orderBy(col("count").desc())
#   return df
