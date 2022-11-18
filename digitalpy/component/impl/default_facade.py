from digitalpy.routing.controller import Controller
from digitalpy.model.node import Node
from digitalpy.model.load_configuration import LoadConfiguration
from digitalpy.config.impl.inifile_configuration import InifileConfiguration
from digitalpy.routing.impl.default_action_mapper import DefaultActionMapper
from digitalpy.core.impl.default_event_manager import DefaultEventManager
from digitalpy.core.object_factory import ObjectFactory
from digitalpy.core.log_manager import LogManager
from digitalpy.core.object_factory import ObjectFactory
from digitalpy.core.impl.default_file_logger import DefaultFileLogger
from digitalpy.routing.controller import Controller
from digitalpy.telemetry.tracer import Tracer


class DefaultFacade(Controller):
    def __init__(
        self,
        action_mapping_path,
        internal_action_mapping_path,
        logger_configuration,
        log_file_path,
        component_name=None,
        type_mapping=None,
        action_mapper=None,
        base=object,
        request=None,
        response=None,
        configuration=None,
        configuration_path_template=None,
        tracing_provider_instance=None,
        manifest_path=None,
        **kwargs,
    ):
        super().__init__(
            action_mapper=action_mapper,
            request=request,
            response=response,
            configuration=configuration,
        )
        self.last_event = ""
        self.base = base

        self.action_mapping_path = action_mapping_path
        self.internal_action_mapping_path = internal_action_mapping_path
        self.type_mapping = type_mapping
        self.action_mapper = action_mapper
        if component_name is not None:
            self.component_name = component_name
        else:
            self.component_name = self.__class__.__name__

        # get a tacer from the tracer provider
        
        if tracing_provider_instance is not None:
            self.tracer: Tracer = tracing_provider_instance.create_tracer(
                component_name
            )
        else:
            self.tracer = None
        # load the manifest file as a configuration
        if manifest_path is not None:
            self.manifest = InifileConfiguration("")
            self.manifest.add_configuration(manifest_path)

        # define the logging
        self.log_manager = LogManager()
        DefaultFileLogger.set_base_logging_path(log_file_path)
        self.log_manager.configure(
            DefaultFileLogger(
                name=self.component_name, config_file=logger_configuration
            )
        )
        self.logger = self.log_manager.get_logger()
        if configuration_path_template:
            self.config_loader = LoadConfiguration(configuration_path_template)
        else:
            self.config_loader = None

    def initialize(self, request, response):
        super().initialize(request, response)
        self.request.set_sender(self.__class__.__name__)

    def execute(self, method):
        self.request.set_value("logger", self.logger)
        self.request.set_value("config_loader", self.config_loader)
        self.request.set_value("tracer", self.tracer)
        try:
            if hasattr(self, method):
                getattr(self, method)()
            else:
                response = self.execute_sub_action(self.request.get_action())
                self.response.set_values(response.get_values())
        except Exception as e:
            self.logger.fatal(str(e))

    def get_logs(self):
        """get all the log files available"""
        return self.log_manager.get_logs()

    def discover(self):
        """discover the action mappings from the component"""
        config = InifileConfiguration(config_path=self.action_mapping_path)
        return config.config_array

    def register(self, config: InifileConfiguration):
        config.add_configuration(self.action_mapping_path)
        internal_config = InifileConfiguration("")
        internal_config.add_configuration(self.internal_action_mapping_path)
        ObjectFactory.register_instance(
            f"{self.component_name.lower()}actionmapper",
            self.base.ActionMapper(
                ObjectFactory.get_instance("event_manager"),
                internal_config,
            ),
        )
        self._register_type_mapping()

    def get_manifest(self):
        """returns the current manifest configuration"""
        return self.manifest

    def _register_type_mapping(self):
        """any component may or may not have a type mapping defined,
        if it does then it should be registered"""
        if self.type_mapping:
            request = ObjectFactory.get_new_instance("request")
            request.set_action("RegisterMachineToHumanMapping")
            request.set_value("machine_to_human_mapping", self.type_mapping)

            actionmapper = ObjectFactory.get_instance("syncactionMapper")
            response = ObjectFactory.get_new_instance("response")
            actionmapper.process_action(request, response)

            request = ObjectFactory.get_new_instance("request")
            request.set_action("RegisterHumanToMachineMapping")
            # reverse the mapping and save the reversed mapping
            request.set_value(
                "human_to_machine_mapping", {k: v for v, k in self.type_mapping.items()}
            )

            actionmapper = ObjectFactory.get_instance("actionMapper")
            response = ObjectFactory.get_new_instance("response")
            actionmapper.process_action(request, response)

    def accept_visitor(self, node: Node, visitor, **kwargs):
        return node.accept_visitor(visitor)
