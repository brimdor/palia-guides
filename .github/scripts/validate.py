import json, os, sys

data = json.load(open('guides.json'))
errors = 0
for i, g in enumerate(data):
    if 'slug' not in g or 'title' not in g:
        print(f'ERROR: entry {i} missing slug or title')
        errors += 1
        continue
    html = g['slug'] + '.html'
    if not os.path.exists(html):
        print(f'ERROR: {html} referenced in guides.json but file not found')
        errors += 1
    else:
        print(f'OK: {html} - {g["title"]}')

print(f'\n{len(data)} guides checked, {errors} errors')
sys.exit(errors)
