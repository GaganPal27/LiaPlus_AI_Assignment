# This script automates the process of setting up a server by installing necessary packages
#  (like nginx, python3, git), and configuring a basic firewall using ufw (Uncomplicated Firewall).

import os
import subprocess

packages = ['nginx', 'python3', 'python3-pip', 'git']

# Firewall configuration
allowed_ports = ['22', '80', '443']  # Allow SSH, HTTP, and HTTPS

def install_packages():
    print("Updating package lists...")
    subprocess.run(['sudo', 'apt-get', 'update'])

    print("Installing necessary packages...")
    for package in packages:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package])

def setup_firewall():
    print("Setting up the firewall...")
    subprocess.run(['sudo', 'ufw', 'allow', 'OpenSSH'])
    for port in allowed_ports:
        subprocess.run(['sudo', 'ufw', 'allow', port])

    print("Enabling the firewall...")
    subprocess.run(['sudo', 'ufw', 'enable'])

def clone_repository(repo_url, target_dir):
    print(f"Cloning repository from {repo_url}...")
    subprocess.run(['git', 'clone', repo_url, target_dir])

def start_nginx():
    print("Starting Nginx server...")
    subprocess.run(['sudo', 'systemctl', 'start', 'nginx'])

def restart_nginx():
    print("Restarting Nginx server...")
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'])

def main():
    repo_url = "https://github.com/xxxxxxxxxx/repo.git" 
    target_dir = "/var/www/xxxxx"

    install_packages()
    setup_firewall()
    clone_repository(repo_url, target_dir)
    start_nginx()
    restart_nginx()

    print("Server setup completed successfully!")

if __name__ == '__main__':
    main()
