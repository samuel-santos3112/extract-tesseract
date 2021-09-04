import os
import pytesseract

from PIL import Image

UPLOAD_FOLDER = os.path.abspath('upload_image')


# Esse método vai ler o arquivo, a partir de um nome informado e vai me retornar as informações contidas na imagem.
def readImage(pathImage):
    image_text = pytesseract.image_to_string(Image.open(pathImage))

    arrWords = []
    idxInit  = None
    idxEnd   = None

    for idx, character in enumerate(image_text):
        # Verifica se a letra é um espaço em branco, e se o index início ainda não foi preenchido.
        if character != ' ' and idxInit is None:
            # Guarda o início da palavra
            idxInit = idx
        elif character == '\n':
            # Guarda o fim da palavra
            idxEnd  = idx
            # Palavra completa ex: bacon - 3KG
            completedWord = image_text[idxInit:idxEnd]
            idxInit = None
            idxEnd  = None

            if '-' in completedWord:
                splitedCompleteWord = completedWord.split('-')

                arrWords.append(
                    {
                        'item' : splitedCompleteWord[0].replace('\n', '').replace('_','').replace('=',''),
                        'quantidade' : splitedCompleteWord[1]
                    }
                )
        



    return arrWords

# Esse método vai salvar a imagem no meu servidor.
def saveImage(request):
    file = request.files['file']
    path = UPLOAD_FOLDER

    path_saved = os.path.join(path, file.filename)
    file.save(path_saved)
    return path_saved