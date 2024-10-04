public class Voiture{

    String marque = "Marks ";
    String model = "generic " ;

    public void demarrer(){
        System.out.println("la voiture " + marque + "" + model + "demarre");
    }
    public static void main(String[] args) {
       Voiture mycar = new Voiture();
       mycar.demarrer();
    }
}