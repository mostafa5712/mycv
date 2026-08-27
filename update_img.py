import re
import urllib.parse

html_file = 'index-1.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

images = [
    "WhatsApp Image 2026-08-27 at 9.48.16 PM.jpeg",
    "WhatsApp Image 2026-08-27 at 9.48.17 PM (1).jpeg",
    "WhatsApp Image 2026-08-27 at 9.48.17 PM (2).jpeg",
    "WhatsApp Image 2026-08-27 at 9.48.17 PM.jpeg"
]

unsplash_pattern = r'<img src="https://images\.unsplash\.com/[^"]+"'

def replace_img(match):
    global img_index
    if img_index < len(images):
        img_name = images[img_index]
        img_index += 1
        return f'<img src="{urllib.parse.quote(img_name)}"'
    return match.group(0)

img_index = 0
content = re.sub(unsplash_pattern, replace_img, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated images to local ones.')
