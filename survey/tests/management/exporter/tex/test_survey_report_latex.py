# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from survey.management.exporter.tex import SurveyReportLatexFile
from survey.tests.management.test_management import TestManagement


class TestSurveyReportLatex(TestManagement):

    def test_mendatory_argument(self):
        """ We get an error when a mandatory argument is not set. """
        temp = settings.TEX_DOCUMENT_CLASS
        del settings.TEX_DOCUMENT_CLASS
        self.assertRaises(ImproperlyConfigured, SurveyReportLatexFile)
        settings.TEX_DOCUMENT_CLASS = temp

    def test_optional_argument(self):
        """ We do not get an error when an optional argument isn't set. """
        temp = settings.TEX_HEADER
        del settings.TEX_HEADER
        self.assertIsNotNone(SurveyReportLatexFile)
        settings.TEX_HEADER = temp
