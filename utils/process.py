import logging
import shlex
import subprocess

log = logging.getLogger("process")


def execute(command, callback=None):
    total_output = ''
    process = subprocess.Popen(shlex.split(command), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = str(process.stdout.readline()).lstrip('b').replace('\\n', '')
        if process.poll() is not None:
            break
        if output and len(output) > 6:
            log.debug(output)
            if callback:
                callback(output)
            else:
                total_output += "%s\n" % output

    if not callback:
        return total_output
    rc = process.poll()
    return rc
