import dlt
from pyspark.sql.functions import * 
from pyspark.sql.types import *

#create destination silver table
dlt.create_streaming_table(
 name = "products_enr"
)

@dlt.view
def products_enr_trns():
    df = spark.readStream.table("products_stg")
    df = df.withColumn("price", col("price").cast("integer"))
    return df

dlt.create_auto_cdc_flow(
    target = "products_enr",
    source = "products_enr_trns",
    keys =["product_id"],
    sequence_by= "last_updated",
    stored_as_scd_type=1
)