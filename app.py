from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    profile = {
        "name": "Aditi Varshney",
        "title": "DevOps Engineer",
        "experience": "2.6+ Years",
        "company": "Tata Consultancy Services",
        "period": "Sep 2023 – Present",
        "location": "India",
        "email": "aditi8886886@gmail.com",
        "phone": "+91-7017609405",
        "linkedin": "https://linkedin.com/in/aditi-varshney-b9574b217",
        "github": "https://github.com/AditiVar",
        "summary": (
            "Results-driven DevOps Engineer with 2.6+ years at Tata Consultancy Services — "
            "specializing in CI/CD pipeline design, Linux server administration, infrastructure "
            "monitoring, and automation. Building scalable, observable, and secure infrastructure "
            "in high-performance engineering environments."
        ),
        "stats": [
            {"number": "2.6+", "label": "Years Experience"},
            {"number": "~70%", "label": "Manual Checks Reduced"},
            {"number": "~85%", "label": "QA Effort Saved"},
            {"number": "9.54", "label": "Graduation CGPA"},
        ],
        "skills": [
            {
                "icon": "⚙️",
                "icon_bg": "rgba(124,106,247,0.12)",
                "title": "CI/CD & Automation",
                "tags": ["Jenkins", "Groovy", "Playwright", "Shell Scripting", "Cron Jobs"],
                "highlights": ["Jenkins"],
            },
            {
                "icon": "📊",
                "icon_bg": "rgba(106,247,196,0.12)",
                "title": "Monitoring & Observability",
                "tags": ["Prometheus", "Grafana", "Node Exporter", "Custom Alerting"],
                "highlights": ["Prometheus", "Grafana"],
            },
            {
                "icon": "🖥️",
                "icon_bg": "rgba(247,194,106,0.12)",
                "title": "Infrastructure & OS",
                "tags": ["Linux (RHEL 7/8)", "Server Migration", "SSH", "Backup Automation"],
                "highlights": ["Linux (RHEL 7/8)"],
            },
            {
                "icon": "💻",
                "icon_bg": "rgba(124,106,247,0.12)",
                "title": "Scripting & Languages",
                "tags": ["Python", "Shell", "Java", "Groovy"],
                "highlights": ["Python"],
            },
            {
                "icon": "🐳",
                "icon_bg": "rgba(106,247,196,0.12)",
                "title": "Containerization & Security",
                "tags": ["Docker", "Vulnerability Scanning", "Java-based tooling"],
                "highlights": ["Docker"],
            },
            {
                "icon": "🗄️",
                "icon_bg": "rgba(247,194,106,0.12)",
                "title": "Databases & Version Control",
                "tags": ["MySQL", "Git", "GitHub", "Flask"],
                "highlights": ["MySQL"],
            },
        ],
        "projects": [
            {
                "icon": "🔄",
                "title": "Server Migration & Backup",
                "bullets": [
                    "Migrated production backup server using SSH + cron across 4 servers — zero data loss",
                    "Upgraded 4 servers RHEL 7 → RHEL 8 with 100% system integrity",
                ],
                "tools": ["Linux", "Shell", "RHEL"],
            },
            {
                "icon": "📡",
                "title": "Monitoring Dashboard",
                "bullets": [
                    "Built real-time Jenkins monitoring dashboard cutting manual health checks by ~70%",
                    "Reduced incident response time by 40%, bottleneck detection 3x faster",
                ],
                "tools": ["Prometheus", "Grafana", "Node Exporter"],
            },
            {
                "icon": "🛠️",
                "title": "System Administration Tool",
                "bullets": [
                    "Python/Flask tool tracking 5+ metrics (CPU, memory, storage, services) in real time",
                    "Automated email alerts reduced MTTR by ~35%",
                ],
                "tools": ["Python", "Flask", "Jenkins"],
            },
            {
                "icon": "🚀",
                "title": "CI/CD Pipeline Engineering",
                "bullets": [
                    "Built Jenkins CI/CD pipelines cutting deployment time by ~30%",
                    "Reduced manual steps by 60%, improved pipeline reliability",
                ],
                "tools": ["Jenkins", "Groovy"],
            },
            {
                "icon": "🧪",
                "title": "Test Automation (Playwright)",
                "bullets": [
                    "Reduced manual QA effort by 85%; test suite from 2–3 hrs to ~1 hr",
                    "Enabled overnight cron runs with automated email notifications",
                ],
                "tools": ["Playwright", "Cron", "Jenkins"],
            },
            {
                "icon": "🔐",
                "title": "Security & Vulnerability Mgmt",
                "bullets": [
                    "Learned JAR creation process for Java-based security tool",
                    "Documented full process for independent team deployments into pipeline",
                ],
                "tools": ["Java", "JAR"],
            },
        ],
        "education": [
            {
                "degree": "B.Sc. Computer Science (Hons)",
                "institution": "University of Delhi",
                "year": "2022",
                "cgpa": "9.54",
            },
            {
                "degree": "Senior Secondary — PCM & CS",
                "institution": "Jamia Millia Islamia",
                "year": "2019",
                "cgpa": "9.15",
            },
        ],
        "certifications": [
            {"icon": "🏅", "name": "Advanced Certification in DevOps", "issuer": "RJP Infotex"},
            {"icon": "🔄", "name": "DevOps CI/CD", "issuer": "TCS"},
            {"icon": "🐧", "name": "Unix / Linux Basics and Commands", "issuer": "TCS"},
            {"icon": "📦", "name": "Nexus Artifact Repository", "issuer": "TCS Digital (Fresco Play)"},
            {"icon": "🌿", "name": "Git Essential Training", "issuer": "LinkedIn Learning"},
            {"icon": "☕", "name": "Advanced Java Programming", "issuer": "LinkedIn Learning"},
            {"icon": "☁️", "name": "Google Cloud Facilitator Program", "issuer": "Google Cloud"},
        ],
        "awards": [
            {"emoji": "🏆", "name": "Elevate Wings Award", "desc": "TCS recognition for exceptional contribution to the team and organization"},
            {"emoji": "⚡", "name": "Xcelerate Warrior Certificate", "desc": "TCS performance excellence award for outstanding results"},
            {"emoji": "🌟", "name": "Special Initiative Award", "desc": "Recognized for outstanding project initiative and proactive ownership"},
            {"emoji": "💻", "name": "Coding Competitions", "desc": "Participant in ALGORYTHM & Code-A-Thon competitions"},
        ],
    }
    return render_template("index.html", p=profile)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
