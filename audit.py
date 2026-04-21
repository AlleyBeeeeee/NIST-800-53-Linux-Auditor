import os
import subprocess
from datetime import datetime

# --- Helper Function for NIST AC-2 ---
def check_inactive_users():
    """Scans the system for users who haven't logged in for 90 days."""
    try:
        # Run the linux command 'lastlog -b 90'
        process = subprocess.run(['lastlog', '-b', '90'], capture_output=True, text=True)
        inactive_output = process.stdout.strip()
        
        # Check if there are results beyond the header line
        if len(inactive_output.split('\n')) <= 1:
            return "PASS", "AC-2: No stale accounts (inactive > 90 days) detected."
        else:
            return "FAIL", f"AC-2: Inactive users found:\n{inactive_output}"
    except Exception as e:
        return "ERROR", f"AC-2: Could not execute check. Error: {e}"

# --- Main Audit Logic ---
def run_audit():
    # 1. Prepare the Report Header
    report_content = f"# NIST 800-53 Audit Report\n"
    report_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report_content += "---\n\n"

    # 2. CHECK AC-8 (Legal Banner)
    if os.path.exists("/etc/issue") and os.path.getsize("/etc/issue") > 0:
        report_content += "### [PASS] AC-8: System Use Notification\n- Legal banner is present in `/etc/issue`.\n\n"
    else:
        report_content += "### [FAIL] AC-8: System Use Notification\n- **Risk:** No pre-login warning.\n\n"

    # 3. CHECK IA-5 (1) (Password Complexity)
    try:
        with open("/etc/pam.d/common-password", "r") as f:
            if "pam_pwquality.so" in f.read():
                report_content += "### [PASS] IA-5 (1): Password Management\n- `pam_pwquality` is active.\n\n"
            else:
                report_content += "### [FAIL] IA-5 (1): Password Management\n- **Risk:** Weak password rules enabled.\n\n"
    except FileNotFoundError:
        report_content += "### [ERROR] IA-5 (1): Could not locate configuration file.\n\n"

    # 4. CHECK AC-2 (Inactive Users)
    status, msg = check_inactive_users()
    report_content += f"### [{status}] {msg}\n\n"

    # 5. Save the Report to a Markdown file
    with open("audit_report.md", "w") as f:
        f.write(report_content)
    
    print("✅ Audit Complete! Results saved to 'audit_report.md'")

# This tells Python to run the audit function when we start the script
if __name__ == "__main__":
    run_audit()