def ChecaPacotesInstalados():

    def InstalaPacote(Faltante):
        # Executa os comando no ambiente virtual do python
        import sys
        import os
        activate_this = str(os.path.dirname(sys.executable)) + '/activate_this.py'
        with open(activate_this) as f:
            code = compile(f.read(), activate_this, 'exec')
            exec(code, dict(__file__=activate_this))
            for Modulo in Faltante:
                try:
                    os.system(f'pip install {Modulo}')
                except:
                    print('Não foi possivel realizar a instalação')

    # Lista de dicionario com os pacotes para realizar a instalacao, a esquerda o nome do pacote e a dirita
    # O nome para ser preenchido no terminal ou CMD para download
    Pacotes = {'requests':'requests',
               'bs4':'bs4',
               'usp':'ultimate-sitemap-parser',
               'gtts':'gtts',
               'numpy':'--only-binary=:all: numpy',
               'pandas':'pandas',
               'sklearn':'scikit-learn',
               'speech_recognition':'SpeechRecognition'}

    ModulosFaltantes = []
    for NomePacote in Pacotes:
        try:
            __import__(NomePacote)
            print(f'O pacote {NomePacote} ja esta instalado')
        except:
            print(f'Pacote {NomePacote} não encontrado')
            ModulosFaltantes.append(Pacotes[NomePacote])
    InstalaPacote(ModulosFaltantes)

ChecaPacotesInstalados()