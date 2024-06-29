import yaml

with open('ascii-templates.yaml') as stream:
    try:
        ascii_templates = yaml.safe_load(stream)
    except e:
        print(e)
        exit(1)

for k, v in ascii_templates.items():
    lines = v.splitlines()
    if len(lines) != 5:
        raise Exception(f'template "{k}" wrong number lines - {len(lines)}')
    for line in lines:
        if len(line) != 3:
            raise Exception(f'template "{k}" wrong line len - {len(line)}')

    ascii_templates[k] = \
            ascii_templates[k]\
            .replace('.', '{spacer}')\
            .replace('x', '{template_char}')

def has_template(letter):
    return letter in ascii_templates

def fill_template(letter, spacer, template_char):
    return ascii_templates[letter].format(spacer = spacer, template_char = template_char)

def fill_template(phrase, spacer, template_char):
    ret = ''
    for i in range(5):
        for letter in filt_phrase[t:tt]:
            ret += get_ascii_template(letter, spacer, emoji) 
            ret += ' ' * 3

        ret += '\n'

    if ret[0] == ' ':
        ret = '.' + ret[1:]

    return ret

