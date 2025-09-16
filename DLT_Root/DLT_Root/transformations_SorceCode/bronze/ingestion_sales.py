import dlt

sales_rules ={
    "rule1":"sales_id IS NOT NULL"
}

# Create empty streaming table for append flow
dlt.create_streaming_table(
    name = "sales_stg",
    expect_all_or_drop=sales_rules
)

# creating east flow
@dlt.append_flow(target="sales_stg")
def east_sales():
    df = spark.readStream.table("dlt_rahul.source.sales_east")
    return df

# creating west flow
@dlt.append_flow(target="sales_stg")
def west_sales():
    df = spark.readStream.table("dlt_rahul.source.sales_west")
    return df
