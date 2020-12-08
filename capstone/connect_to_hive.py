from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession, HiveContext

sc = SparkContext("local[*]", )
ssc = StreamingContext(sc,10)
ss = SparkSession.builder \
	.appName("Nothing") \
	.master("local[*]") \
	.config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
	.config("hive.metastore.uris", "thrift://localhost:9083") \
	.enableHiveSupport().getOrCreate()


column_names = "created_at|id|id_str|text"

df = ss.createDataFrame(
  [
    tuple('' for i in column_names.split("|"))
  ],
  column_names.split("|")
).where("1=0")


#df = sparkSession.createDataFrame()
# Write into Hive
#df.write.saveAsTable('example')



df_load = ss.sql('SELECT * FROM default.tweets_for_analysis')
df_load.show()
results = df_load.collect()
print(results)



ssc.start()
ssc.awaitTermination()



#####/home/marcus/opt/hive-2.3.5/conf