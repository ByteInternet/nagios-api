## NAGIOS-CLI USAGE
Once your API server is up and running you can access it through the
included nagios-cli script. The script now has some decent built-in help
so you should be able to get all you need:

    nagios-cli -h

The original raw JSON mode is still supported by passing the --raw
option.


## OPTIONS
    -p, --port=PORT

Listen on port 'PORT' for HTTP requests.

    -b, --bind=ADDR

Bind to ADDR for HTTP requests (defaults to all interfaces).

    -c, --command-file=FILE

Use 'FILE' to write commands to Nagios. This is where external
commands are sent. If your Nagios installation does not allow
external commands, do not set this option.

    -s, --status-file=FILE

Set 'FILE' to the status file where Nagios stores its status
information. This is where we learn about the state of the world and
is the only required parameter.

    -l, --log-file=FILE

Point 'FILE' to the location of Nagios's log file if you want to
allow people to subscribe to it.

    -o, --allow-origin=ORIGIN

Modern web browsers implement the Cross-Origin Resource Sharing
specification from W3C. This spec allows you to host your
JavaScript/HTML on one host and have it access an endpoint on a
different service. This requires setting a header on the endpoint,
which this option allows you to do.

You can simply set this header to `*` and not worry about it
if you want to allow all access. For more information see the
[CORS specification](http://www.w3.org/TR/cors/).

    -q, --quiet

If present, we will only print warning/critical messages. Useful if
you are running this in the background.

