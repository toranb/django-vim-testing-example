from icc11codecamp.settings.base_settings import *

TEMPLATE_DEBUG = DEBUG = True

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
