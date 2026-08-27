import re

html_file = 'index-1.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Hero Section
content = re.sub(
    r'<p class="hero-sub">.*?</p>',
    '<p class="hero-sub">Highly motivated IT Specialist and Information Systems graduate specializing in enterprise networking, IT helpdesk support, and Cisco CyberOps cybersecurity methodologies.</p>',
    content, count=1, flags=re.DOTALL)

# Update About
new_about_html = '''<section id="about">
    <div class="section-head">
      <span class="idx">01</span><h2>About</h2><span class="rule"></span>
    </div>
    <div class="about-grid reveal">
      <div>
        <p>I\\'m <strong>Mostafa Mohamed Elsayed Elmashad</strong>, a highly motivated Information Technology Specialist and Information Systems graduate from <strong>Tanta Institute of Computers and Information Systems</strong> (Class of 2026).</p>
        <p>With a strong foundation in networking, IT helpdesk support, and cybersecurity, I am proficient in troubleshooting complex hardware/software issues and managing network infrastructure. My approach integrates <strong>Cisco CyberOps methodologies</strong> to apply robust security protocols.</p>
        <p>I continuously embrace learning and adaptability, eager to contribute to dynamic IT teams and resolve technical challenges efficiently.</p>
      </div>
      <div>
        <div class="stat-card"><div class="n">2026</div><div class="l">Information Systems Graduate</div></div>
        <div class="stat-card"><div class="n">NTI</div><div class="l">Intensive IT Infrastructure Training</div></div>
        <div class="stat-card"><div class="n">CyberOps</div><div class="l">Cisco Security Methodologies</div></div>
      </div>
    </div>
  </section>'''
content = re.sub(r'<section id="about">.*?(?=<section id="skills">)', new_about_html + '\n\n  ', content, flags=re.DOTALL)

# Update Skills
new_skills_html = '''<section id="skills">
    <div class="section-head">
      <span class="idx">02</span><h2>Skills & Technologies</h2><span class="rule"></span>
    </div>
    <div class="skill-grid reveal">
      <span class="skill-chip">Networking (LAN/WAN)</span>
      <span class="skill-chip">Routing & Switching</span>
      <span class="skill-chip">TCP/IP & Subnetting</span>
      <span class="skill-chip">Windows Server & Linux</span>
      <span class="skill-chip">Active Directory</span>
      <span class="skill-chip">IT Helpdesk & Support</span>
      <span class="skill-chip">Hardware Diagnostics</span>
      <span class="skill-chip">CyberOps & Threat Analysis</span>
      <span class="skill-chip">Kali Linux & Security Onion</span>
      <span class="skill-chip">Vulnerability Mitigation</span>
      <span class="skill-chip">Cisco Packet Tracer</span>
      <span class="skill-chip">Analytical Problem Solving</span>
    </div>
  </section>'''
content = re.sub(r'<section id="skills">.*?(?=<section id="projects">)', new_skills_html + '\n\n  ', content, flags=re.DOTALL)

# Update Projects
new_projects_html = '''<section id="projects">
    <div class="section-head">
      <span class="idx">03</span><h2>Projects & Experience</h2><span class="rule"></span>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">CyberOps</span>
        <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80" alt="Cyber Security">
      </div>
      <div class="project-info">
        <span class="p-index">Project 01</span>
        <h3>CyberOps Labs & Security Analysis</h3>
        <p>Analyzed network traffic and security alerts using virtualized environments like Kali Linux and Security Onion to detect potential security breaches and mitigate risks based on Cisco CyberOps methodologies.</p>
        <div class="stack-list">
          <span>Kali Linux</span><span>Security Onion</span><span>Threat Analysis</span><span>Incident Response</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">Network Design</span>
        <img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=800&q=80" alt="Networking">
      </div>
      <div class="project-info">
        <span class="p-index">Project 02</span>
        <h3>Enterprise Network Simulation</h3>
        <p>Designed and simulated enterprise network architectures using Cisco Packet Tracer. Implemented VLANs, advanced routing protocols, and access control lists (ACLs) to ensure secure and efficient data flow.</p>
        <div class="stack-list">
          <span>Packet Tracer</span><span>VLANs</span><span>Routing & Switching</span><span>ACLs</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">IT Infrastructure</span>
        <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="Servers">
      </div>
      <div class="project-info">
        <span class="p-index">Training & Certifications</span>
        <h3>NTI IT Training & Systems Admin</h3>
        <p>Completed an intensive, hands-on program at the National Telecommunication Institute (NTI) focused on modern IT infrastructure, systems administration (Windows Server, Linux), and enterprise networking.</p>
        <div class="stack-list">
          <span>NTI</span><span>Windows Server</span><span>Linux</span><span>Active Directory</span>
        </div>
      </div>
    </div>

    <div class="project reveal" style="transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
      <div class="project-media">
        <span class="tag">IT Support</span>
        <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80" alt="IT Helpdesk">
      </div>
      <div class="project-info">
        <span class="p-index">Experience</span>
        <h3>IT Helpdesk & Diagnostics</h3>
        <p>Proficient in hardware diagnostics, software configuration, end-user support, and Active Directory management. Dedicated to solving complex IT issues and improving overall system performance.</p>
        <div class="stack-list">
          <span>Helpdesk</span><span>Hardware Diagnostics</span><span>Troubleshooting</span>
        </div>
      </div>
    </div>

  </section>'''
content = re.sub(r'<section id="projects">.*?(?=<section id="contact">)', new_projects_html + '\n\n  ', content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('File updated successfully.')
