import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming._
import org.apache.spark.sql.types._
import com.mongodb.spark._
import com.mongodb.spark.sql._
import com.mongodb.spark.config._
import com.mongodb.spark.MongoSpark





case class stock_data(symbol:String,name:String,exchange:String,currency:String,datetime:String,open:String,
high:String,low:String,close:String,volume:String,previous_close:String,change:String,percent_change:String,
average_volume:String,fifty_two_week:String)

//case class StockData()
object StreamHandler {
	def main(args: Array[String]) {
 
        val spark = SparkSession
			.builder
			.appName("Stream Handler")
            // .config("spark.mongodb.input.uri", "mongodb://localhost:27017/twelve.stocks?readPreference=primaryPreferred")
            // .config("spark.mongodb.output.uri", "mongodb://localhost:27017/twelve.stocks")
            .getOrCreate()

        // val spark_mongo = SparkSession
		// 	.builder
		// 	.appName("Stream Handler")
        //     .config("spark.mongodb.input.uri", "mongodb://localhost:27017/twelve.stocks?readPreference=primaryPreferred")
        //     .config("spark.mongodb.input.readPreference.name", "secondaryPreferred")
        //     .config("spark.mongodb.output.uri", "mongodb://localhost:27017/twelve.stocks")
        //     .config("spark.mongodb.output.collection","stocks")
        //     .config("spark.mongodb.input.collection","stocks")
        //     .getOrCreate()
            val spark_mongo = SparkSession
            .builder
            .config("spark.mongodb.input.uri","mongodb://localhost:27017/") 
            .config("spark.mongodb.input.collection","stocks" ) 
            .getOrCreate()




        // val readConfig = ReadConfig(Map("uri" -> "mongodb://127.0.0.1/test.myCollection"))
        // val writeConfig = WriteConfig(Map("uri" -> "mongodb://127.0.0.1/test.myCollection"))


        val schema1 = StructType(List(
StructField("symbol", StringType, true),
StructField("name", StringType, true),
StructField("exchange", StringType, true),
StructField("currency", StringType, true),
StructField("datetime", StringType, true),
StructField("open",StringType, true),
StructField("high", StringType, true),
StructField("low", StringType, true),
StructField("close", StringType, true),
StructField("volume", StringType, true),
StructField("previous_close", StringType, true),
StructField("change", StringType, true),
StructField("percent_change",StringType, true),
StructField("average_volume", StringType, true),
StructField("fifty_two_week",StringType,true)
)
)


        import spark.implicits._



        val inputDF = spark
			.readStream
			.format("kafka") 
			.option("kafka.bootstrap.servers", "localhost:9092,localhost:9093,localhost:9094")
			.option("subscribe", "stockmarket")
			.load()
            .select($"value" cast "string" as "json")
            .select(from_json($"json", schema1) as "data")
            .select("data.*")

        //val df = MongoSpark.load(spark)

        // MongoSpark.save(df.writeStream.mode(SaveMode.Overwrite))
        //df.printSchema()


        //val rawDF = inputDF.selectExpr("CAST(value AS STRING)").as[String]


        
        // var stagedf = inputDF.toDF().coalesce(1)
        // stagedf.printSchema()
        //val newdf = inputDF.union(inputDF)

        // MongoSpark.save(stagedf.writeStream.mode(SaveMode.Overwrite))
//        MongoSpark.save(stagedf.write.option("collection", "stockdata").mode("overwrite"))

//         val mongoDbFormat = "com.stratio.datasource.mongodb"
//         val mongoDbDatabase = "mongodatabase"
//         val mongoDbCollection = "mongodf"

//         val mongoDbOptions = Map(
//     MongodbConfig.Host -> "localhost:27017",
//     MongodbConfig.Database -> mongoDbDatabase,
//     MongodbConfig.Collection -> mongoDbCollection
// )
//     stagedf.write
//     .format(mongoDbFormat)
//     .mode(SaveMode.Append)
//     .options(mongoDbOptions)
//     .save()
        

        //inputDF.printSchema()                           
        //inputDF.write.format("mongo").mode("append").save()
        // var query = inputDF
        // .writeStream
        // .outputMode("update")
        // .option("truncate", "false")
        // .format("console")
        // .start()

        //val df = MongoSpark.load(sparkSession = spark_mongo).toDF()
        //MongoSpark.save(df)
        //MongoSpark.save(df.write.option("collection", "stocks").mode("overwrite").format("mongo"))





        //MongoSpark.save(inputDF.write.mode(SaveMode.Overwrite))
        //MongoSpark.save(inputDF.write.mode("overwrite"), writeConfig)
        //.trigger(ProcessingTime.create("40 seconds"))
        // var query = inputDF
        // .writeStream
        // .format("com.mongodb.spark.sql.DefaultSource")
        // .outputMode("append")
        // .start()
    //    val pathstring = "/home/marcus/data_for_db"
    //    val query = inputDF.writeStream
    //   .format("json")
    //   .option("path", pathstring)
    //   .outputMode("append")
    //   .trigger(Trigger.ProcessingTime("40 seconds"))
    //   .start()
    val block_sz = 8
    val query = inputDF
            .writeStream
            //.format("console")
            .outputMode("append")
            .format("json")
            .option("json.block.size", block_sz)
            .partitionBy("currency")
            .option("path", "/data_for_db/")
            .option("checkpointLocation", "/chkpoint_dir/")
            .start()


        query.awaitTermination()
    }   
}