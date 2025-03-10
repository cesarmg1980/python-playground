"""
This code mimicks a car assembly line using threading.
3 different functions are used to simulate the assembly line:
1. assemble_chassis: simulates the assembly of the car chassis.
2. assemble_body: simulates the assembly of the car body.
3. assemble_interior: simulates the assembly of the car interior.
"""
import threading
import time

def assemble_chassis():
    """
    This function simulates the assembly of the car chassis.
    """
    print('Assembling chassis...')
    time.sleep(5)
    print('Chassis assembled')
    return 'Chassis'

def assemble_body():
    """
    This function simulates the assembly of the car body.
    """
    print('Assembling body...')
    time.sleep(5)
    print('Body assembled')
    return 'Body'

def assemble_interior():
    """
    This function simulates the assembly of the car interior.
    """
    print('Assembling interior...')
    time.sleep(5)
    print('Interior assembled')
    return 'Interior'

def supervisor():
    """
    This function manages the assembly line.
    """
    chassis_thread = threading.Thread(target=assemble_chassis)
    body_thread = threading.Thread(target=assemble_body)
    interior_thread = threading.Thread(target=assemble_interior)

    """
    Uncomment these lines below to see the difference between 
    starting and joining alternatively or starting all threads 
    at once and joining them at the end.
    """
    # chassis_thread.start()
    # chassis_thread.join()
    # body_thread.start()
    # body_thread.join()
    # interior_thread.start()
    # interior_thread.join()

    chassis_thread.start()
    body_thread.start()
    interior_thread.start()

    chassis_thread.join()
    body_thread.join()
    interior_thread.join()

    return "Car assembled."

def main():
    result = supervisor()
    print(result)

if __name__ == '__main__':
    main()