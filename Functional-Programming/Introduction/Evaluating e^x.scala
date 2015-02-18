object Solution {
def f(x: Float):Float = (1 to 10).toList.map(t => (math.pow(x,(t-1)) / (1 to (t-1)).product) ).sum.toFloat

def main(args: Array[String]) {
       var n = readInt
       (1 to n) foreach(x=> println(f(readFloat())))
    }
}
