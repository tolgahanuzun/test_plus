import sys
import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.utils import get_command_line_option
from django.test.utils import get_runner
from django.test.runner import DiscoverRunner as _DiscoverRunner

from unittest import TextTestRunner as _TextTestRunner, TextTestResult as _TextTestResult


class TimeLoggingTestResult(_TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timings = []

    def startTest(self, test):
        self.test_started = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        total_time = time.time() - self.test_started
        test_name = self.getDescription(test)
        self.timings.append((test_name, total_time))
        super().addSuccess(test)

    def getTestTimings(self):
        return self.timings


class TextTestRunner(_TextTestRunner):
    def run(self, test):
        result = super().run(test)
        for test_name, total_time in result.getTestTimings():
            self.stream.writeln("({:.10}s) {}".format(format(total_time, 'f'), test_name))
        return result


class DiscoverRunner(_DiscoverRunner):
    test_runner = TextTestRunner
    def get_resultclass(self):
        return TimeLoggingTestResult


class Command(BaseCommand):
    def handle(self, *test_labels, **options):
        TestRunner = get_runner(settings, 'test_plus.management.commands.test_plus.DiscoverRunner')

        test_runner = TestRunner(**options)
        failures = test_runner.run_tests(test_labels)
        if failures:
            sys.exit(1)
