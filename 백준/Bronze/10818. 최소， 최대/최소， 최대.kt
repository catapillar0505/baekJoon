import java.util.*
import kotlin.collections.ArrayList

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)
    val size = sc.nextInt()

    val list = ArrayList<Int>(size)

    for (i in 0 until size) {
        val n = sc.nextInt()
        list.add(n)
    }

    print("${list.minOrNull()} ${list.maxOrNull()}")
}