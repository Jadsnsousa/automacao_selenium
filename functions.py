# Automação com Selenium by Jadson Sousa

# Escrevi esse codigo com o proposito de conhecer a biblioteca Selenium. 
# O objetivo dele é bem simples, entrar no site, buscar o resultado de um jogo e retornar essa informação ao usuário.

# Importar Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Opções do WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Executa o navegador em 2° plano.
driver = webdriver.Chrome(options=options)




def MegaSena(jogo=1475, onlynum=False):
    """
    Arg:
        jogo - Recebe o numero do jogo digitado pelo usuário, por padrão ele busca o resultado do jogo 1475.

        onlynum - Da ao usuário a possibilidade de receber os numeros em formato de lista ou em formato de texto.
        Se verdadeiro, envia os numeros em formato de lista, se não, envia os numeros formatado em string.

    Esta função acessa o site da Mega-Sena automaticamente e retorna o resultado do jogo selecionado pelo usuário.
    Se o usuário não passar o numero do jogo, a função retorna o resultado do jogo 1475.
    """
    try:
        numbers = list()
        driver.get("https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx")
        driver.find_element('xpath', '//*[@id="buscaConcurso"]').send_keys(f'{jogo}')
        driver.find_element('xpath', '//*[@id="buscaConcurso"]').send_keys(Keys.ENTER)
        sleep(2)
        result = driver.find_element(By.ID, 'ulDezenas').text
        A = 0
        B = 2
        for c in range(0, 6):
            numbers.append(result[A:B])
            A += 2
            B += 2
        if onlynum:
            return numbers
        else:
            return print(f'Resultado do jogo n°{jogo} MegaSena'
                f'\n{numbers[0]} - {numbers[1]} - {numbers[2]} - {numbers[3]} - {numbers[4]} - {numbers[5]}')
    except:
        return print(f'Não foi possivel realizar a consulta, tente novamente.')
    
def Quina(jogo=1475, onlynum=False):
    """
    Arg:
        jogo - Recebe o numero do jogo digitado pelo usuário, se não houver, por padrão ele busca o resultado do jogo 1475.

        onlynum - Da ao usuário a possibilidade de receber os numeros em formato de lista ou em formato de texto.
        Se verdadeiro, envia os numeros em formato de lista, se não, envia os numeros formatado em string.

    Esta função acessa o site da Quina automaticamente e retorna o resultado do jogo selecionado pelo usuário.
    Se o usuário não passar o numero do jogo, a função retorna o resultado do jogo 1475.
    """
    try:
        numbers = list()
        driver.get("https://loterias.caixa.gov.br/Paginas/Quina.aspx")
        driver.find_element('xpath', '//*[@id="buscaConcurso"]').send_keys(f'{jogo}')
        driver.find_element('xpath', '//*[@id="buscaConcurso"]').send_keys(Keys.ENTER)
        sleep(2)
        result = driver.find_element(By.ID, 'ulDezenas').text
        A = 0
        B = 2
        for c in range(0, 5):
            numbers.append(result[A:B])
            A += 2
            B += 2
        if onlynum:
            return numbers
        else:
            print(f'Resultado do jogo N°{jogo} Quina'
                f'\n{numbers[0]} - {numbers[1]} - {numbers[2]} - {numbers[3]} - {numbers[4]}')
    except:
        print(f'Não foi possivel realizar a busca. Verifique o numero de jogo e tente novamente.')

def LotoFacil(jogo=1475, onlynum=False):
    """
    Arg:
        jogo - Recebe o numero do jogo digitado pelo usuário, se não houver, por padrão ele busca o resultado do jogo 1475.

        onlynum - Da ao usuário a possibilidade de receber os numeros em formato de lista ou em formato de texto.
        Se verdadeiro, envia os numeros em formato de lista, se não, envia os numeros formatado em string.

    Esta função acessa o site da Loto-Facil automaticamente e retorna o resultado do jogo selecionado pelo usuário.
    Se o usuário não passar o numero do jogo, a função retorna o resultado do jogo 1475.
    """
    try:
        numbers = list()
        driver.get("https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx")
        driver.find_element('xpath', '//*[@id="buscaConcurso"]').send_keys(f'{jogo}')
        driver.find_element('xpath', '//*[@id="buscaConcurso"]').send_keys(Keys.ENTER)
        sleep(2)
        result = driver.find_element(By.CLASS_NAME, 'lista-dezenas').text
        A = 0
        B = 2
        for c in range(0, 16):
            numbers.append(result[A:B])
            A += 2
            B += 2
        if onlynum:
            return numbers
        else:
            print(f'Resultado do jogo N°{jogo} LotoFacil:' \
            f'\n{numbers[0]} - {numbers[1]} - {numbers[2]} - {numbers[3]} - {numbers[4]}' \
            f'\n{numbers[5]} - {numbers[6]} - {numbers[7]} - {numbers[8]} - {numbers[9]}' \
            f'\n{numbers[10]} - {numbers[11]} - {numbers[12]} - {numbers[13]} - {numbers[14]}')
        
    except:
        print(f'Não foi possivel realizar a busca. Verifique o numero de jogo e tente novamente.')




if __name__ == '__main__':
    # Rodando o codigo
    NJogo = str(input('Digite o n° do jogo: '))[:4]
    ResMega = MegaSena(NJogo, True)
    MegaSena(NJogo, False)
    print(f'\nResultado do jogo n°{NJogo}: {ResMega}')

    # Output
    
    # onlynum = False \/
    # Resultado do jogo n°2558 MegaSena
    # 02 - 10 - 18 - 25 - 34 - 44
    #
    # onlynum = True \/
    # ['02', '10', '18', '25', '34', '44']