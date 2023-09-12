import java.util.Scanner;

class Parimpa{
    public static void main(String[] args){
    
    int num=0;

    Scanner s = new Scanner(System.in);
    System.out.println("Digite o número aqui:");
    num = s.nextInt();

    if (num % 2 == 0){
        System.out.println("O número "+num+" é Par!");
    }else{
        System.out.println("O número "+num+" é ímpar!");
    }

   }
}
