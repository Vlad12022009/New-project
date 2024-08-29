def slugify(name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz- '
    name = name.lower().replace(' ', '-')
    for i in name:
        if not i in alphabet:
            name = name.replace(f"{i}", '')
    return name
    


print(slugify('HELLO world!'))