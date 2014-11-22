# -*- coding: utf8 -*-
from frigg.helpers import detect_test_runners


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
