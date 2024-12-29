import subprocess
import time


install_commands = [
    "apt-get update",
    "apt-get upgrade -y",
    "apt install net-tools -y",
    "apt-get install dnsutils -y",
    "apt install sslscan -y",
    "apt install fierce -y",
    "apt install network-manager -y",
    "apt -y install resolvconf",
    "apt-get -y install dnsmasq",
    "apt-get install ssh -y",
    "apt-get install iptables -y",
    "apt-get install curl -y",
    "apt-get install bleachbit -y",
    "apt-get install privoxy -y",
    "apt-get install tor -y",
    "apt-get install macchanger -y",
    "systemctl enable ssh",
    "systemctl enable dnsmasq",
    "systemctl enable NetworkManager.service",
    "systemctl enable resolvconf",
    "systemctl start ssh",
    "systemctl start dnsmasq",
    "systemctl start NetworkManager.service",
    "apt install finalrecon -y",
    "apt install theharvester -y",
    "apt install dnsenum -y",
    "apt install dnsrecon -y",
    "apt install wpscan -y",
    "apt install nmap -y",
    "apt install whatweb -y",
    "apt install metagoofil -y",
    "apt-get dist-upgrade -y"
]


for command in install_commands:
    print(f"Executing: {command}")
    process = subprocess.run(command, shell=True, text=True)
    if process.returncode != 0:
        print(f"Command failed: {command}")
        break
    time.sleep(1)


scan_commands = [
    "traceroute -T -O info <domain.com>",
    "fierce --domain <domain.com>",
    "fierce -dns <domain.com>",
    "sslscan <domain.com>",
    "dig <domain.com> mx",
    "finalrecon --full --url <https://<domain.com>",
    "theHarvester -d <domain.com> -l 500 -b all",
    "dnsenum <domain.com>",
    "dnsrecon -t std -d <domain.com>",
    "metagoofil -d <domain.com> -t doc -l 25 -o <domain> -f <domain.html>",
    "whatweb <domain.com>",
    "nmap -Pn -sT -P0 <targetIP> -D 10.0.0.1,10.0.0.2,10.0.0.4",
    "nmap -Pn -n -A -T5 <targetIP> -D 10.0.0.1,10.0.0.2,10.0.0.4",
    "wpscan --url https://<domain.com/wp-content> --ignore-main-redirect --scope --api-token ouxTJCAOxyWXwVKnWgrBSWBo5htFLpyX7JW4UF3371U --verbose --enumerate ap,at",
    "wpscan --url https://<domain.com> --api-token ouxTJCAOxyWXwVKnWgrBSWBo5htFLpyX7JW4UF3371U --force --enumerate u,p,t,tt,cb,dbe",
    "wpscan -u <targetIP> -e u vp"
]


for command in scan_commands:
    print(f"Executing scan: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    with open("scanresults.txt", "a") as f:
        f.write(f"Results for: {command}\n")
        f.write(result.stdout)
        f.write(result.stderr)
        f.write("\n" + "="*40 + "\n")
    time.sleep(1)