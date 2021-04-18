import re


def normaliz(line):
    symbol_map = {ord("А"): "A", ord("а"): "a", ord("Б"): "B", ord("б"): "b", ord("В"): "V", ord("в"): "v", ord("Г"): "G", ord("г"): "g", ord("Д"): "D", ord("д"): "d", ord("Е"): "E", ord("е"): "e", ord("Ё"): "YO", ord("ё"): "yo", ord("Ж"): "ZH", ord("ж"): "zh", ord("З"): "Z", ord("з"): "z", ord("И"): "I", ord("и"): "i", ord("Й"): "Y", ord("й"): "y", ord("К"): "K", ord("к"): "k", ord("Л"): "L", ord("л"): "l", ord("М"): "M", ord("м"): "m", ord("Н"): "N", ord("н"): "n", ord("О"): "O", ord("о"): "o", ord("П"): "P", ord("п"): "p", ord("Р"): "R", ord("р"): "r", ord("С"): "S", ord("с"): "s", ord("Т"): "T", ord("т"): "t", ord("У"): "U", ord("у"): "u", ord("Ф"): "F", ord("ф"): "f", ord("Х"): "H", ord("х"): "h", ord("Ц"): "C", ord("ц"): "c", ord("Ч"): "CH", ord("ч"): "ch", ord("Ш"): "SH", ord("ш"): "sh", ord("Щ"): "SCH", ord("щ"): "sch", ord("Ъ"): "", ord("ъ"): "", ord("Ы"): "I", ord("ы"): "i", ord("Ь"): "", ord("ь"): "", ord("Э"): "E", ord("э"): "e", ord("Ю"): "YU", ord("ю"): "yu", ord("Я"): "YA", ord("я"): "ya", ord("Є"): "YE", ord("є"): "ye", ord("Ї"): "YI", ord("ї"): "yi"}
    new_line = line.translate(symbol_map)
    clear_line = re.sub(r'[^\w\s]', '_', new_line)
    return clear_line


def main():
    line = input("Write: ")
    print(normaliz(line))
    

if __name__ == "__main__":
    main()
