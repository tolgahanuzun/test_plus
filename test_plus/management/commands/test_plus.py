import sys
import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test.utils import get_runner
from django.test.runner import DiscoverRunner as _DiscoverRunner

from unittest import TextTestRunner as _TextTestRunner, TextTestResult as _TextTestResult


class TimeLoggingTestResult(_TextTestResult):
    def __init__(self, *args, **kwargs):
        super(TimeLoggingTestResult, self).__init__(*args, **kwargs)
        self.timings = []

    def startTest(self, test):
        self.test_started = time.time()
        super(TimeLoggingTestResult, self).startTest(test)

    def addSuccess(self, test):
        total_time = time.time() - self.test_started
        test_name = self.getDescription(test)
        self.timings.append((test_name, total_time))
        super(TimeLoggingTestResult, self).addSuccess(test)

    def getTestTimings(self):
        return self.timings


class TextTestRunner(_TextTestRunner):
    def run(self, test):
        result = super(TextTestRunner, self).run(test)
        for test_name, total_time in result.getTestTimings():
            self.stream.writeln("({:.10}s) {}".format(format(total_time, 'f'), test_name))
        return result


class DiscoverRunner(_DiscoverRunner):
    test_runner = TextTestRunner
    def get_resultclass(self):
        return TimeLoggingTestResult


class Command(_DiscoverRunner, BaseCommand):
    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
                '--repeat', '-rp',
                help='Runs a specific test n times.'
                )
        parser.add_argument(
                'args', metavar='test_label', nargs='*',
                help='Module paths to test; can be modulename, modulename.TestCase or modulename.TestCase.test_method'
            )

    def handle(self, *test_labels, **options):
        TestRunner = get_runner(settings, 'test_plus.management.commands.test_plus.DiscoverRunner')
        repeat = int(options.get('repeat') or 1)
        failures = False
        for index in range(1, repeat+1):
            test_runner = TestRunner(**options)
            print('\n_______Loop:{}_______'.format(index))
            failures = failures or test_runner.run_tests(test_labels)

        if failures:
            sys.exit(1)
