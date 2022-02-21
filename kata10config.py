#Primer programa
#Este programa hace referencia a poder abrir una archivo que no existe
#open("/path/to/mars.jpg")

#Segundo programa,verifica que existe el archivo pero no puede acceder por privilegios
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")

#if __name__ == '__main__':
#    main()

#tercer programa
#def main():
#    try:
#        configuration = open('config.txt')
#    except Exception:
#        print("Couldn't find the config.txt file!")

#if __name__ == '__main__':
#    main()

#tercer programa
#def main():
#    try:
#        configuration = open('config.txt')
#     except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")

#if __name__ == '__main__':
#    main()

#cuarto programa para verificar un error

#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")
#    except (BlockingIOError, TimeoutError):
#        print("Filesystem under heavy load, can't complete reading configuration file")

#if __name__ == '__main__':
#    main()

#Quinto programa para verificar un error
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")
#    except (BlockingIOError, TimeoutError):
#        print("Filesystem under heavy load, can't complete reading configuration file")

