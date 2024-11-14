input_string = input()

def docker_command(input_string):
    # Separa a entrada em ação e nome do volume
    action, volume_name = input_string.split(", ")
    
    # COMPLETE AQUI: Mapeie as ações para comandos Docker correspondentes
    actions_to_commands = {
        "criar": "docker volume create",
        "inspecionar": "docker volume inspect",
        "remover": "docker volume rm "
    }
    
    # Verifica se a ação está mapeada e retorna o comando correspondente
    if action in actions_to_commands:
        return f"{actions_to_commands[action]} {volume_name}"

# Gera e exibe o comando Docker correspondente
print(docker_command(input_string))