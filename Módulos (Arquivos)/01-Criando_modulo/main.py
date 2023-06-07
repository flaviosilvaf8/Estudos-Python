from functions import somar # importamos apenas no módulo funções a função somar

from items.cadastro import cliente # Irá dentro do package items e dentro de cadastro achando a função cliente

somar() # Chamando a função somar do modulo functions
cliente()

# Para importar todas as funções do modulo functions deveriamos escrever "import functions"


