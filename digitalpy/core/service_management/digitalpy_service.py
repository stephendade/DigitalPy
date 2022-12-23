#######################################################
# 
# DigitalPyService.py
# Python implementation of the Class DigitalPyService
# Generated by Enterprise Architect
# Created on:      02-Dec-2022 5:39:44 PM
# Original author: Giu Platania
# 
#######################################################
from digitalpy.core.zmanager.service import Service
from digitalpy.core.zmanager.impl.zmq_subscriber import ZmqSubscriber
from digitalpy.core.zmanager.impl.zeroless_pusher import ZerolessPusher

class DigitalPyService(Service, ZmqSubscriber, ZerolessPusher):
    # on the reception of messages from the subscriber interface or the socket
    #TODO: what is the service manager supposed to do? is this going to be a new service
    
    def __init__(self, service_id: str, subject_address: str, subject_port: int, integration_manager_address: str, integration_manager_port: int):
        self.subject_address = subject_address
        self.subject_port = subject_port
        self.integration_manager_address = integration_manager_address
        self.integration_port_address = integration_manager_port
        self.service_id = service_id

    def discovery(self):
        """used to  inform the discoverer of the specifics of this service"""
        # TODO: the contract for discovery needs to be established
        # example for potential implementation
        return "service desc"

    def send_heart_beat(self):
        """used to inform the service menager that this service is still alive"""
        # TODO: once the service manager has been well defined then we will need
        # to define the format for this service.

    def initialize_connections(self):
        self.subject_bind(self.subject_address, self.subject_port)
        self.broker_connect(self.integration_port_address, self.integration_manager_address,self.service_id)