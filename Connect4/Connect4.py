from Env import Env
from ruleAbidingAgent import RuleAbidingAgent
import logging

def main():
    agent1 = RuleAbidingAgent()
    agent2 = RuleAbidingAgent()
    e  = Env( agent1, agent2, logging.DEBUG )
    e.play()


            















main()