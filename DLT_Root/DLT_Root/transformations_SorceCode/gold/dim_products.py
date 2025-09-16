import dlt
from pyspark.sql.functions import *

# Create empty sreaming table

dlt.create_streaming_table(
    name = "dim_products"
)

# AUTO CDC FLOW

dlt.create_auto_cdc_flow(
    target = "dim_products",
    source = "products_enr_trns",
    keys =["product_id",],
    sequence_by= "last_updated",
    stored_as_scd_type=2
)