# -*- coding: utf-8 -*-
import logging
import os

import yaml

logger = logging.getLogger(__name__)

PATHS = [
    '/etc/frigg/config.yaml',
    '/etc/frigg/config.yml',
    os.path.expanduser('~/.frigg/config.yaml'),
    os.path.expanduser('~/.frigg/worker.yml'),
]


def config(key):
    settings = yaml.load(open(os.path.join(os.path.dirname(__file__), 'defaults.yml')))
    for path in PATHS:
        try:
            settings.update(yaml.load(open(path)))
        except IOError:
            pass
    return settings.get(key, None)


def redis_client():
    try:
        import redis
        return redis.Redis(
            host=config('REDIS')['host'],
            port=config('REDIS')['port'],
            db=config('REDIS')['db'],
            password=config('REDIS')['password']
        )
    except ImportError:
        logger.warning('You need to install the redis python package in order to'
                       ' use functionality that relies on redis.')


try:
    from raven import Client
    sentry = Client(config('SENTRY_DSN'))  # noqa
except ImportError:
    logger.debug('Raven is not installed.')
    sentry = None
