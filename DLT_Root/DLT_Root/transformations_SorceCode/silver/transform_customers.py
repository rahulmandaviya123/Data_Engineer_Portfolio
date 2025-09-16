from pyspark.sql.functions import * 
from pyspark.sql.types import *
import dlt

#create destination silver table
dlt.create_streaming_table(
 name = "customers_enr"
)

@dlt.view 
def customers_enr_trns():
    df = spark.readStream.table("customers_stg")
    df = df.withColumn("customer_name",upper(col("customer_name")))  
    return df

dlt.create_auto_cdc_flow(
    target = "customers_enr",
    source = "customers_enr_trns",
    keys =["customer_id"],
    sequence_by= "last_updated",
    stored_as_scd_type = 1
)
