"""
GreenGrass Lambda Bluetooth Gateway
"""
__author__  = "Dai Ikeda <dai@d-line.net>"
__version__ = "0.01"
__date__    = "17 Oct 2020"

import logging
import platform
import sys
from threading import Timer
from bluepy import btle
import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from the Lambda function - Greengrass_HelloWorld_QzADm
my_platform = platform.platform()

# When deployed to a Greengrass core, this code will be executed immediately
# as a long-lived lambda function.  The code will enter the infinite while
# loop below.
# If you execute a 'test' on the Lambda Console, this test will fail by
# hitting the execution timeout of three seconds.  This is expected as
# this function never returns a result.

scanner = btle.Scanner(0)

def greengrass_bl_gw_run():
    try:
        if not my_platform:
            logger.error("This function works only with Greengrass.")
            return 1
        else:
            client.publish(
                topic="hello/world",
                queueFullPolicy="AllOrException",
                payload="Hello world! Sent from " "the Lambda function - Greengrass_HelloWorld_QzADm running on platform: {}".format(my_platform),
            )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))

    # Asynchronously schedule this function to be run again in 5 seconds
    Timer(5, greengrass_bl_gw_run).start()


# Start executing the function above
greengrass_bl_gw_run()


# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    return