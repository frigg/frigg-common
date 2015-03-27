# -*- coding: utf8 -*-
import os
from unittest import TestCase, skip

import mock

from frigg.projects import build_settings, get_path_of_settings_file


class BuildSettingsTestCase(TestCase):

    @mock.patch('frigg.projects.build_tasks')
    def test_build_settings_no_settings_file(self, mock_build_tasks):
        self.assertRaises(RuntimeError, build_settings, '/')
        self.assertTrue(mock_build_tasks.called)

    def test_build_settings(self):
        settings = build_settings(os.getcwd())
        self.assertEqual(settings['webhooks'], [])
        self.assertEqual(settings['tasks'], ['tox -e py34', 'tox -e py27', 'flake8',
                                             'isort -c -rc frigg tests',
                                             'coverage combine', 'coverage report --fail-under=80',
                                             'coverage xml'])

    @skip('Mock not working')
    @mock.patch('os.path.exists', lambda path: 'yaml' in path)
    def test_get_path_of_settings_file_yaml(self):
        self.assertEqual(get_path_of_settings_file('/'), '/.frigg.yaml')

    @skip('Mock not working')
    @mock.patch('os.path.exists', lambda path: 'yml' in path)
    def test_get_path_of_settings_file_yml(self):
        self.assertEqual(get_path_of_settings_file('/'), '/.frigg.yml')
