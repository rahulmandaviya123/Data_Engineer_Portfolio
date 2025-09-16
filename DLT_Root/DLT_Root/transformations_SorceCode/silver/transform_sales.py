import dlt
from pyspark.sql.functions import * 

 
dlt.create_streaming_table(
 name = "sales_enr"
)

@dlt.view
def sales_enr_trns():
    df = spark.readStream.table("sales_stg")
    df1 = df.withColumn("Total_Amount", col("quantity") * col("amount"))
    return df1 
 
dlt.create_auto_cdc_flow(
    target = "sales_enr",
    source = "sales_enr_trns",
    keys =["sales_id"],
    sequence_by= "sale_timestamp",
    stored_as_scd_type=1
)
