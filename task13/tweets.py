from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import json



if __name__== "__main__":

# Create Session
	sc = SparkContext("local[*]","TwitterData")
	ssc = StreamingContext(sc,5)

	ss = SparkSession.builder.appName("TwitterData").config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()
	kafkaStream = KafkaUtils.createStream(ssc, "localhost:2181","kafkatopic", {"kafkatopic" :1 })

	# Parse the Tweets
	parsed = kafkaStream.map(lambda y: json.loads(y[1])).filter(lambda y: y.get("lang") == "en") \
	.map(lambda y: (y.get("id"),y.get("text")))


	def process(rdd):
		if not rdd.isEmpty():
			global ss
			df = ss.createDataFrame(rdd, schema=["id", "text"])
			df.show()
			df.write.saveAsTable(name ="default.tweets", format="hive", mode="append")

	# Write parsed tweets to Hive
	parsed.foreachRDD(process)



	ssc.start()
	ssc.awaitTermination()