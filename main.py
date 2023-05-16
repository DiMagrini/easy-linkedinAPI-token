def check_json_file():
    import json_crud
    try:
        data= json_crud.read_json()
    except:
        print('arquivo JSON necessário não encontrado.')
        return None

    key_list= [
        'client_id', 'client_secret','about_token',
        'linkedin_id','URLs'
    ]
    not_found = []
    
    for i in range(len(key_list)):
        #checks each key. if it isnt found, it is appended to a list
        key_checking = key_list[i]

        print(f'Checando chave {key_checking}')
        checked = data.get(key_checking)
        if checked is None:
            not_found.append(key_checking)
            print(not_found)

    print(f'Checando chave redirect_link')
    if data.get(key_list[-1]).get('redirect_link') is None:
        not_found.append(key_list[-2])

    if len(not_found) > 0:
        join_not_found = ', '.join(not_found)
        print(f'arquivo JSON encontrado mas faltam as chaves {join_not_found}')
        return not_found
    else:
        print('arquivo JSON com as chaves corretas encontrado.')
        return data

first_time = False
config = check_json_file()

if config is None:
    first_time = True
    from config import first_config
    first_config()
    config = check_json_file()

if config is type(list):
    
    if config in ('client_id', 'client_secret','redirect_link','URLs'):
        from config import first_config
        first_config()
        config = check_json_file()
    
    if config in 'about_token':
        from codes_manager import token_catcher
        from json_crud import read_json
        token = token_catcher()
        if token_catcher() == None:
            first_config()
        config = check_json_file()
    
    if config in 'linkedin_id':
        from bashcmd import get_id
        from json_crud import read_json
        command = read_json().get('URLs').get('bash_command_id')
        get_id(command)
        config = check_json_file()
#if there is the correct file and keys, it just verify the expiration date of the access token
if first_time == False:
    from codes_manager import check_expiration_date
    expiration_date = check_expiration_date()
    print(f'\no access code expira em {expiration_date}.\n\n Volte em 60 dias para atualiza-lo.\n')
 
update = input('Arquivo JSON configurado e pronto para uso na API do linkedIn.\nPressione [Y] se deseja atualizar o access_token ou [N] para encerrar.')
#ask user for update the token even if it isnt expirated
if update.lower() == 'y':
    from codes_manager import token_catcher
    from json_crud import read_json, update_json
    token = token_catcher()
    update_json(dict_=token)
    expires = token.get('expiration_date')
    input(f'Token atualizado. Nova data de validade: {expires}\nVolte em 60 dias para atualiza-lo navamente.\n Aperte qualquer tecla para encerrar.')
