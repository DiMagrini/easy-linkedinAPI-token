import json_crud
from codes_manager import token_catcher
from code_parse import catch_code
from bashcmd import get_id

#adds a first json file with all needed information
def first_config():
    print('forneça as informações para criar o arquivo para ser usado nas requests para a api do linkedIn:\n')
    client_id= input('Seu client id: ')
    client_secret= input('Seu client_secret: ')
    redirect_link= input('Seu redirect_link: ')
    
    url_get_your_code= f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_link}&state=RandomString&scope=w_member_social,r_liteprofile'
    code = catch_code(url_get_your_code)
    #cacth_code verifies if validation code is correct. if dont, it returns None
    if code is None:
            print('\ntalvez seu link de redirecionamento, client_id ou client_secret esteja errado. Verifique-os novamente:')
            first_config()
    #concatenates given information to create the correct URL to request access token.
    redirection = f'{redirect_link}&client_id={client_id}&client_secret={client_secret}'
    #concatenates a cURl to request access token
    post_access_token= f'"grant_type=authorization_code&code={code}&redirect_uri={redirection}" -H "application/x-www-form-urlencoded" -X POST "www.linkedin.com/oauth/v2/accessToken"'
    
    about_token = token_catcher(post_access_token)
    #if token_catcher returns None, it try a new validation code
    while about_token == None:
            code = catch_code(url_get_your_code)
            post_access_token= f'"grant_type=authorization_code&code={code}&redirect_uri={redirection}" -H "application/x-www-form-urlencoded" -X POST "www.linkedin.com/oauth/v2/accessToken"'
            about_token = token_catcher(post_access_token)

    access_token = about_token['token']
    #now with the accress token, it can request the user id, used to make shares with linkedin api
    bash_command_id = f'"Authorization: Bearer {access_token}" -X GET "https://api.linkedin.com/v2/me"'
    linkedin_id = get_id(bash_command_id)
    #Put all the information gathered in a json file
    json_crud.create_new_json(
        client_id = client_id,
        client_secret = client_secret,
        code = code,
        linkedin_id = linkedin_id,
        about_token = about_token,
        URLs = {
            'redirect_link': redirect_link,
            'redirection': redirection,
            'post_access_token': post_access_token,
            'url_get_your_code': url_get_your_code,
            'bash_command_id': bash_command_id
        }
    )
