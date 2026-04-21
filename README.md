# Project Sentinel: NIST 800-53 Linux Auditor
In modern cybersecurity, manual auditing is a bottleneck. This project implements Compliance-as-Code by using Python to automatically "interrogate" a Linux operating system against federal security standards. Instead of manual checklists, this script provides instant, repeatable verification of system hardening.

## What are we doing?
We are building a Python-based security auditor. Instead of a human manually checking settings, your script will "interrogate" the Linux operating system to see if it meets the NIST 800-53 security standards.

## 🛠️ What This Project Demonstrates
By building this auditor, I have mastered and demonstrated the following core competencies:

Regulatory Literacy: Translating high-level NIST 800-53 controls (e.g., AC-8, IA-5) into specific technical configurations within a Linux environment.

Linux Internals & Identity Management: Deep-diving into PAM (Pluggable Authentication Modules) and system metadata files to verify security posture.

Security Automation: Moving away from manual troubleshooting toward scalable, automated security enforcement.

GRC Strategy: Bridging the gap between business compliance requirements and hands-on technical implementation.

## 🛡️ Targeted NIST Controls
This auditor currently validates three critical areas of the Access Control (AC) and Identification & Authentication (IA) families:

```markdown
| Control ID | Name | Technical Check |
| :--- | :--- | :--- |
| **AC-8** | System Use Notification | Verify banner in `/etc/issue` |
| **IA-5 (1)** | Password Management | Check `pam_pwquality` in `/etc/pam.d/` |
| **AC-2** | Account Management | Scan for users inactive > 90 days |

## 🚀 How It Works
The script utilizes Python’s os and subprocess libraries to audit the system.

Prerequisites
Python 3.x

Root/Sudo privileges (Required to access sensitive configuration files like /etc/pam.d/)

### 💻 Usage

```bash
# Clone the repository
git clone [https://github.com/AlleyBeeeeee/NIST-800-53-Linux-Auditor.git](https://github.com/AlleyBeeeeee/NIST-800-53-Linux-Auditor.git)

# Navigate to the directory
cd NIST-800-53-Linux-Auditor

# Run the auditor
sudo python3 audit.py

📊 Sample Output
Upon completion, the tool generates a audit_report.md file. This report serves as a formal artifact for compliance officers, mapping technical "Pass/Fail" results directly to NIST Control IDs.
