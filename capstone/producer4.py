from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import json
from pyspark.sql.functions import col,struct


{
 "created_at": "Wed Oct 10 20:19:24 +0000 2018",
 "id": 1050118621198921728,
 "id_str": "1050118621198921728",
 "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
 "user": {},  
 "entities": {}
}


def Process(rdd):
	if not rdd.isEmpty():
		global ss
		df = ss.createDataFrame(rdd, schema=['created_at', 'id','id_str','text','user','entities'])
		df.show()
		updatedDF = df.withColumn("total_shots", struct(col("shots.total").alias("total")))\
			.withColumn("Shots on Target",struct(col("shots.on").alias("on")))
		updatedDF.show()
		#df.write.saveAsTable(name ="default.football", format="hive", mode="append")


sc = SparkContext("local[*]", "footballdata")
ssc = StreamingContext(sc, 5)

ss = SparkSession.builder.appName("footballdata").config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()

kafkastream = KafkaUtils.createStream(ssc, "localhost:2181",
"footballapi", {"footballapi": 1})


parsed = kafkastream.map(lambda x: json.loads(x[1]))

#parsed.pprint()


api = parsed.map(lambda x: x.get("api"))


topscorers = api.flatMap(lambda x: x.get("topscorers"))

topscorers.pprint()

filtered = topscorers.map(lambda x: (x.get("player_id"), x.get("player_name"),
x.get('position'), x.get('nationality'),x.get("shots")))

filtered.foreachRDD(Process)

ssc.start()
ssc.awaitTermination()