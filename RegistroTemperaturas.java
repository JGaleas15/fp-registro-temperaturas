/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author USUARIO
 */
public class RegistroTemperaturas {
    public static void main(String[] args) {
        // Definir ciudades, días y semanas
        String[] ciudades = {"Ambato", "Quito"};
        String[] dias = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"};
        int semanas = 2;
        double[][][] temperaturas = new double[ciudades.length][dias.length][semanas];
        for (int c = 0; c < ciudades.length; c++) {
            for (int s = 0; s < semanas; s++) {
                for (int d = 0; d < dias.length; d++) {
                    // Generar temperatura aleatoria entre 15 y 35 grados
                    temperaturas[c][d][s] = 15 + Math.random() * 20;
                }
            }
        }
        for (int c = 0; c < ciudades.length; c++) {
            System.out.println("==============================");
            System.out.println("Promedio de temperaturas");
            System.out.println("Ciudad: " + ciudades[c]);
            System.out.println("------------------------------");
            for (int s = 0; s < semanas; s++) {
                double suma = 0;
                for (int d = 0; d < dias.length; d++) {
                    suma += temperaturas[c][d][s];
                }
                double promedio = suma / dias.length;
                System.out.printf("Semana %d - Promedio: %.2f°C\n", s + 1, promedio);
            }
            System.out.println();
        }
    }
}
