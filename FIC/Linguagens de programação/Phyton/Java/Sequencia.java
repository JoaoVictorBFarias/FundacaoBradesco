import java.util.Scanner;

public class Sequencia{
    public static void main(String[] args) {
        double n1=0.0, n2=0.0, n3 = 0.0;

        Scanner s = new Scanner(System.in);

        System.out.println("Digite o 1 número: ");
        n1 = s.nextDouble();
        
        System.out.println("Digite o 2 número: ");
        n2 = s.nextDouble();

        System.out.println("Digite o 3 número: ");
        n3 = s.nextDouble();

        if(n1 <n2 && n1 < n3){
            if(n2 < n3){
                System.out.println(n1+"\n"+"\n"+n2+"\n"+n3);
            }else{
                System.out.println(n1+"\n"+"\n"+n3+"\n"+n2);
            }

        }
        else if(n2 <n1 && n2 < n3){
            if(n1 < n3){
                System.out.println(n2+"\n"+"\n"+n1+"\n"+n3);
            }else{
                System.out.println(n2+"\n"+"\n"+n3+"\n"+n1);
            }

        }
        else if(n3 <n1 && n3 < n2){
            if(n1 < n2){
                System.out.println(n3+"\n"+"\n"+n1+"\n"+n2);
            }else{
                System.out.println(n3+"\n"+"\n"+n2+"\n"+n1);
            }
        }
    }
}