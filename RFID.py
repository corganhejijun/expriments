import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc522

reader = rc522()
LED_number = 7
READ = 0
WRITE = 1
operation = READ

GPIO.setup(LED_number, GPIO.OUT)
while True:
    try:
        if operation == READ:
            print("begin reading ")
            id, data = reader.read()
            data = data.strip()
            print("id is " + str(id))
            print("data is " + str(data))
            try:
                value = float(data)
                if value > 100:
                    GPIO.output(LED_number, GPIO.HIGH)
                else:
                    GPIO.output(LED_number, GPIO.LOW)
                print('input data is ' + str(value))
            except Exception as error:
                print('input data "' + data + '" is not digit only')
                print("error: " + str(error))
        if operation == WRITE:
            data = raw_input("input data:")
            print("input data is: " + data)
            print("place your card to write")
            reader.write(data)
            print("write success")
    except Exception as error:
        print("error happened: " + str(error))
    finally:
        a = raw_input("what do you want? f: finish; w: write; other key: read.")
        if a == 'f':
            print("yes finish")
            break
        elif a == 'w':
            print("begin writing")
            operation = WRITE
        else:
            operation = READ

GPIO.output(LED_number, GPIO.LOW)
GPIO.cleanup()
