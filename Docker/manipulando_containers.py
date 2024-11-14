input_string = input()

def docker_command(input_string):
    # Separa a entrada em ação e nome do volume
    action, name = input_string.split(", ")
    
    # COMPLETE AQUI: Mapeie as ações para comandos Docker correspondentes
    actions_to_commands = {
        "baixar": "docker pull",
        "executar": "docker run",
        "parar": "docker stop",
        "remover": "docker rm"
    }
    
    # Verifica se a ação está mapeada e retorna o comando correspondente
    if action in actions_to_commands:
        return f"{actions_to_commands[action]} {name}"

# Gera e exibe o comando Docker correspondente
print(docker_command(input_string))


