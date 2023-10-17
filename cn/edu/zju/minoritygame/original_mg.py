import matplotlib.pyplot as plt
import math

import networkx as nx
import numpy as np
#import pandas as pd
from random import *
import time
import logging
#from scipy.stats import pearsonr

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 定义handler的输出格式
# logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)

def main():

    N=1001  # number of agents
    T=1000
    M = 6   # length of memory
    num_memory  =2<<(M-1)
    S = 5  # bag volume of strategies
    num_total_strategies = 2<< (num_memory-1)
    #num_total_strategies = math.pow(2,math.pow(2,M))
    lt_agent_stragies_score={}
    total_action_for_one = 0
    syst_action_memory=""
    syst_last_action={}
    agent_action=[]
    dict_map_strategies = {}
    print('memory -> total strategies %d / %d ' % (num_memory, num_total_strategies))

    #logger.info("initializing strategy mapping ...")
    '''
    for s in range(0,num_total_strategies):
        dict_map_strategies[s]={}
        # transform the strategies to binary and mapping to memories
        # e.g. strategy "1" mapped to 00000001 for M =3
        tmp_b =  ('{0:0%db}' % num_memory).format(s)
        #print(tmp_b)
        for m in range(num_memory):
            dict_map_strategies[s][m] =int(tmp_b[m])
        #print(tmp_b,dict_map_strategies[s])
    #    if s ==3 :
        #exit(0)
    '''
    x=[]
    y=[]
    logger.info("initializing system and agents' strategy...")
    time_start = time.time()
    #initialization
    num_action_one = 0
    for i in range(N):
        action =randint(0,1)
        if(action==1):
            num_action_one+=1
        agent_action.append(action)
        tmp_lst_strategies = []
        if(syst_last_action.get(agent_action[i])==None):
            syst_last_action[action] =0
        else:
            syst_last_action[action]=syst_last_action[action]+1

        for s in range(S):
            tmp = randint(0, num_total_strategies-1)

            if(dict_map_strategies.get(tmp)==None):
                dict_map_strategies[tmp]={}
                tmp_b = ('{0:0%db}' % num_memory).format(tmp)
                # print(tmp_b)
                for m in range(num_memory):
                    dict_map_strategies[tmp][m] = int(tmp_b[m])

            while (tmp in tmp_lst_strategies):
                tmp = randint(0, num_total_strategies-1)
            tmp_lst_strategies.append(tmp)
            if(lt_agent_stragies_score.get(i)== None):
                lt_agent_stragies_score[i] = {}
            lt_agent_stragies_score[i][tmp] = 0  #the score of each strategy for every agent is zero
    #    logger.info("agent %d, strategty:%s", i,lt_agent_stragies[i])
    logger.info("actual stragegies:%d",len(dict_map_strategies))
    minority_action = 1 if syst_last_action[0] >syst_last_action[1] else 0

    logger.info("initializing system memory action...")
    for m in range(M-1):
    #    syst_action_memory.append(randint(0,1))
        syst_action_memory +=  str(randint(0,1))
    syst_action_memory += str(minority_action)

    #print(syst_action_memory,int(syst_action_memory,2))

    logger.info("Game starting...")
    #run for minority game
    for t in range(T):
        if t %1000 ==0:
            time_end = time.time()
            logger.info("%d/%d,time cost: %d s",t,T,time_end - time_start)
        tmp_syst_memory = int(syst_action_memory,2)  #convert syst. memory from binary to decem
        tmp_syst_last_action = int(syst_action_memory[-1],2)
        #print(tmp_syst_last_action)
        syst_last_action={}
        num_action_one=0
        for i in range(N):
            tmp_agent_strategy_max_score = 0
            best_strategies = []
            round_best_strategy=-1

            if(agent_action[i] == tmp_syst_last_action): # predict correctly the right minority side
                for s in lt_agent_stragies_score[i].keys():
                    #if s ==num_total_strategies:
                    #    print(s)
                    if dict_map_strategies[s][tmp_syst_memory]==tmp_syst_last_action:
                        lt_agent_stragies_score[i][s]= lt_agent_stragies_score[i][s] + 1 # reward a viewpoint to the right strategy
            # make a new prediction
            for s in lt_agent_stragies_score[i].keys():
                if tmp_agent_strategy_max_score <= lt_agent_stragies_score[i][s]:
                    tmp_agent_strategy_max_score = lt_agent_stragies_score[i][s]
            for s in lt_agent_stragies_score[i].keys():
                if lt_agent_stragies_score[i][s] == tmp_agent_strategy_max_score:
                    best_strategies.append(s)
    #        a = randint(0,len(best_strategies)-1)
    #        print(a)
            round_best_strategy= best_strategies[randint(0,len(best_strategies)-1)]

            agent_action[i] = dict_map_strategies[round_best_strategy][tmp_syst_memory]
            if (syst_last_action.get(agent_action[i]) == None):
                syst_last_action[agent_action[i]] = 0
            else:
                syst_last_action[agent_action[i]] = syst_last_action[agent_action[i]] + 1

            if (agent_action[i] == 1):
                num_action_one += 1

        y.append(num_action_one)
        x.append(t + 1)
        minority_action = 1 if syst_last_action[0] > syst_last_action[1] else 0
        syst_action_memory = syst_action_memory[-1*(M-1):] + str(minority_action)
        #print(syst_action_memory)

    plt.plot(x, y)
    #plt.savefig("a.png")
    plt.show()
    '''
    plt.semilogx(x,y)
    plt.xlabel('$ \\beta $')
    plt.ylabel('correlation')
    '''

    logger.info("writing results to file..")
    time_end = time.time()
    logger.info('The end,cost time:%d s', time_end - time_start)


if __name__ == '__main__':
    main()