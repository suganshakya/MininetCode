#! /usr/bin/python

#usage: mn --custom <path-to-file> --topo aatopo,m,n,k ....

from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo(Topo):
    ""
    def __init__(self, nAggr=2, nAccess=2, nHost=2, **opts):
        """ nAggr= number of aggregation switch,
            nAccess = number of access switch per aggregation switch
            nHost= no of host per access switch
        """    
   
        Topo.__init__(self, **opts)
        aggrSwitchList = []
        accessSwitchList = []

        for i in range(1, (nAggr+1)):
            aggrSwitch = self.addSwitch('g%d' % i)
	        lastAccessSwitch= None
            
	        for j in range(1, (nAccess+1)):
    	        
                accessSwitch = self.addSwitch('s%dg%d' % (j,i))
                self.addLink(accessSwitch, aggrSwitch)
                for k in range(1, (nHost+1)):
                    host = self.addHost('h%ds%dg%d' % (k, j, i))
                    self.addLink(host, accessSwitch)

		        if lastAccessSwitch:
			        self.addLink(lastAccessSwitch,accessSwitch)
		        lastAccessSwitch = accessSwitch

            for previousAggrSwitch in aggrSwitchList:
                self.addLink(previousAggrSwitch, aggrSwitch)
            aggrSwitchList.append(aggrSwitch)
        
    

topos = {'aatopo': MyTopo}
