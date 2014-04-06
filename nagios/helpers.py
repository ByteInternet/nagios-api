import sys
import logging
import logging.handlers
import subprocess


LOGOBJECT = None


def logger():
    global LOGOBJECT
    if LOGOBJECT:
        return LOGOBJECT

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)-7s %(message)s")
    log = logging.getLogger(name='byte-vpn-sync-users')
    log.setLevel(logging.DEBUG)

    # logging to std err
    errlog = logging.StreamHandler()
    errlog.setLevel(logging.DEBUG)
    errlog.setFormatter(formatter)
    log.addHandler(errlog)

    LOGOBJECT = log
    return LOGOBJECT


def run_command(command):
    ''' Run a shell command and get the output and exit code 
        while the output is send to both logging and returned. 
    '''
    output = []
    log = logger()
    process = subprocess.Popen(command.split(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
    return(str(output), exitcode)


def nagios_or_icinga():
    pass


def get_monitoring_pid():
    pass
