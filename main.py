from agent import *
import argparse
import logging


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--goalie', action = 'store_true')
    parser.add_argument('--debug', action = 'store_true')
    options = parser.parse_args()

    if options.debug:
        logging.basicConfig(format = '%(levelname)s:%(message)s',
                            level = logging.DEBUG)

    agent = None
    if options.goalie:
        # create a goalie
    else:
        agent = Agent('will')
    agent.connect()
    agent.run()
