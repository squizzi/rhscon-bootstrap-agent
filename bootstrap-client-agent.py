#!/usr/bin/env python
import os
import sys
import paramiko
import argparse

"""
Configure argument parsing
"""
parser = argparse.ArgumentParser(description='Bootstrap a client agent \
                                for Red Hat Storage Console 2.0')

parser.add_argument("--type",
                    dest="type",
                    required=True,
                    help='Define the type of client agent to bootstrap.  Valid \
                    options are mon, osd or rgw.'
parser.add_argument("--host,
                    dest="host",
                    required=True,
                    help='Define a host or list of comma-delimited hosts to \
                    bootstrap.'
parser.add_argument("--server",
                    dest="server",
                    required=True,
                    help='The target FQDN of a Red Hat Storage Console 2.0 \
                    server that clients will be connecting too')
args = parser.parse_args = ()

"""
Build a list of hosts
"""

"""
Bootstrap prereqs
"""
# The only different between the types is the repo subscription that is ran
# depending on the type installed
if args.type == 'mon' or args.type == 'osd' or args.type == 'rgw':
    raise NameError('The --type provided is invalid')

# Issue the correct subscription-manager repos --enable command for each type
if args.type == 'mon':
    repo_type = 'mon'
if args.type == 'osd':
    repo_type = 'osd'
if args.type == 'rgw':
    repo_type = 'tools'

rootPassword = getpass.getpass('Enter the root password for the host(s): '
reposHosts = "subscription-manager repos --disable=* ; subscription-manager repos --enable=rhel-7-server-rhceph-2-{0}-rpms --enable=rhel-7-server-rhscon-2-agent-rpms --enable=rhel-7-server-rhscon-2-installer-rpms --enable=rhel-7-server-rpms".format(repo_type)
for each in host_list:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(each,
                username="root",
                password=rootPassword,
                look_for_keys=False
                )
stdin, stdout, stderr = ssh.exec_command(reposHosts)
# Wait for the subscription-manager commands to run
exit_status = stdout.channel.recv_exit_status()
if exit_status == 0:
    pass
else:
    print("Error subscribing host {0} to agent repositories. {1}".format(each, exit_status)
    client.close()
    sys.exit(1)

"""
Bootstrap client agent(s)
"""
bootstrapCommand = 'yum update -y ; systemctl start ntpd ; curl https://ceph1.hq.gsslab.rdu.redhat.com:8181/setup/agent | bash'
stdin, stdout, stderr = ssh.exec_command(reposHosts)
# Wait for the register commands to run before continuing
# to prevent problems during build_playbook()
exit_status = stdout.channel.recv_exit_status()
if exit_status == 0:
    pass
else:
    print("Error during bootstrap of host {0}. {1}".format(each, exit_status)
    client.close()
    sys.exit(1)

print(
"""The client agent has been installed and configured but may take a few moments
to appear in the Red Hat Storage Console web interface"""