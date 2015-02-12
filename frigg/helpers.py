# -*- coding: utf8 -*-
import logging
import subprocess

logger = logging.getLogger(__name__)


def detect_test_runners(files):
    if 'Makefile' in files:
        return ['make test']
    if 'tox.ini' in files:
        return ['tox', 'flake8']
    if 'setup.py' in files:
        return ['python setup.py test', 'flake8']
    if 'manage.py' in files:
        return ['python manage.py test', 'flake8']
    if 'package.json' in files:
        return ['npm install', 'npm test']
    if 'build.sbt' in files:
        return ['sbt test']
    if 'Cargo.toml' in files:
        return ['cargo test']
    if '_config.yml' in files:
        return ['jekyll build']
    return []


class ProcessResult(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def local_run(command, directory=None):
    command = '{} 2>&1'.format(command)
    if directory:
        command = 'cd {} && {}'.format(directory, command)

    logger.debug('Running command: {}'.format(command))
    result = ProcessResult(command=command)
    print(command)

    process = subprocess.Popen(
        ['/bin/bash', '-i', '-c'] + command.split(' '),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True
    )

    (stdout, stderr) = process.communicate()
    result.out = stdout.decode('utf-8').strip() if stdout else ''
    result.err = stderr.decode('utf-8').strip() if stderr else ''
    result.return_code = process.returncode
    result.succeeded = result.return_code == 0
    logger.debug('Result: {}'.format(result.__dict__))
    return result


class CachedProperty(object):
    def __init__(self, func, name=None):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name = name or func.__name__

    def __get__(self, instance, type=None):
        if instance is None:
            return self
        res = instance.__dict__[self.name] = self.func(instance)
        return res


cached_property = CachedProperty
