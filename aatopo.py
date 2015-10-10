from mininet.topo import Topo

class MyTopo(Topo):
    ""
    def __init__(self, nAggr=2, nAccess=2, nHost=2, **opts):
        """ nAggr= number of aggregation switch,
            nAccess = number of access switch per aggregation switch
            nHost= no of host per access switch
        """    
        
        Topo.init(self, **opts)
        aggreSwitchList = []
        accessSwitchList = []

        for i in irange(1,nAggr):
            aggrSwitch = self.addSwitch('s%s' %i)

            for j in irange(1,nAccess):
                accessSwitch = self.addSwitch('s%js%i' %j %i)
                self.addLink(accessSwitch, aggrSwitch)
                for k in irange(1, nHost):
                    host = self.addHost('h%ks%js%i' %k %j %i)
                    self.addLink(host, accessSwitch)
                for previousAccessSwitch in accessSwitchList:
                    self.addLink(previousAccessSwitch, accessSwitch)
                accessSwitchList.append(accesSwitch)

            for previousAggrSwitch in aggrSwitchList:
                self.addList(previousAggrSwitch, aggrSwitch)
            aggrSwitchList.append(aggrSwitch)
        
    

topos = {'aatopo':(lambda:MyTopo())}
