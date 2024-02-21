import speech_recognition as sr
import pygame
import time
import os

# Define a função para abrir o arquivo PNG
def open_png():
    file_png = "./ovo.png"
    pygame.init()
    pygame.display.set_mode((100, 100))
    pygame.display.set_caption('OVO?')
    img = pygame.image.load(file_png)
    img_rect = img.get_rect()
    screen = pygame.display.set_mode(img_rect.size)
    screen.blit(img, img_rect)
    pygame.display.flip()

def clearscreen():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Define a função principal
def main():
    running = True
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    clearscreen()
    print("Waiting for your command...")
    time.sleep(2)
    clearscreen()
    print('Say "OVO" to start')
    clearscreen()
    while True:
        with microphone as source:
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language ='pt').lower()
            print("You said: " + command)
            if "ovo" in command:  # Verifica se a palavra "ovo" foi dita
                open_png()
                time.sleep(3)
                pygame.quit()
        except sr.UnknownValueError:
            print("I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Failed to access Google Speech Recognition Service: {0}".format(e))
#Adicionar reconhecimento de palavras para execução de comandos

if __name__ == "__main__":
    os.system('clear')
    main()
    os.system('clear')
    print("Goodbye!")
