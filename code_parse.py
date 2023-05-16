def catch_code(url_get_your_code):
    #returns only the code from the given url response
    def url_slicer():

        code_to_extract = input('3) Copie o link dessa pagina e cole no terminal para extrair o code: ')
        
        begin_slice = code_to_extract.find('code=')
        end_slice = code_to_extract.find('&state')

        return [code_to_extract, begin_slice+len('code='), end_slice]
    
    print('\n1) Precisamos de um codigo de validação para obter o access token.'
        f'acesse esse link e logue na pagina do linkedIn:\n\n{url_get_your_code}\n\n'
        '2)isso vai te levar a uma pagina inexistente\n')

    code_in = url_slicer()
    count = 0

    while code_in[1] and code_in[2] == -1:
        #try use the given inrformation 2 times. at the tirthy time it returns None, so the script can ask for new informations
        count += 1
        if count > 1:
            return None
        
        print('\nHá algo de errado com esse link. Codigo não encontrato. Tente novamente.')
        
        code_in = url_slicer()

    code = code_in[0][code_in[1]:code_in[2]]
    print('\nCodigo encontrado.')

    return code
