package org.converter;

import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static Scanner scanner = new Scanner(System.in);
    public static float med1, med2;
    public static String m1, m2;

    public static void main(String[] args) {



        mostrarMenu();

    }

    public static void mostrarMenu(){


        int n;
        float result = 0f;

        System.out.println("Conversor de Unidades de Longitudes, Volumenes y Peso, a partir de las opciones  y medida.");

    do {
        System.out.println("""
                
                
                1)Longitudes.
                1.1.- Pulgadas a Milimetros.
                1.2.- Yardas a Metros.
                1.3.- Millas a kilometros.
                1.4.- Pulgadas a centimetros.
                1.5.- Pies a metros.
                1.6.- Yardas a metros.
                1.7.- Acre a hectareas.
                1.8.- Millas a kilometros.
                
                2)VOLUMEN.
                2.1.- Pie a metros.
                2.2.- Yardas a metros.
                2.2.- Pinta a litros.
                2.3.- Galon a litros
                
                3)PESO.
                1.3.- Onza a gramos.
                2.3.- Libra a kilogramos
                3.3.- Tonelada inglesa a tonelada.
                
                0)Salir""");




            System.out.println("\n\nIngrese Opción 1: ");
            scanner = new Scanner(System.in);
            n = scanner.nextInt();
            limpiarPantalla();

            switch (n) {
                case 1:
                    longitudConverter();
                    result = med1;
                    break;

                case 2:
                    volumenConverter();
                    result = med1;
                    break;

                case 3:
                    pesoConverter();
                    result = med1;
                    break;
                default:
                    System.out.println("Opcion incorrecta");
                    break;

            }

            System.out.println("Resultado de  "+m1+" a "+m2+": "+result);
            System.out.println("Quieres hacer otra conversion?  \n\n1.- Si\n0.- No");
            n = scanner.nextInt();
        }while(n != 0);

        scanner.close();





    }// Fin de mostrarMenu

    public static void limpiarPantalla() {
        String os = System.getProperty("os.name").toLowerCase();

        try {
            if (os.contains("win")) {
                // Para Windows
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                // Para Linux, macOS y Unix
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            // Si falla, imprime múltiples líneas en blanco
            System.out.println("\n".repeat(50));
        }
    }

    public static void longitudConverter(){

        int opt2;


        System.out.println("""
                1.- Pulgadas a Milimetros.
                2.-Yardas a Metros.
                3.- Millas a Kilometros.
                4.- Pulgadas a Centimetros.
                5.- Pies a Metros
                6.- Yardas a Metros.
                7.- Acre a Hectareas.
                8.- Millas a Kilometros.""");

        System.out.println("Ingrese la opción de conversión:");

        scanner = new Scanner(System.in);
        opt2 = scanner.nextInt();
        limpiarPantalla();

        System.out.println("Ingrese medida: ");
        scanner = new Scanner(System.in);
        med1 = scanner.nextFloat();
        med2 = med1;

        switch(opt2) {
            case 1:
                System.out.println("Pulgadas a Milimetros");
                med1 *= 25.40f;
                m1 = "Pulgadas";
                m2 = "Milimetros";
                break;
            case 2:
                System.out.println("Yardas a Metros");
                med1 *= 0.9144f;
                m1 = "Yardas";
                m2= "Metros";
                break;
            case 3:
                System.out.println("Millas a Kilometros");
                med1 *= 1.6093f;
                m1 = "Millas";
                m2 = "Kilometros";
                break;
            case 4:
                System.out.println("Pulgadas a Centimetros");
                med1 *= 6.452f;
                m1 = "Pulgadas";
                m2 = "Centimetros";
                break;
            case 5:
                System.out.println("Pies a Metros");
                med1 *= 0.09290f;
                m1 = "Pies";
                m2 = "Metros";
                break;
            case 6:
                System.out.println("Yardas a Metros");
                med1 *= 0.8361f;
                m1 = "Yardas";
                m2 = "Metros";
                break;
            case 7:
                System.out.println("Acre a Hectareas");
                med1 *= 0.4047f;
                m1 = "Acre";
                m2 = "Hectareas";
                break;
            case 8:
                System.out.println("Millas a Kilometros");
                med1 *= 2.59f;
                m1 = "Millas";
                m2 = "Kilometros";
                break;
            default:
                System.out.println("Opción incorrecta");
                break;
        }

    }

    public static void volumenConverter(){

        int opt2;


        System.out.println("""
                1.- Pie a metros.
                2.-Yardas a metros.
                3.- Pinta a Litros.
                4.- Galon a Litros.""");

        System.out.println("Ingrese la opción de conversión:");

        scanner = new Scanner(System.in);
        opt2 = scanner.nextInt();
        limpiarPantalla();

        System.out.println("Ingrese medida: ");
        scanner = new Scanner(System.in);
        med1 = scanner.nextFloat();
        med2 = med1;


        switch(opt2) {
            case 1:
                System.out.println("Pies a Metros");
                med1 *= 0.02832f;
                m1 = "Pies";
                m2 = "Metros";
                break;
            case 2:
                System.out.println("Yardas a Metros");
                med1 *= 0.7646f;
                m1 = "Yardas";
                m2= "Metros";
                break;
            case 3:
                System.out.println("Pinta a Litros");
                med1 *= 0.56826f;
                m1 = "Pinta";
                m2 = "Litros";
                break;
            case 4:
                System.out.println("Galon a Litros");
                med1 *= 6.452f;
                m1 = "Galon";
                m2 = "Litros";
                break;
            default:
                System.out.println("Opcion incorrecta");
                break;
        }
    }

    public static void pesoConverter(){

        int opt2;


        System.out.println("""
                1.- Onza a gramos.
                2.-Libra a Kilogramos.
                3.- Tonelada inglesa a Tonelada.""");

        System.out.println("Ingrese la opción de conversión:");

        scanner = new Scanner(System.in);
        opt2 = scanner.nextInt();
        limpiarPantalla();

        System.out.println("Ingrese medida: ");
        scanner = new Scanner(System.in);
        med1 = scanner.nextFloat();
        med2 = med1;


        switch(opt2) {
            case 1:
                System.out.println("Onza a gramos");
                med1 *= 28.35f;
                m1 = "Onza";
                m2 = "Gramos";
                break;
            case 2:
                System.out.println("Libra a kilogramos");
                med1 *= 0.45359f;
                m1 = "Libra";
                m2= "Kilogramos";
                break;
            case 3:
                System.out.println("Tonelada inglesa a tonelada");
                med1 *= 1.0160f;
                m1 = "Tonelada Inglesa";
                m2 = "Tonelada";
                break;
            default:
                System.out.println("Opcion incorrecta");
                break;
        }


    }
}