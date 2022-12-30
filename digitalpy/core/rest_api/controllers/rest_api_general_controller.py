#######################################################
# 
# core_name_general_controller.py
# Python implementation of the Class CoreNameGeneralController
# Generated by Enterprise Architect
# Created on:      16-Dec-2022 10:56:05 AM
# Original author: Giu Platania
# 
#######################################################
from Catalog.Implementation.Libraries.Digitalpy.digitalpy.Async.routing.controller import Controller

class RESTAPIGeneralController(Controller):
# default constructor  def __init__(self):  

    def __init__(Request, Response, ActionMapper, Configuration):
        pass

    def execute( = None):
        pass

    def serialize_rest_api():
        """this is the general method used to serialize the component to a given format
        """
        pass
        
	def web_ui_manage_presence():
		"""Using this function, the user can create a custom team member (friendly Dot) on the ATAK map, who will however appear like a real TAK user."""
    	pass
    	
	def api_sensorpostspi():
		"""Creates an SPI at a point or update an existing SPI. If the video source is a UAV, and the UAV is also publishing its own position and sensor point of interest (SPI), those will be plotted on the map. Being able to see the position of the aircraft and know where on the map the camera is looking in real time, while being able to see the video on the same screen, is a huge boost to SA."""
    	pass
    	
	def api_sensor():
		""" manage sensors (name to be changed in ManageSensor)"""
    	pass
    	
	def api_exchecktable():
		"""access data regarding ExCheck items such as checklists and templates
		"""
    	pass
    	
	def api_excheck_table():
		"""access data regarding ExCheck items such as checklists and templates"""
    	pass
    	
	def api_managechat():
		""""""
    	pass
    	
	def api_apiuser():
		""" event used to access list of connected client aswell as data relating to each client."""
    	pass
    	
	def api_missiontable():
		"""access data regarding mission packages"""
    	pass
    	
	def fth__telegram_integration():
		""" provides integration with the messaging system"""
    	pass
    	
	def api_systemuserpostsystemuser():
		""" used to create a new system user on the server"""
    	pass
    	
	def api_managegeoobjectgetgeoobject():
		""" retrieve in a array all geoObjects in a given radius. It uses JSON variables, not the json body"""
    	pass
    	
	def api_managegeoobject():
		""""""
    	pass
    	
	def api_events():
		"""event used to retrieve last 5 events"""
    	pass
    	
	def api_system_health():
		"""event used to retrieve information regarding the status of the server hardware including cpu, disk and memory usage."""
    	pass
    	
	def web_ui__send_message():
		"""This function allows users to send system messages to all connected TAK clients"""
    	pass
    	
	def api_generateqr():
		""""""
    	pass
    	
	def fth__telegram_integration__datapackage():
		"""send a telegram shared file to the server"""
    	pass
    	
	def api_managegeoobjectputgeoobject():
		""" Update a GeoObject  an element place on a map. It has a name, characteristics, and an attitude."""
    	pass
    	
	def api_mapvid():
		"""TBD"""
    	pass
    	
	def api_authenticateuser():
		"""event used to authenticate new clients in the websocket"""
    	pass
    	
	def api_managekmlpostkml():
		""" allows to post a set of geo information with attached metadata in tabular format"""
    	pass
    	
	def api_manageroutepostroute():
		""" creates a route on the map"""
    	pass
    	
	def api_manageroute():
		"""manage routes on the map"""
    	pass
    	
	def fth__video_server():
		"""provides integration with the Video system"""
    	pass
    	
	def api_clients():
		""""""
    	pass
    	
	def api_manageemergencygetemergency():
		""""""
    	pass
    	
	def api_managepresenceputpresence():
		"""Update a team member position"""
    	pass
    	
	def api_managesystemuserputsystemuser():
		""""""
    	pass
    	
	def web_ui__send_cot():
		"""Can be used to create a CoT (also called a geoObject)"""
    	pass
    	
	def api_sendgeochat():
		"""send a message to all the connected clients"""
    	pass
    	
	def api_sensorpostdrone():
		""" create a drone object with a field of view, a current aiming point a video stream"""
    	pass
    	
	def api_managechatpostchattoall():
		""""""
    	pass
    	
	def api_managevideostream():
		"""Manages creation of videos endpoints in the clients. The videos are visible under 'Video Player""""
    	pass
    	
	def api_managenotificationgetnotification():
		""""""
    	pass
    	
	def api_url():
		"""TBD"""
    	pass
    	
	def api_managevideostreampostvideostream():
		""" creates the video stream"""
    	pass
    	
	def api_manageemergencypostemergency():
		""""""
    	pass
    	
	def api_addsystemuser():
		"""add one or many system users to the server"""
    	pass
    	
	def api_datapackagetable():
		""" access data regarding DataPackages"""
    	pass
    	
	def api_managegeoobjectpostgeoobject():
		"""create a GeoObject  an element place on a map. It has a name, characteristics, and an attitude."""
    	pass
    	
	def api_managecotgetzonecot():
		""""""
    	pass
    	
	def api_managevideostreamgetvideostream():
		"""retrieves list of stream paths"""
    	pass
    	
	def fth__kml_forms():
		"""example integration for a Salute report"""
    	pass
    	
	def api_manageemergency():
		""""""
    	pass
    	
	def fth__telegram_integration__chat_to_all():
		"""send a telegram group chat to all connected clients"""
    	pass
    	
	def api_recentcot():
		"""TBD"""
    	pass
    	
	def api_broadcastdatapackage():
		""""""
    	pass
    	
	def api_systemuserdeletesystemuser():
		"""used to remove a system user and their associated files from the server"""
    	pass
    	
	def _api_logs():
		"""event used to retrieve recent error log entries from the server"""
    	pass
    	
	def api_managepresencepostpresence():
		"""create a team member position"""
    	pass
    	
	def api_serviceinfo():
		""" event used to retrieve information about all services including their current status and port"""
    	pass
    	
	def api_manageemergencydeleteemergency():
		""""""
    	pass
    	
	def api_managepresence():
		"""Manage a team member position"""
    	pass
    	
	def api_federationtable():
		""" endpoint used to access federation objects"""
    	pass
    	
	def api_alive():
		""""""
    	pass
    	
	def api_managevideostreamdeletevideostream():
		"""Delete the video stream"""
    	pass
    	
	def api_manageapigethelp():
		"""Retrieve API version and supported endpoints. * verb: GET * endpoint: /manageAPI/getHelp * returns: json containing API version and supported endpoints """
    	pass
    	
