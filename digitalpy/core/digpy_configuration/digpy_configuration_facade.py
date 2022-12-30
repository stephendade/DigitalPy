from Catalog.Data.Domain.FTS_Model.Facade import Facade

class DigPyConfigurationFacade(Facade, Facade):
    """Facade class for the this component. Responsible for handling all public
    routing. Forwards all requests to the internal router.
      WHY
      <ul>
      	<li><b>Isolation</b>: We can easily isolate our code from the complexity of
    a subsystem.</li>
      	<li><b>Testing Process</b>: Using Facade Method makes the process of testing
    comparatively easy since it has convenient methods for common testing tasks.
    </li>
      	<li><b>Loose Coupling</b>: Availability of loose coupling between the
    clients and the Subsystems.</li>
      </ul>
    """
	
# default constructor  def __init__(self):  

    def __init__(self):
		self.configure_dp_ip = DigPyConfigurationGeneralController()
		self.web_ui__manage_services = DigPyConfigurationGeneralController()
		self.installation_wizard = DigPyConfigurationGeneralController()
		self.configure__set_port = DigPyConfigurationGeneralController()
		self.configuration_wizard = DigPyConfigurationGeneralController()
	

