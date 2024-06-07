class Text:
    files = dict()

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.count_line = len(text)
        self.files[len(text)] = self

f1 = Text('1.txt', open('1.txt', encoding="utf-8").readlines())
f2 = Text('2.txt', open('2.txt', encoding="utf-8").readlines())
f3 = Text('3.txt', open('3.txt', encoding="utf-8").readlines())

def write_file(result, file):
    result.write(f'{file.name}\n{file.count_line}\n{"".join(file.text)}\n')

sort = dict(sorted(Text.files.items()))
merge_file = open('merge.txt', 'a', encoding="utf-8")

for key in sort.values():
    write_file(merge_file, key)


