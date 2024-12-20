import os

from behave import use_step_matcher
from lib.db import DB as DB
from lib.db_setup import DB_setup
from lib.webdriver_manager import WebdriverManager
from lib.logger import *

use_step_matcher("parse")

## -----DB setup---------
# def before_all(context):
#    setup_db = context.config.userdata.get('setup_db_test_data', 'true')

 #   if setup_db == 'true':
 #       environment = context.config.userdata.get('base_url', 'apple')
 #       param = {'environment': environment}
 #        context.db = DB(param)
 #        db_setup = DB_setup(context)
 #        db_setup.setup_database(context)


def before_scenario(context, scenario):
    context.browser = None
    environment = context.config.userdata.get('base_url', 'apple')
    browser = context.config.userdata.get('browser', 'chrome')
    browsers_list = browser.split(',')
    headless = context.config.userdata.get('headless', 'false').lower() == 'true'
    remote = context.config.userdata.get('remote', 'false').lower() == 'true'
    WebdriverManager.set_driver(browser=browsers_list, headless=headless, remote=remote, context=context)
    WebdriverManager.get_base_url(context=context, base_url=environment)
    feature_name = scenario.feature.name.replace(" ", "_").lower()
    download_directory = os.path.join(os.getcwd(), "downloads", feature_name)
    os.makedirs(download_directory, exist_ok=True)
    context.download_directory = download_directory
    logger.info(f"\n\n\tScenario Name - {scenario.name}\n")
    logger.info(f"\tDownload Directory: {context.download_directory}")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        WebdriverManager.screenshot(context, scenario)

    if hasattr(context, 'browser'):
        context.browser.quit()


def after_step(context, step):
    logger.info(f"\n\t\tStep Name - {step.name}")
    logger.info(f"\t\tStatus - {step.status}")
    logger.info(f"\t\tDuration - {step.duration}s")
    browser_error_list = context.browser.get_log(context.browser.log_types[0])
    driver_error_list = context.browser.get_log(context.browser.log_types[1])
    if step.status == 'Status.failed':
        if len(browser_error_list) > 0:
            for err in browser_error_list:
                logger.info(f"\t\tBrowser Error: {err['message']}")
        if len(driver_error_list) > 0:
            for err in driver_error_list:
                logger.info(f"\t\tDriver Error: {err['message']}")

    WebdriverManager.screenshot(context, step)
