from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.link import TCLink
from mininet.topo import Topo


class MyTopo( Topo ):
    "Tree topology"

    def build( self ):
        "15 host dan 15 switch tree topology"

        # Add hosts 
        h1 = self.addHost( 'h1', ip='10.10.10.1' )
        h2 = self.addHost( 'h2', ip='10.10.10.2' )
        h3 = self.addHost( 'h3', ip='10.10.10.3' )
        h4 = self.addHost( 'h4', ip='10.10.10.4' )
        h5 = self.addHost( 'h5', ip='10.10.10.5' )
        h6 = self.addHost( 'h6', ip='10.10.10.6' )
        h7 = self.addHost( 'h7', ip='10.10.10.7' )
        h8 = self.addHost( 'h8', ip='10.10.10.8' )
        h9 = self.addHost( 'h9', ip='10.10.10.9' )
        h10 = self.addHost( 'h10', ip='10.10.10.10' )
        h11 = self.addHost( 'h11', ip='10.10.10.11' )
        h12 = self.addHost( 'h12', ip='10.10.10.12' )
        h13 = self.addHost( 'h13', ip='10.10.10.13' )
        h14 = self.addHost( 'h14', ip='10.10.10.14' )
        h15 = self.addHost( 'h15', ip='10.10.10.15' )

        # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )
        s9 = self.addSwitch( 's9' )
        s10 = self.addSwitch( 's10' )
        s11 = self.addSwitch( 's11' )
        s12 = self.addSwitch( 's12' )
        s13 = self.addSwitch( 's13' )
        s14 = self.addSwitch( 's14' )
        s15 = self.addSwitch( 's15' )

        # Add links to create a tree structure
        self.addLink( h1, s1 )
        self.addLink( h2, s2 )
        self.addLink( h3, s3 )
        self.addLink( h4, s4 )
        self.addLink( h5, s5 )
        self.addLink( h6, s6 )
        self.addLink( h7, s7 )
        self.addLink( h8, s8 )
        self.addLink( h9, s9 )
        self.addLink( h10, s10 )
        self.addLink( h11, s11 )
        self.addLink( h12, s12 )
        self.addLink( h13, s13 )
        self.addLink( h14, s14 )
        self.addLink( h15, s15 )

        self.addLink( s1, s2 )
        self.addLink( s1, s3 )
        self.addLink( s2, s4 )
        self.addLink( s2, s5 )
        self.addLink( s3, s6 )
        self.addLink( s3, s7 )
        self.addLink( s4, s8 )
        self.addLink( s4, s9 )
        self.addLink( s5, s10 )
        self.addLink( s5, s11 )
        self.addLink( s6, s12 )
        self.addLink( s6, s13 )
        self.addLink( s7, s14 )
        self.addLink( s7, s15 )

topos = { 'initopo': ( lambda: MyTopo() ) }
locations = {
    'c0': (600, 50),
    's1': (400, 150),
    's2': (200, 300),
    's3': (600, 300),
    's4': (100, 450),
    's5': (300, 450),
    's6': (500, 450),
    's7': (700, 450),
    's8': (50, 600),
    's9': (150, 600),
    's10': (250, 600),
    's11': (350, 600),
    's12': (450, 600),
    's13': (550, 600),
    's14': (650, 600),
    's15': (750, 600),
    'h1': (400, 100),
    'h2': (200, 250),
    'h3': (600, 250),
    'h4': (100, 400),
    'h5': (300, 400),
    'h6': (500, 400),
    'h7': (700, 400),
    'h8': (50, 550),
    'h9': (150, 550),
    'h10': (250, 550),
    'h11': (350, 550),
    'h12': (450, 550),
    'h13': (550, 550),
    'h14': (650, 550),
    'h15': (750, 550)
}

