from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import json
from pyspark.sql.functions import col,struct
from pyspark.sql import Row
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import (DoubleType, IntegerType)



def Process(rdd):
	if not rdd.isEmpty():
		global ss
		df = ss.createDataFrame(rdd,schema=["id","text","polarity","subjectivity"])
		# df.withColumn["id"].cast(IntegerType)
		# df.withColumn["polarity"].cast(DoubleType)
		# df.withColumn["subjectivity"].cast(DoubleType)
		# df.createOrReplaceTempView("senti_tweets")
		# ss.sql("select * from senti_tweets").show()
		# df.show()
		df.write.format('jdbc').options(
      url='jdbc:mysql://localhost/tweets',
      driver='com.mysql.jdbc.Driver',
      dbtable='senti_tweets',
      user='root',
      password='password').mode('append').save()



sc = SparkContext("local[*]", "stonks")
ssc = StreamingContext(sc, 5)

ss = SparkSession.builder.master("local").config(conf=SparkConf()).getOrCreate()


# ss = SparkSession.builder.appName("footballdata").config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()

# ss = SparkSession.builder \
#     .appName('stack_overflow') \
#     .config('spark.jars', '/home/marcus/Mindbender_BD/capstone/mysql-connector-java-5.1.49/mysql-connector-java-5.1.49.jar') \
#     .getOrCreate()

kafkastream = KafkaUtils.createStream(ssc, "localhost:2181", "stonks",{"stonks":1})


parsed = kafkastream.map(lambda x: json.loads(x[1]))
parsed.foreachRDD(Process)

#df = parsed.toDF("id","text","polarity","subjectivity")


#DF.write.format("jdbc").option("url", "dbc:mysql://localhost/tweets").option("dbtable", "senti_tweets").option("user", "root").option("password", "password").mode('append').save()


# column_names = "id"|"text"|"polarity"|"subjectivity"

# df = ss.createDataFrame(
#   [
#     tuple('' for i in column_names.split("|"))
#   ],
#   column_names.split("|")
# ).where("1=0")

# filtered = parsed.map(lambda x : (x.get("created_at"), x.get("id"), x.get("id_str"),x.get("text")))
# filtered.foreachRDD(Process)


ssc.start()
ssc.awaitTermination()