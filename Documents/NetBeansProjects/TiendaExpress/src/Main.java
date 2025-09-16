/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author USUARIO
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    public static void mostrarMenu() {
        System.out.println("\n====== TIENDA EXPRESS ======");
        System.out.println("1. Agregar producto");
        System.out.println("3. Pagar");
        System.out.println("4. Salir");
        System.out.print("Seleccione una opcion: ");
    }
    public static int leerOpcion(Scanner sc) {
        int opcion = 0;
        try {
            opcion = Integer.parseInt(sc.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Debe ingresar un número.");
        }
        return opcion;
    }
    public static void agregarProducto(List<Double> carrito, double precio) {
        carrito.add(precio);
        System.out.println("Producto de $" + precio + " agregado al carrito.");
    }
    public static double total(double base, double impuesto) {
        return base + (base * impuesto);
    }
    public static void confirmarCompra(String correo, double total) {
        if (!correo.contains("@") || !correo.contains(".")) {
            System.out.println("Correo no válido.");
            return;
        }
        System.out.println("\n--- RESUMEN DE COMPRA ---");
        System.out.println("Correo: " + correo);
        System.out.println("Total pagado: $" + String.format("%.2f", total));
        System.out.println("Gracias por su compra.");
    }
    public static void pagar(List<Double> carrito, Scanner sc) {
        if (carrito.isEmpty()) {
            System.out.println("El carrito está vacío.");
            return;
        }
        double suma = 0;
        for (double precio : carrito) {
            suma += precio;
        }
        double totalConImpuesto = total(suma, 0.15);
        System.out.println("Subtotal: $" + String.format("%.2f", suma));
        System.out.println("IVA (15%): $" + String.format("%.2f", totalConImpuesto - suma));
        System.out.println("Total a pagar: $" + String.format("%.2f", totalConImpuesto));
        System.out.print("Ingrese su correo para recibir el comprobante: ");
        String correo = sc.nextLine();
        confirmarCompra(correo, totalConImpuesto);
        carrito.clear();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Double> carrito = new ArrayList<>();
        int opcion;
        do {
            mostrarMenu();
            opcion = leerOpcion(sc);
            switch (opcion) {
                case 1:
                    System.out.print("Ingrese el precio del producto: ");
                    try {
                        double precio = Double.parseDouble(sc.nextLine());
                        if (precio > 0) {
                            agregarProducto(carrito, precio);
                        } else {
                            System.out.println("El precio debe ser positivo.");
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Precio no válido.");
                    }
                    break;
                case 3:
                    pagar(carrito, sc);
                    break;
                case 4:
                    System.out.println("Saliendo de la Tienda Express...");
                    break;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        } while (opcion != 4);
        sc.close();
    }
}
