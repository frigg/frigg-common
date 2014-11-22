# -*- coding: utf8 -*-


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
