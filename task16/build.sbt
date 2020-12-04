name := "StreamHandler"
version := "1.0"
scalaVersion := "2.11.8"
// https://mvnrepository.com/artifact/org.mongodb.spark/mongo-spark-connector



libraryDependencies ++= Seq(
    "org.apache.spark" %% "spark-core" % "2.3.2" % "provided",
     "org.mongodb.spark" % "mongo-spark-connector_2.11" % "2.3.4",
    "org.apache.spark" %% "spark-sql" % "2.3.2" % "provided"
)
