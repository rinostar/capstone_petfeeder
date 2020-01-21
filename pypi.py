import RPi.GPIO as GPIO
from time import sleep
import time
import os
from dotenv import load_dotenv
import asyncio
import threading
import datetime
from six.moves import input
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import MethodResponse

load_dotenv()
DEVICE_CONNECTION_STRING = os.getenv('DEVICE_CONNECTION_STRING')

def turn_motor():
    in1 = 24
    in2 = 23
    en = 25
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p.start(75)
    GPIO.output(in2,GPIO.HIGH)
    sleep(1)
    GPIO.output(in2,GPIO.LOW)
    GPIO.cleanup()

async def main():
    # 1. Setup connectuon between local device "PyPi" to IoT Hub "FoodieBear"
    device_client_PyPi = IoTHubDeviceClient.create_from_connection_string(DEVICE_CONNECTION_STRING)
    await device_client_PyPi.connect()

    # 2. Define behavior for handling method (success)
    async def success_request_listener(device_client_PyPi):
        while True:
            # 1). wait for feed method call
            method_request = await device_client_PyPi.receive_method_request(
                "feed"
            )
            # 2). perform method feed
            turn_motor()
            print("executed method feed")
            # 3). set response payload
            responseMsg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payload = {"result": True, "data": responseMsg}
            # 4). set return status code
            status = 200
            # 5). send response
            method_response = MethodResponse.create_from_method_request(
                method_request, status, payload
            )
            await device_client_PyPi.send_method_response(method_response)
        
    # 3. Define behavior for handling method (failure)
    async def failure_request_listener(device_client_PyPi):
        while True:
            # 1). wait for unknown method call
            method_request = (
                await device_client_PyPi.receive_method_request()
            )
            print("executed unknown method: " + method_request.name)
            # 2). set response payload & return status code
            payload = {"result": False, "data": "unknown method"}
            status = 400
            # 3). send response
            method_response = MethodResponse.create_from_method_request(
                method_request, status, payload
            )
            await device_client_PyPi.send_method_response(method_response)
        
    # 4. Define behavior for halting the application
    def stdin_listener():
        while True:
            selection = input("Press Q to quit\n")
            if selection == "Q" or selection == "q":
                print("Quitting...")
                break
        
    # 5. Schedule tasks for Method Listener
    listeners = asyncio.gather(
        failure_request_listener(device_client_PyPi),
        success_request_listener(device_client_PyPi)
    )

    # 6. Run the stdin listener in the event loop
    loop = asyncio.get_running_loop()
    user_finished = loop.run_in_executor(None, stdin_listener)
    
    # 7. Wait for user to indicate they are done listening for method calls
    await user_finished

    # 8. Cancel listening
    listeners.cancel()

    # 9. Disconnect local device "PyPi" from IoT Hub "FoodieBear"
    await device_client_PyPi.disconnect()

if __name__ == '__main__':
	print('PyPi running...')
	asyncio.run(main())
	print('Pypi stopped.')
