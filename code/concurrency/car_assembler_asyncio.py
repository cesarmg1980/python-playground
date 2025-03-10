"""
This code mimicks a car assembly line using asyncio. 
3 different functions are used to simulate the assembly line:
1. assemble_chassis: simulates the assembly of the car chassis.
2. assemble_body: simulates the assembly of the car body.
3. assemble_interior: simulates the assembly of the car interior.

Each function takes a few seconds to complete and the supervisor function is used to manage the assembly line.
"""

import asyncio
import time

async def assemble_chassis():
    """
    This function simulates the assembly of the car chassis.
    """
    print('Assembling chassis...')
    """
    Uncomment the line below to see the difference between using time.sleep and asyncio.sleep.
    One is going to block the event loop while the other will allow other tasks to run.
    """
    #time.sleep(5) 
    await asyncio.sleep(5)
    print('Chassis assembled')
    return 'Chassis'

async def assemble_body():
    """
    This function simulates the assembly of the car body.
    """
    print('Assembling body...')
    await asyncio.sleep(5)
    print('Body assembled')
    return 'Body'

async def assemble_interior():
    """
    This function simulates the assembly of the car interior.
    """
    print('Assembling interior...')
    await asyncio.sleep(5)
    print('Interior assembled')
    return 'Interior'  

async def supervisor():
    """
    This function manages the assembly line.
    """
    car = await asyncio.gather(assemble_chassis(), assemble_body(), assemble_interior())
    return f"Car assembled with {', '.join(car)}"

def main():
    result = asyncio.run(supervisor())
    print(result)

if __name__ == '__main__':
    main()