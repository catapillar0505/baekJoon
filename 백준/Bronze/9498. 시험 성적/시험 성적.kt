fun main(){
    val grade : Int = readLine()!!.toInt()
    if(grade >= 90){
        print("A");
    }
    else if(grade >= 80){
        print("B");
    }
    else if(grade >= 70){
        print("C");
    }
    else if(grade >= 60){
        print("D");
    }
    else {
        print("F");
    }
    
}