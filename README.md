# nagios-api

## NAME
nagios-api - presents a REST-like JSON interface to Nagios


## SYNOPSIS
nagios-api [OPTIONS]


## DEPENDENCIES
Dependencies include: diesel, greenlet and python-openssl bindings. These
should be available via pip/easy_install.


## DESCRIPTION
This program provides a simple REST-like interface to Nagios. Run this
on your Nagios host and then sit back and enjoy a much easier, more
straightforward way to accomplish things with Nagios. You can use the
bundled nagios-cli, but you may find it easier to write your own system
for interfacing with the API.


## USAGE
Usage is pretty easy:

    nagios-api -p 8080 -c /var/lib/nagios3/rw/nagios.cmd \
        -s /var/cache/nagios3/status.dat -l /var/log/nagios3/nagios.log

You must at least provide the status file options. If you don't provide
the other options, then we will disable that functionality and error to
clients who request it.


## HTTP USAGE
The server speaks JSON. You can either GET data from it or POST data to
it and take an action. It's pretty straightforward, here's an idea of
what you can do from the command line:

    curl http://localhost:8080/state

That calls the `state` method and returns the JSON result.

    curl -d '{"host": "web01", "duration": 600}' \
      http://localhost:8080/schedule_downtime

This POSTs the given JSON object to the `schedule_downtime` method. You
will note that all objects returned follow a predictable format:

    {"content": <object>, "result": <bool>}

The `result` field is always `true` or `false`, allowing you to
determine at a glance if the command succeeded. The `content` field may
be any valid JavaScript object: an int, string, null, bool, hash, list,
etc etc. What is returned depends on the method being called.


## AUTHOR
Written by Mark Smith <mark@qq.is> while under the employ of Bump
Technologies, Inc.

updated By Flip Hess for all the Byte customizations :) 2014


## COPYING
See the LICENSE file for licensing information.
