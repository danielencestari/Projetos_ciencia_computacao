def exists_word(word, instance):
    data = list()

    for i in range(len(instance)):
        content = instance.search(i)
        find_lines = list()

        for i, line in enumerate(content["linhas_do_arquivo"]):
            line_lower = line.lower()
            if line_lower.find(word.lower()) == -1:
                continue
            else:
                find_lines.append({"linha": i + 1})

        if len(find_lines) > 0:
            data.append({
                "palavra": word,
                "arquivo": content["nome_do_arquivo"],
                "ocorrencias": find_lines
            })
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
