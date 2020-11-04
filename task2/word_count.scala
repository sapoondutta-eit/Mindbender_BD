import scala.io.Source
import scala.collection.immutable.ListMap
import java.io.PrintWriter
import java.io._
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs._
import org.apache.spark.SparkContext._
import org.apache.spark._
import org.apache.spark.deploy.SparkHadoopUtil
import org.apache.spark.sql._
import org.apache.spark.sql.hive.HiveContext
import scala.io._
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import java.io.PrintWriter;





lazy val initialize_file = io.Source.fromFile("/home/marcus/tasks/Shakespeare.txt").getLines.mkString

val remove_punct = initialize_file.replaceAll(""".[\p{Punct}&&[^.]].""", "").toLowerCase()

val split_word = remove_punct.split(" ").map(_.trim)

def count_words (dat : Array[String]) : Map[String, Int] = {
 	dat.toSet.map((word: String) => (word, dat.count(_ == word))).toMap

}


def order_map(dat: Map[String, Int]): Map[String, Int] = {
	return ListMap(dat.toSeq.sortWith(_._2 < _._2):_*)
}

def printing(dat: Map[String, Int]) = {
	for ((k,v) <- dat) printf("%s : %s\n", k , v)
}


def printToFile(f: java.io.File)(op: java.io.PrintWriter => Unit) {
  val p = new java.io.PrintWriter(f)
  try { op(p) } finally { p.close() }
}



def main(args: Array[String]){

	var counted_stuff = count_words(args)
	val ordered_map = order_map(counted_stuff)
	printing(ordered_map)


    new PrintWriter("scala_output.txt") {
    ordered_map.foreach {
    case (k, v) =>
      write(k + ":" + v)
      write("\n")
  }
    val conf = new Configuration()
    val fs= FileSystem.get(conf)
    val output = fs.create(new Path("hdfs://localhost:9000/task2/scala_output.txt"))
    val writer = new PrintWriter(output)

    try {
        writer.write(ordered_map) 
    }
    finally {
        writer.close()
    }


  
  close()
}
}

main(split_word)


