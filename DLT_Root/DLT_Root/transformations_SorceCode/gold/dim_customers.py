import dlt
from pyspark.sql.functions import *

# Create empty sreaming table

dlt.create_streaming_table(
    name = "dim_customers"
)

# AUTO CDC FLOW

dlt.create_auto_cdc_flow(
    target = "dim_customers",
    source = "customers_enr_trns",
    keys =["customer_id",],
    sequence_by= "last_updated",
    stored_as_scd_type=2
)