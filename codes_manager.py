from datetime import datetime, timedelta
import json_crud, bashcmd, code_parse

def update_helpper():
    #concatenetes a query used to cat the code
    urls = json_crud.read_json().get('URLs')
    redirection = urls.get('redirection')
    url_code = urls.get('url_get_your_code')

    code = code_parse.catch_code(url_code)
    post_access_token= f'"grant_type=authorization_code&code={code}&redirect_uri={redirection}" -H "application/x-www-form-urlencoded" -X POST "www.linkedin.com/oauth/v2/accessToken"'
    return post_access_token
#do a query to access token
def token_catcher(command=None):
    #if the curl is aredy passed, the func use the given curl
    if command:
        response = bashcmd.get_access_token(command)

    else: response = update_helpper()
    token = response.get('access_token')
    #verify if the response is actualy the token or an error
    if token == None:
        error = response.get('error')
        print(f'{error}. \nAtualize o codigo de valídação.')
        return
    #defines the expiration date
    expiration_date = datetime.now() + timedelta(seconds=response.get('expires_in'))

    about_token = {'token': token,
    'expiration_date': expiration_date.isoformat()}

    return about_token

def check_expiration_date():

    print('\nChecando data de validade do access_token.')

    try:
        validation_date = datetime.fromisoformat(json_crud.read_json().get('about_token').get('expiration_date'))
    except:
        print('Formato de data inválido. Obtenha o accress_token novamente para confirmar a validade.')
        token_catcher()

    if validation_date:
        print(f'\nValidade do token: {validation_date}')

        if validation_date > datetime.now():
            print('Token ainda válido. Não é necessario atualiza-lo')
            return validation_date
        else:
            print('\nToken obsoleto. Atualize...')
            #if token is expirated, it try catch a new token.
            token_catcher()

    else:
        print('validade do token não encontrada. obtenha o access_token')
        token_catcher()
