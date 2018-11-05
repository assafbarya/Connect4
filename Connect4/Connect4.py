from Env import Env
from ruleAbidingAgent import RuleAbidingAgent
from minMaxAgent import MinMaxAgent
from humanAgent import HumanAgent
#from rlAgent import RLAgent
from historianAgent import HistorianAgent
from softMaxSelector import SoftMaxSelector
from epsGreedySelector import EpsGreedySelector
import logging


def main():
    filename = 'c:\\work\\modelWeights.h5'
    #for _x in range(30):
    #    #agent1 = RuleAbidingAgent()
    #    #agent1 = MinMaxAgent( 1, 1 )
    #    agent1 = RLAgent( SoftMaxSelector() )
    #    agent2 = MinMaxAgent( 2, 1 )
    #    e  = Env( agent1, agent2, logging.INFO )
    #    e.play()
    agent1 = MinMaxAgent( 1, 1 )
    #agent1 = RLAgent( EpsGreedySelector() )
    #agent2 = RLAgent( EpsGreedySelector(), filename )
    #agent2 = RLAgent( EpsGreedySelector() )
    agent2 = HistorianAgent()
    e  = Env( agent1, agent2, logging.ERROR )
    e.playGames( 1000000 )

    


            















main()