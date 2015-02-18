object Solution {

    def pascals(n : Int) = for (i <- 0 to (n-1)) println((0 to i).toList.map(x=> ((1 to i).product / ((1 to x).product * (1 to (i-x)).product))).mkString(" "))
    
    def main(args: Array[String]) {
         /** This will handle the input and output**/
         pascals(readInt())

    }
}
