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
