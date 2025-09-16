import dlt

#customer Expectations

customers_rules ={
    "rule1":"customer_id IS NOT NULL",
    "rule2":"customer_name IS NOT NULL"
}

#Ingesting customers

@dlt.table
@dlt.expect_all_or_drop(customers_rules)
def customers_stg():
    df = spark.readStream.table("dlt_rahul.source.customers")
    return df