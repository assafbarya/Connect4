from Env import Env
from ruleAbidingAgent import RuleAbidingAgent
from minMaxAgent import MinMaxAgent
from humanAgent import HumanAgent
from rlAgent import RLAgent
from softMaxSelector import SoftMaxSelector
import logging


def main():
    for _x in range(10):
        #agent1 = RuleAbidingAgent()
        #agent1 = MinMaxAgent( 1, 1 )
        agent1 = RLAgent( SoftMaxSelector() )
        agent2 = MinMaxAgent( 2, 1 )
        e  = Env( agent1, agent2, logging.DEBUG )
        e.play()


            















main()