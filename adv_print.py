def adv_print(*args, **kwargs):
    source = str(args[0])
    if kwargs.get('start') is None:
        start = '\n'
    else:
        start = kwargs['start'] + '\n'
    if kwargs.get('max_line') is None:
        max_line = 0
    else:
        max_line = int(kwargs['max_line'])
    if kwargs.get('in_file') is None:
        in_file = None
    else:
        in_file = kwargs['in_file']
    def source_format(source): # на основе решения http://www.cyberforum.ru/python-beginners/thread1799717.html
        if max_line == 0:
            proxy_text = source
        else:
            proxy_text = ''
            counter = 0
            for word in source.split():
                counter += len(word)
                if counter > max_line:
                    proxy_text += '\n'
                    counter = len(word)
                elif proxy_text != '':
                    proxy_text += ' '
                    counter += 1
                proxy_text += word
        return proxy_text
    result = '' + start + source_format(source)
    def output_file(in_file):
        if in_file == None:
            pass
        else:
            with open(in_file, 'wt', encoding='utf-8') as document:
                document.write(result)
    output_file(in_file)
    print(result)

if __name__ == '__main__':
    a = "Антиутопия (от «анти-» и «утопия»), также дистопия (" \
        "dystopia, букв. «плохое место» от греч. δυσ «отрицание» + " \
        "греч. τόπος «место») или какотопия (kakotopia или " \
        "cacotopia от греч. κακός «плохой») — изображение " \
        "общественного строя или сообщества, представляющегося " \
        "автору или критику нежелательным, отталкивающим или " \
        "пугающим. Является противоположностью утопии или её " \
        "деривацией.\n Антиутопические общества описаны во многих " \
        "художественных произведениях, действие которых в " \
        "литературе Нового времени происходит в будущем. " \
        "Антиутопия как жанр зачастую используется, чтобы обратить " \
        "внимание на реальные для автора проблемы в окружающей " \
        "среде, политике, экономике, религии, технологии и др. В " \
        "литературоведении XX—XXI веков антиутопии, как и утопии, " \
        "рассматриваются в ряду жанров научной фантастики. "

    adv_print('Задача 3\n')
    adv_print('Печать с указанием аргументов: \n')
    adv_print(a, start='Тест adv_print', max_line=25,
              in_file='example.txt')

    adv_print('\nПечать без аргументов\n')
    adv_print(a)
