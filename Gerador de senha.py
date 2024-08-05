from random import sample

class Password():
      def __init__(self) -> None:
            self.numbers = '0 1 2 3 4 5 6 7 8 9 10 '
            self.lowletters = 'a b c d e f g h i j k l m n o p q r s t u v w y x z '
            self.upperletters = 'A B C D F G H I J K L M N O P Q R S T U V W Y X Z'
            self.symbols = '! @ # $ % ¨& * ( ) _ + ^ : > < ? / ;'

            pass

      def generate_password(self , senha , tamanho =12 ):
            run = True
            senha = self.lowletters + self.numbers + self.upperletters + self.symbols
            password = ''.join(sample(senha ,  tamanho ) ) 

            return password
      
      def run (self):
            run = True
            while run == True:
                    try:
                     length = int(input("Digite o comprimento desejado da senha: "))

                    except ValueError:
                     print("Por favor, digite um número válido.")

                    continue
            
            senha = self.generate_password(length)
            print(f"Senha gerada: {senha}")
            
            continuar = input('Deseja gerar outra senha? [S/N] ').strip().upper()
            if continuar != 'S':
                print("Encerrando o gerador de senhas.")
              
      
if __name__ =='__main__':
      app = Password()
      app.run()      