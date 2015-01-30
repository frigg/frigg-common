# -*- coding: utf8 -*-
import logging

import requests

from frigg.config import config

logger = logging.getLogger(__name__)


def report_run(build_id, build):
    response = requests.post(
        config('HQ_REPORT_URL'),
        data=build,
        headers={
            'content-type': 'application/json',
            'FRIGG_WORKER_TOKEN': config('TOKEN')
        }
    )
    logger.info('Reported build to hq, hq response status-code: %s, data:\n%s' % (
        response.status_code,
        build
    ))
    if response.status_code != 200:
        with open('build-%s-hq-response.html' % build_id, 'w') as f:
            f.write(response.text)
    return response
