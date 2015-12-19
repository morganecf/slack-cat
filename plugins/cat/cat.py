import os
import sys
import time
import random
from phue import Bridge, PhueRegistrationException

def setup(ip, lights):
    pass

# Alert a given bulb that cat message has been posted
def glow(bulb, bridge):
    # Save current state
    state = bridge.get_light(bulb).get('state')

    # Make sure light is on
    bridge.set_light(bulb, 'on')

    # Set to max brightness and saturation
    bridge.set_light(bulb, 'bri', 254)
    bridge.set_light(bulb, 'sat', 254)

    # Make purple
    bridge.set_light(bulb, 'xy', [0.26, 0.05])

    return state

def set_state(bulb, state, bridge):
    for k, v in state.iteritems():
        bridge.set_light(bulb, k, v)

#TODO: make sure message is a cat gif
def process_message(data, bridge, bulbs):
    # Only glow if there's a gif
    if 'attachments' not in data:
        return
    print 'Cat message:', data['attachments'][0]['title'], '\n'

    # Make each bulb glow purple
    states = []
    for bulb in bulbs:
        states.append(glow(bulb, bridge))

    # Wait a bit
    time.sleep(30)

    # Revert to original state
    for i, bulb in enumerate(bulbs):
        set_state(bulb, states[i], bridge)

def respond(input):
    pass
