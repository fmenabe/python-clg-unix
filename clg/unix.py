# coding: utf-8

import re
import sys
import inspect
import clg.logger as logger

def execute(msg, cmd, quit=True, show_warnings=True, event_hdl=logger):
    logger.info(msg)
    func_code = re.sub('\n\s*', ' ', inspect.getsource(cmd).strip())
    logger.debug(func_code)
    status, stdout, stderr = cmd()
    logger.verbose('\nstatus: {:b}\nstdout: {:s}\nstderr: {:s}'
                    .format(status, stdout.strip(), stderr.strip()))
    if not status:
        event_hdl.error('{:s} failed: {:s}'.format(msg, stdout + stderr), quit=quit)
    elif show_warnings and stderr:
        event_hdl.warn(stderr)
    return stdout

def catch(msg, cmd, exceptions, quit=True):
    logger.info(msg)
    try:
        return cmd()
    except exceptions as err:
        event_hdl.error('{:s} failed: {:s}'.format(msg, err), quit=quit)

def edit(msg, host, filepath, content, mode='w', quit=True, event_hdl=logger):
    logger.info(msg)
    try:
        with host.open(filepath, mode) as fhandler:
            fhandler.write(content)
    except IOError as err:
        event_hdl.error('{:s} failed: {:s}'.format(msg, err), quit=True)
