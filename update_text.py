import re
import urllib.parse

html_file = 'index-1.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new content for each image
updates = {
    "WhatsApp Image 2026-08-27 at 9.48.16 PM.jpeg": {
        "tag": "VLAN & Campus",
        "title": "Multi-Floor Campus Network",
        "desc": "A campus network design featuring 1st, 2nd, and 3rd floors with distinct departments. Implemented Inter-VLAN routing across core routers to ensure segmented and secure traffic.",
        "stack": "<span>Campus Network</span><span>VLANs</span><span>Routing</span>"
    },
    "WhatsApp Image 2026-08-27 at 9.48.17 PM (1).jpeg": {
        "tag": "OSPF Routing",
        "title": "Multi-Area OSPF Configuration",
        "desc": "Configured multiple OSPF areas (Area 0, 20, 30, 40) in Cisco Packet Tracer. Successfully verified end-to-end connectivity with ping tests across the backbone and standard areas.",
        "stack": "<span>OSPF</span><span>Multi-Area</span><span>Verification</span>"
    },
    "WhatsApp Image 2026-08-27 at 9.48.17 PM (2).jpeg": {
        "tag": "WAN Topology",
        "title": "Home, Central & Branch WAN",
        "desc": "A wide area network topology integrating a Home Office via modem/internet, a Branch site, and a Central corporate site. Includes Intranet routing and redundant switch fabrics.",
        "stack": "<span>WAN</span><span>Intranet</span><span>Redundancy</span>"
    },
    "WhatsApp Image 2026-08-27 at 9.48.17 PM.jpeg": {
        "tag": "Enterprise Design",
        "title": "Enterprise Network with VPN & DMZ",
        "desc": "A massive enterprise topology connecting a Central site, Branch site, and Mobile networks. Features an IPsec VPN tunnel and a fully functional DMZ hosting HTTP, FTP, Syslog, and DNS servers.",
        "stack": "<span>DMZ</span><span>IPsec VPN</span><span>Enterprise</span>"
    },
    "WhatsApp Image 2026-08-27 at 9.50.09 PM (1).jpeg": {
        "tag": "CCNA Helper",
        "title": "CCNA Helper Service Topology",
        "desc": "A custom network topology designed for CCNA training and helper services, demonstrating clear divisional routing between West, East, and Admin network sectors.",
        "stack": "<span>CCNA</span><span>Custom Topology</span><span>Training</span>"
    },
    "WhatsApp Image 2026-08-27 at 9.50.09 PM.jpeg": {
        "tag": "Packet Tracer",
        "title": "Basic Routing & Switching",
        "desc": "Close-up configuration of GigabitEthernet router interfaces and switch-to-PC access ports, ensuring fundamental network connectivity and proper interface addressing.",
        "stack": "<span>Interfaces</span><span>Switching</span><span>Access Ports</span>"
    }
}

# Iterate through the projects to update the text
def update_project(match):
    project_html = match.group(0)
    
    # Find which image is in this project
    img_match = re.search(r'<img src="([^"]+)"', project_html)
    if not img_match: return project_html
    
    img_src = urllib.parse.unquote(img_match.group(1))
    
    if img_src in updates:
        data = updates[img_src]
        
        # Replace tag
        project_html = re.sub(r'<span class="tag">.*?</span>', f'<span class="tag">{data["tag"]}</span>', project_html)
        # Replace title
        project_html = re.sub(r'<h3>.*?</h3>', f'<h3>{data["title"]}</h3>', project_html)
        # Replace description
        project_html = re.sub(r'<p>.*?</p>', f'<p>{data["desc"]}</p>', project_html)
        # Replace stack
        project_html = re.sub(r'<div class="stack-list">\s*.*?\s*</div>', f'<div class="stack-list">\n          {data["stack"]}\n        </div>', project_html, flags=re.DOTALL)
        
    return project_html

# Regex to match each project div
project_pattern = re.compile(r'<div class="project reveal".*?</div>\s*</div>\s*</div>', re.DOTALL)
content = project_pattern.sub(update_project, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated project descriptions based on image contents.')
