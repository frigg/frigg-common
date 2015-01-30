# -*- coding: utf-8 -*-
import os

import responses

from frigg import Build
from frigg.config import config


@responses.activate
def test_report_api_success():
    project = Build(1, {})
    responses.add(responses.POST, config('HQ_REPORT_URL'), body='success')
    assert project.report_run() == 200


@responses.activate
def test_report_api_failure():
    project = Build(1, {})
    responses.add(responses.POST, config('HQ_REPORT_URL'), body='failure', status=400)
    assert project.report_run() == 400
    error_file_path = os.path.join(os.getcwd(), 'build-1-hq-response.html')
    os.path.exists(error_file_path)
    os.remove(error_file_path)
