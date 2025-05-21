import subprocess

# Get metadata of all Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

# Extract Wi-Fi profile names
profiles = []
for line in data:
    if "All User Profile" in line:
        profiles.append(line.split(":")[1].strip())

# For each profile, extract the password
for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        password = ""
        for line in results:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break
        print("{:<30} |  {:<}".format(profile, password if password else "No Password Found"))
    except Exception as e:
        print("{:<30} |  {:<}".format(profile, "ERROR OCCURRED"))
# This script retrieves the saved Wi-Fi profiles and their passwords on a Windows machine.
# It uses the 'netsh' command to get the profiles and their details.