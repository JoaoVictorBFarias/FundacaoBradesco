// add pacote se precisar

// add o import
import java.util.Scanner;

// publicar Class
public class Temperatura{
    
    // add main
    public static void main(String[] args) {
        
        // declarar variável
        double c = 0.0, f = 0.0;
        
        // add scanner
        Scanner s = new Scanner(System.in);
        
        // sysout (perguntar ao usuário)
        System.out.println("Informe a temperatura em graus Celsius: ");
        
        // armazenar
        c = s.nextDouble();

        // sistema
        f = (9*c+160)/5;
        
        // exibição final
        System.out.println("A temperatura convertida é: "+f+" °F");
        s.close();
    }
}
