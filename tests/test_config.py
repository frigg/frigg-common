# -*- coding: utf-8 -*-
from frigg.config import config, redis_client


def test_config():
    assert config('HQ_REPORT_URL') == 'http://localhost:8000'


def test_redis_import_fail_silently():
    assert redis_client() is None
