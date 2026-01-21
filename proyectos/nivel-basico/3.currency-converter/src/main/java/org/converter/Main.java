package org.converter;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Create Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        System.out.println("Currency Converter");
        System.out.println();

        // Available currencies and exchange rates relative to USD(currently)
        double usdToEur = 0.85; // 1 USD = 0.85 EUR
        double usdToGbp = 0.73; // 1. USD = 0.73 GBP
        double usdToPesos = 18.50; // 1. USD = 18.50 Pesos
        double usdToJpy = 110.25; // 1 USD = 110.25 JPY
        double usdToCad = 1.25; // 1 USD = 1.25 CAD

        // Showing available currencies
        System.out.println("Available currencies:");
        System.out.println("1. USD Dollar (USD)");
        System.out.println("2. Euro (EUR)");
        System.out.println("3. Pesos (PESOS)");
        System.out.println("4. British Pound (GBP)");
        System.out.println("5. Japanese Yen (JPY)");
        System.out.println("6. Canadian Dollar (CAD)");
        System.out.println();

        // Getting the amount
        System.out.println("Enter the amount to convert: ");
        double amount = scanner.nextDouble();

        // Choosing the source currency
        System.out.println("\nSelect source currency (enter number 1-5):");
        System.out.println("Select: ");
        int sourceCurrency = scanner.nextInt();

        // Choosing target currency
        System.out.println("\nSelect target currency (enter number 1-5):");
        System.out.println("Select: ");
        int targetCurrency = scanner.nextInt();

        // Variables to store
        String sourceCurrencyName = "";
        String targetCurrencyName = "";
        double convertedAmount = 0;

        double amountInUsd = 0;

        switch(sourceCurrency){
            case 1: // USD
                amountInUsd = amount;
                sourceCurrencyName = "USD";
            break;
            case 2: //EUR to USD
                amountInUsd = amount / usdToEur;
                sourceCurrencyName = "EUR";
            break;
            case 3: //Pesos to USD
                amountInUsd = amount / usdToPesos;
                sourceCurrencyName = "Pesos";
            break;
            case 4: // GBP to USD
                amountInUsd = amount / usdToGbp;
                sourceCurrencyName = "GBP";
            break;
            case 5: // JPY to USD
                amountInUsd = amount / usdToJpy;
                sourceCurrencyName = "JPY";
            break;
            case 6: // CAD to USD
                amountInUsd = amount / usdToCad;
                sourceCurrencyName = "CAD";
            break;
            default:
                System.out.println("Invalid source currency selection");
                scanner.close();
                return;
        }


        switch(targetCurrency){
            case 1: // USD
                convertedAmount = amountInUsd;
                targetCurrencyName = "USD";
            break;
            case 2: // USD to EUR
                convertedAmount = amountInUsd * usdToEur;
                targetCurrencyName = "EUR";
            break;
            case 3: // USD to Pesos
                convertedAmount = amountInUsd * usdToPesos;
                targetCurrencyName = "Pesos";
            break;
            case 4: // UAS to GBP
                convertedAmount = amountInUsd * usdToGbp;
                targetCurrencyName = "GBP";
            break;
            case 5: // USD to JPY
                convertedAmount = amountInUsd * usdToJpy;
                targetCurrencyName = "JPY";
            break;
            case 6: // USD to CAD
                convertedAmount = amountInUsd * usdToCad;
                targetCurrencyName = "CAD";
            break;
            default:
                System.out.println("Invalid target currency selection");
                scanner.close();
                return;
        }



        System.out.println("\n======================================================");
        System.out.println("Result");
        System.out.printf("%.2f %s = %.2f %s%n", amount, sourceCurrencyName, convertedAmount, targetCurrencyName);


        System.out.println("=========================================================");
        /*System.out.println();
        System.out.printf("1 USD = %.2f EUR%n", usdToEur);
        System.out.printf("1 USD = %.2f Pesos%n", usdToEur);
        System.out.printf("1 USD = %.2f GBP%n", usdToGbp);
        System.out.printf("1 USD = %.2f JPY%n", usdToJpy);
        System.out.printf("1 USD = %.2f CAD%n", usdToCad);*/

        scanner.close();



    }
}