from xmlrpc.server import SimpleXMLRPCServer

def ordenar_lista(lista):
    return sorted(lista)

def dizer_ola():
    return "Ola"

def main():
    endereco_servidor = "localhost"
    porta_servidor = 50000
    servidor = SimpleXMLRPCServer((endereco_servidor, porta_servidor))
    
    print("Servidor em execução na porta", porta_servidor)
    
    # Registra as funções para serem invocadas ou chamadas pelos clientes
    servidor.register_function(ordenar_lista, "ordenar_lista")
    servidor.register_function(dizer_ola, "dizer_ola")
    
    # Inicia o servidor
    servidor.serve_forever()

if __name__ == "__main__":
    main()
