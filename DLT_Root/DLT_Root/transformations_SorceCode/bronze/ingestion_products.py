import dlt

#Ingesting Products

#products Expectations

products_rules ={
    "rule1":"product_id IS NOT NULL",
    "rule2":"price >= 0"
}

@dlt.table
@dlt.expect_all_or_drop(products_rules)
def products_stg():
    df = spark.readStream.table("dlt_rahul.source.products")
    return df