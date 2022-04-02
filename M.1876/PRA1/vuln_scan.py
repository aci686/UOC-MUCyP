#!/usr/bin/env python3

#

__author__ = "Aaron Castro"
__author_email__ = "aaron.castro.sanchez@outlook.com"
__author_nick__ = "i686"
__copyright__ = "Aaron Castro"
__license__ = "MIT"

import sys, signal, argparse, subprocess, json

# CTRL+C Handler
def signal_handler(signal, frame):
    print("\r[!] Interrupted! Exiting...")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Arument Parser
def get_arguments():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")
    required.add_argument("-i", "--image", help="docker image to scan", type=str, required=True)
    required.add_argument("-s", "--severity", help="show vulnerabilities for this level", choices=["medium", "high"], type=str, required=True)
    parser.add_argument("-k", "--keystring", help="key string to look for", type=str, default="")
    
    args = parser.parse_args()

    return(args)

# Vulnerability scanner
def scan_vulns(image, severity, keystring):
    print("[i] Scanning {}...".format(image))
    # Run docker scan to the selected image and capture output
    scan = subprocess.run(["docker", "scan", "--severity", severity, "--json", image], capture_output=True, text=True)
    json_file = json.loads(scan.stdout)
    data = json_file["vulnerabilities"]
    flag = False
    CVE = []
    # Loop docker scan output
    for _ in data:
        # Match criteria
        if severity in _["severity"] and keystring in _["description"]:
            if _["identifiers"]["CVE"][0] not in CVE:
                print("[+] Found {} vulnerability. Please check {}".format(_["title"], _["identifiers"]["CVE"][0]))
            CVE.append(_["identifiers"]["CVE"][0])
            flag = True
    if not flag:
        print("[i] No {} severity vulnerabilites found on {} related to {}".format(severity, image, keystring))

# Core script function
def main():
    args = get_arguments()

    # Check if docker image exists
    images=subprocess.run(["docker", "image", "ls", args.image], capture_output=True, text=True)
    if args.image in images.stdout:
        scan_vulns(args.image, args.severity, args.keystring)
    else:
        print("[-] Specified docker image does not exist...")
        exit(0)

if __name__ == "__main__":
    main()
