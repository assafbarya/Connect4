from Env import Env
from ruleAbidingAgent import RuleAbidingAgent
from minMaxAgent import MinMaxAgent
import logging

def main():
    for _x in range(100):
        #agent1 = RuleAbidingAgent()
        agent1 = MinMaxAgent( 1, 1 )
        agent2 = MinMaxAgent( 2, 2 )
        e  = Env( agent1, agent2, logging.INFO )
        e.play()


            















main()