from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import json

def Process(rdd):
	if not rdd.isEmpty():
		global ss
		df = ss.createDataFrame(rdd, schema=['player_id', 'player_name','position','nationality'])
		df.show()
		df.write.saveAsTable(name ="default.football", format="hive", mode="append")


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
x.get('position'), x.get('nationality')))

filtered.foreachRDD(Process)

ssc.start()
ssc.awaitTermination()