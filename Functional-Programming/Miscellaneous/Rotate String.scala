object Solution {

    def main(args: Array[String]) {
        val T = readInt
        for (i <- 1 to T){
            val str = readLine.toList
            val n = str.length
            val strz = str.zipWithIndex
            for (rotz <- 1 to n) print(strz.map((x) => str((x._2 + rotz) % n)).mkString("") + " ")
            println()
        }
        
    }
}
