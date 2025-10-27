try:
    import colorama

    version = getattr(colorama, '__version__', 'unknown')

    if version == '0.4.4':
        colorama.init()
        print(colorama.Fore.GREEN + "Зеленый текст работает!")
    else:
        colorama.init()
        print(colorama.Fore.RED + "Красный текст работает!")

except ImportError:
    print("Библиотека 'colorama' не установлена!")
    print("Установить: pip install colorama==0.0.4")