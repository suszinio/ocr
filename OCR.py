import pytesseract
import cv2
import os



#sciezka do obrazu
#imPath = 'C:/Users/xxx/Documents/ocrtest/example_01.png'
#preprocesType = 'thresh'

print("Program OCR do odczytywania tekstu ze zdjęcia/skanu.")
print("Podaj sciezke do pliku który chcesz odczytać : ")
imPath = input()
print("W tym momencie mamy dwie mozliwosci preprocesingu zdjęcia : Thresh i Blur. Podaj wartość"
      " 1 dla Thresh, 2 dla Blur. Jeżeli nie chcesz preprocesingować obrazu, pomin wprowadzanie parametru")
intType = input()

if intType == '1':
    preprocesType = "thresh"
elif intType == '2':
    preprocesType = "blur"
else:
    preprocesType =""

#Funkcja jako argumenty przyjmuje sciezke do pliku, oraz typ preprocessingu dla obrazu(thresh,blur)
def OCR(imPath,preprocesType):

    #zaladuj obraz i skonwertuj na skale szarosci
    image = cv2.imread(imPath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


    #wybierz odpowiedni preprocessing dla obrazu
    if preprocesType == 'thresh':
        gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocesType == 'blur':
        gray = cv2.medianBlur(gray,3)

    #zapisz obraz na dysku jako plik tymczasowy, i przekaz do OCR
    filename ="{}.png".format(os.getpid())
    cv2.imwrite(filename,gray)


    #config dla OCR pyteesracta
    #config = ('-l pol --oem 0 --psm 3')

    #zaladuj obraz jako Pil/pillow, zapusc OCR, a potem skasuj tempa
    text = pytesseract.image_to_string(filename)
    os.remove(filename)
    print("Odczytano obraz. Jego wynikim jest : ")
    print(text)

    # pokaz zmienione obrazy
    cv2.imshow("image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)

OCR(imPath,preprocesType)
