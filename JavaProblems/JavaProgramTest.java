public class JavaProgramTest {
    
    String carColor;
    public void Car(String color){

        carColor = color;
    }
    public static void main(String[] args){
        Car ferrari = new Car("red");
        System.out.println(ferrari.color);

    }
}