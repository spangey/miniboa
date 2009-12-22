#!/usr/bin/env python
#------------------------------------------------------------------------------
#   chat_server.py
#   Copyright 2009 Jim Storch
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain a
#   copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#------------------------------------------------------------------------------

"""
Example of using on_connect and on_disconnect handlers.
"""

from miniboa.async import TelnetServer


CLIENTS = []

def my_on_connect(client):
    """Example on_connect handler."""
    client.send('You connected from %s\r\n' % client.addrport())
    if CLIENTS:
        client.send('Also connected are:\r\n')
        for neighbor in CLIENTS:
            client.send('%s\r\n' % neighbor.addrport())
    else:
        client.send('Sadly, you are alone.\r\n')
    CLIENTS.append(client)


def my_on_disconnect(client):
    """Example on_disconnect handler."""
    CLIENTS.remove(client)


server = TelnetServer()
server.on_connect=my_on_connect
server.on_disconnect=my_on_disconnect

print "\n\nStarting server on port %d.  CTRL-C to interrupt.\n" % server.port
while True:
    server.poll()