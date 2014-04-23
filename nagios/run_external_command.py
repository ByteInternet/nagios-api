import logging
import logging.handlers
import subprocess


LOGOBJECT = None


def logger():
    global LOGOBJECT
    if LOGOBJECT:
        return LOGOBJECT

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)-7s %(message)s")
    log = logging.getLogger(name=__name__)
    log.setLevel(logging.DEBUG)

    # logging to std err
    errlog = logging.StreamHandler()
    errlog.setLevel(logging.DEBUG)
    errlog.setFormatter(formatter)
    log.addHandler(errlog)

    LOGOBJECT = log
    return LOGOBJECT


def get_stats():
    ''' Get icinga statistics in json format using the icingastats binary'''
    stats = {}
    output, exitcode = run_command("""/usr/sbin/icingastats | sed -e '1,9d' -e 's/  */ /g' -e 's/^\ //g' -e '/^$/d'""")
    if exitcode != 0:
        return { 'output': output, 'exitcode': exitcode }
    for line in output:
        key, value = line.split(':')
        newkey = key.replace(' ', '_').lower()
        stats[newkey] = value.strip().lstrip()
    return stats


def run_command(command):
    ''' Run a shell command and get the output and exit code 
        while the output is send to both logging and returned. 
    '''
    output = []
    log = logger()
    log.info('Command = %s' % command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() != None:
            break
        elif nextline == '\n' or nextline == '':
            continue
        output.append(nextline.strip())
        log.info('%s - %s' % (__name__, nextline.strip()))
    exitcode = process.returncode
    log.info('Exitcode for %s was %s' % (command, exitcode))
    return(output, exitcode)
