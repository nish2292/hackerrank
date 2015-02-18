object Solution {

    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/
        val s1 = readLine().toList
        val s2 = readLine().toList
        val s3 = s1.zip(s2)
        println(s3.flatMap((x) => List(x._1,x._2)).mkString(""))
    }
}
