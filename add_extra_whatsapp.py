import re
import urllib.parse

html_file = 'index-1.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

extra_projects = f'''
    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Certification</span>
        <img src="{urllib.parse.quote('WhatsApp Image 2026-08-27 at 9.50.09 PM (1).jpeg')}" alt="Certification">
      </div>
      <div class="project-info">
        <span class="p-index">Certificate 01</span>
        <h3>Professional Certification</h3>
        <p>A testament to ongoing dedication to learning and mastering advanced networking and IT support methodologies.</p>
        <div class="stack-list">
          <span>Achievement</span><span>Growth</span><span>Networking</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Certification</span>
        <img src="{urllib.parse.quote('WhatsApp Image 2026-08-27 at 9.50.09 PM.jpeg')}" alt="Certification">
      </div>
      <div class="project-info">
        <span class="p-index">Certificate 02</span>
        <h3>Technical Excellence</h3>
        <p>Demonstrated capability in technical infrastructure, server diagnostics, and comprehensive network simulation.</p>
        <div class="stack-list">
          <span>Excellence</span><span>Training</span><span>Skills</span>
        </div>
      </div>
    </div>
'''

content = content.replace('</section>\n\n  <section id="contact">', extra_projects + '\n  </section>\n\n  <section id="contact">')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added extra Whatsapp images back successfully.")
