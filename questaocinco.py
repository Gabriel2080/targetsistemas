# Input uma string
string_original = input("Digite a string a ser invertida: ")

# Pegando tamnho da string
tamanho_string = len(string_original)

# Variável que vai armazenar a string invertida
string_invertida = ""

# Invertendo a string
while tamanho_string > 0:
    string_invertida += string_original[tamanho_string-1]
    tamanho_string -= 1

print("A string invertida é:", string_invertida)