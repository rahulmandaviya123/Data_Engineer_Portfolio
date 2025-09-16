'''' Creating streaming table

import dlt

@dlt.table(
    name = 'first_stream_table'
)
def first_stream():
    df = spark.readStream.table("dlt_rahul.source.orders")
    return df

# create materialized view
@dlt.materialized_view
def first_mat_view():
    df = spark.read.table("dlt_rahul.source.orders")
    return df


#create view

@dlt.view(
    name = "first_batch_view"
)
def first_batch_view():
    df = spark.read.table("dlt_rahul.source.orders")
    return df


@dlt.view(
    name = "first_stream_view"
)
def first_stream_view():
    df = spark.readStream.table("dlt_rahul.source.orders")
    return df
'''