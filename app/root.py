import os

DIR_ROOT=os.path.dirname(os.path.abspath(__file__))
DIR_DATA="{0}{1}data{1}".format(DIR_ROOT, os.sep)
DIR_LOG="{0}{1}logging{1}".format(DIR_ROOT, os.sep)
DIR_DATA_RAW="{0}{1}raw{1}".format(DIR_DATA, os.sep)
DIR_DATA_STAGE="{0}{1}stage{1}".format(DIR_DATA, os.sep)
DIR_DATA_ANALYTICS="{0}{1}analytics{1}".format(DIR_DATA, os.sep)
DIR_DATA_TEST="{0}{1}test{1}".format(DIR_DATA, os.sep)
DIR_DATA_RAW_TEST="{0}{1}raw{1}".format(DIR_DATA_TEST, os.sep)
DIR_DATA_ANALYTICS_TEST="{0}{1}analytics{1}".format(DIR_DATA_TEST, os.sep)
