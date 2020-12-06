from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import json
from pyspark.sql.functions import col,struct
from pyspark.sql import Row



def Process(rdd):
	if not rdd.isEmpty():
		global ss
		df = ss.createDataFrame(rdd,schema=["created_at", "id",'id_str',"text"])
		df.show()
		df.write.saveAsTable(name ="default.tweets_for_analysis", format="hive", mode="append")


sc = SparkContext("local[*]", "stonks")
ssc = StreamingContext(sc, 5)

ss = SparkSession.builder.appName("footballdata").config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()

kafkastream = KafkaUtils.createStream(ssc, "localhost:2181", "stonks",{"stonks":1})


parsed = kafkastream.map(lambda x: json.loads(x[1]))

filtered = parsed.map(lambda x : (x.get("created_at"), x.get("id"), x.get("id_str"),x.get("text")))
filtered.foreachRDD(Process)


ssc.start()
ssc.awaitTermination()