from Env import Env
from ruleAbidingAgent import RuleAbidingAgent
from minMaxAgent import MinMaxAgent
from humanAgent import HumanAgent
import logging

def main():
    for _x in range(10):
        #agent1 = RuleAbidingAgent()
        #agent1 = MinMaxAgent( 1, 1 )
        agent1 = HumanAgent()
        agent2 = MinMaxAgent( 2, 4 )
        e  = Env( agent1, agent2, logging.INFO )
        e.play()


            















main()