""" https://edisciplinas.usp.br/pluginfile.php/
5092237/mod_resource/content/1/estruturas.pdf """


class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        try:
            if index < len(self.data) and index >= 0:
                return self.data[index]
            else:
                raise IndexError
        except IndexError:
            raise IndexError
