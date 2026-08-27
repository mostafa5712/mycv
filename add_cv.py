import re

html_file = 'index-1.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add button in hero section
hero_btn = '''<div style="margin-top: 30px; display: flex; justify-content: center; gap: 15px; animation: riseIn .8s ease forwards; opacity: 0; animation-delay: .8s;">
    <a class="contact-btn" href="Mostafa_Elmashad_CV.pdf" download="Mostafa_Elmashad_CV.pdf">Download CV ↓</a>
  </div>'''

content = re.sub(
    r'(<p class="hero-sub">.*?</p>)',
    r'\1\n  ' + hero_btn,
    content, count=1, flags=re.DOTALL)

# Add button in contact section
contact_btns = '''<div style="display: flex; justify-content: center; gap: 15px;">
        <a class="contact-btn" href="mailto:mostafa5716cc@gmail.com">Send a message →</a>
        <a class="contact-btn" href="Mostafa_Elmashad_CV.pdf" download="Mostafa_Elmashad_CV.pdf" style="background: transparent; border: 1px solid var(--cyan); color: var(--cyan);">Download CV ↓</a>
      </div>'''

content = re.sub(
    r'<a class="contact-btn" href="mailto:mostafa5716cc@gmail.com">Send a message →</a>',
    contact_btns,
    content, count=1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('CV buttons added successfully.')
