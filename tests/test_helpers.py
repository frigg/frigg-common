# -*- coding: utf8 -*-
from datetime import datetime
from time import sleep

from frigg.helpers import cached_property, detect_test_runners, local_run


def test_detect_test_runners():
    assert(detect_test_runners([]) == [])
    assert(detect_test_runners(['random file']) == [])
    files = ['_config.yml', 'Cargo.toml', 'build.sbt', 'package.json', 'manage.py', 'setup.py',
             'tox.ini', 'Makefile']
    assert(detect_test_runners(files) == ['make test'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['tox', 'flake8'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['python setup.py test', 'flake8'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['python manage.py test', 'flake8'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['npm install', 'npm test'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['sbt test'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['cargo test'])
    del files[len(files) - 1]
    assert(detect_test_runners(files) == ['jekyll build'])


def test_local():
    result = local_run('ls')
    assert result.succeeded is True
    assert result.return_code == 0


def test_cached_property():
    class A(object):
        @cached_property
        def func(self):
            return datetime.now().microsecond

    a = A()
    first = a.func
    sleep(0.1)
    last = a.func
    assert(first == last)
