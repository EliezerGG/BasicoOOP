class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");

        UberX uberX = new UberX("AMQ234", new Account("Andres Herrera", "AN123"),"Chevrolet","Sonic");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGGQ123", new Account("Jorge Lopez", "JRG123")); 
        uberVan.setPassenger(6);
        uberVan.printDataCar();
        
    
    }
}