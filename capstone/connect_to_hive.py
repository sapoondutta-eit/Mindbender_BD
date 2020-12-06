from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, HiveContext


sparkSession = (SparkSession
                .builder
                .appName('read-data-from-hive')
                .config("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf())
                .enableHiveSupport()
                .getOrCreate()
                )


column_names = "created_at|id|id_str|text"

df = sparkSession.createDataFrame(
  [
    tuple('' for i in column_names.split("|"))
  ],
  column_names.split("|")
).where("1=0")


#df = sparkSession.createDataFrame()
# Write into Hive
#df.write.saveAsTable('example')

df_load = sparkSession.sql('SELECT * FROM tweets_for_analysis')
df_load.show()
print(df_load.show())