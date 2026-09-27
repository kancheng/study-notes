def G(name, meaning, rows, examples):
    return {
        'name': name,
        'meaning': meaning,
        'rows': [list(row) for row in rows],
        'examples': [list(pair) for pair in examples],
    }


def L(slug, level, title, h1, intro, card, tip, groups, cols=('用法', '形式', '中文')):
    return {
        'slug': slug,
        'level': level,
        'title': title,
        'h1': h1,
        'intro': intro,
        'card': card,
        'tip': tip,
        'groups': groups,
        'cols': list(cols),
        'pdf': f'{slug}.pdf',
        'pdf_sub': '對照、例句、中文翻譯',
        'meta': f'{level} · 文法 · 例句跟讀',
    }
