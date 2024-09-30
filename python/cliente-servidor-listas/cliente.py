import xmlrpc.client
import random

def gerar_lista_aleatoria(tamanho):
    return [random.randint(0, 100) for _ in range(tamanho)]

def main():
    # Conecta ao servidor
    endereco_servidor = "localhost"
    porta_servidor = 50000
    cliente = xmlrpc.client.ServerProxy("http://" + endereco_servidor + ":" + str(porta_servidor) + "/")
    
    # Gera uma lista aleatória
    tamanho_lista = 60  # você pode alterar o tamanho conforme necessário
    lista_aleatoria = gerar_lista_aleatoria(tamanho_lista)
    print(f"Lista enviada: {lista_aleatoria}")
    
    # Envia a lista para o servidor e recebe a lista ordenada
    lista_ordenada = cliente.ordenar_lista(lista_aleatoria) #ordenar_lista eh um metodo do servidor, invocado pelo cliente
    print(f"Lista ordenada recebida: {lista_ordenada}")

    print(cliente.dizer_ola()) #dizer_ola eh um metodo do servidor, invocado pelo cliente

if __name__ == "__main__":
    main()
