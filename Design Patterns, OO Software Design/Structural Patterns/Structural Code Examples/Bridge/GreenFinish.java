public class GreenFinish implements ColorFinishPlan
{
    public void paint(){
        this.chooseColor();
        this.startPaintMachine();
        System.out.println("Car Painted Successfully");
    };
    public void chooseColor(){
        System.out.println("Green Color Chosen Successfully");
    };
    public void startPaintMachine(){
        System.out.println("Paint Machine Started");
    };
}