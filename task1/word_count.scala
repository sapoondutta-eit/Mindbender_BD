import scala.io.Source
import scala.collection.immutable.ListMap


lazy val initialize_file = io.Source.fromFile("Shakespeare.txt").getLines.mkString

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

def main(args: Array[String]){

	var counted_stuff = count_words(args)
	val ordered_map = order_map(counted_stuff)
	printing(ordered_map)
}

main(split_word)


