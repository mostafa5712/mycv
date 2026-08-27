import re

html_file = 'index-1.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

unsplash_projects = '''
    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Security</span>
        <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80" alt="Cyber Security">
      </div>
      <div class="project-info">
        <span class="p-index">Showcase 01</span>
        <h3>Network Security Architecture</h3>
        <p>Implementation of robust security protocols and monitoring traffic patterns to secure enterprise networks against external threats.</p>
        <div class="stack-list">
          <span>Security</span><span>Monitoring</span><span>Defense</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Infrastructure</span>
        <img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=800&q=80" alt="Networking">
      </div>
      <div class="project-info">
        <span class="p-index">Showcase 02</span>
        <h3>Advanced Routing & Switching</h3>
        <p>Designing complex topologies incorporating multiple VLANs and advanced routing protocols to ensure scalable network infrastructure.</p>
        <div class="stack-list">
          <span>Switches</span><span>Routers</span><span>VLAN</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Systems</span>
        <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="Servers">
      </div>
      <div class="project-info">
        <span class="p-index">Showcase 03</span>
        <h3>Server Administration</h3>
        <p>Deployment and management of Windows and Linux servers, configuring Active Directory, and maintaining reliable server environments.</p>
        <div class="stack-list">
          <span>Windows Server</span><span>Linux</span><span>AD</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Hardware</span>
        <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80" alt="IT Helpdesk">
      </div>
      <div class="project-info">
        <span class="p-index">Showcase 04</span>
        <h3>IT Hardware Diagnostics</h3>
        <p>Comprehensive troubleshooting of hardware components, ensuring optimal performance and minimizing downtime in enterprise workstations.</p>
        <div class="stack-list">
          <span>Diagnostics</span><span>Maintenance</span><span>Support</span>
        </div>
      </div>
    </div>
'''

content = content.replace('</section>\n\n  <section id="contact">', unsplash_projects + '\n  </section>\n\n  <section id="contact">')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added unsplash images back successfully.")
