#######################################################
#
# default_persistence_facade.py
# Python implementation of the Class DefaultPersistenceFacade
# Generated by Enterprise Architect
# Created on:      29-Aug-2022 9:43:05 AM
# Original author: ingo herwig <ingo@wemove.com>
#
#######################################################
from typing import Any
from digitalpy.core.event_manager import EventManager
from digitalpy.model.object_id import ObjectId
from digitalpy.model.persistence_facade import PersistenceFacade
from digitalpy.model.persistent_object import PersistentObject
from digitalpy.model.build_depth import BuildDepth
from digitalpy.model.paging_info import PagingInfo
from digitalpy.model.persistence_mapper import PersistenceMapper
from digitalpy.core.state_change_event import StateChangeEvent


class DefaultPersistenceFacade(PersistenceFacade):
    """Default PersistenceFacade implementation."""

    __createdOIDs = []
    __currentTransaction = None
    __eventManager = None
    __logStrategy = None
    __mappers = []
    simple_to_fq_names = {}

    def __init__(self, event_manager: EventManager) -> Any:
        """Constructor
        @param $eventManager
        @param $logStrategy OutputStrategy used for logging persistence actions.
        """
        pass

    def __del__(self) -> Any:
        """Destructor"""
        pass

    def calculate_simple_type(self, type: Any) -> Any:
        """_calculate the simple type name for a given fully qualified type name.
        @param $type _type name with namespace
        @return _simple type name (without namespace)
        """
        pos = type.find("+")
        if pos != False:
            return type[pos + 1 :]

        return type

    def __check_array_parameter(
        self, param: Any, param_name: Any, class_name: Any = None
    ) -> Any:
        """_check if the given value is either None or an array and throw an exception if
        not
           @param $param _the parameter
           @param $param_name _the name of the parameter (used in the exception text)
           @param $class_name _class name to match if, instances of a specific type are
        expected (optional)
        """
        if param == None:
            return

        if not isinstance(param, list):
            raise ValueError(
                "_the parameter '" + param_name + "' is expected to be None or an array"
            )

        if class_name != None:
            for instance in param:
                if instance.__class__.__name__ != class_name:
                    raise ValueError(
                        "_the parameter '"
                        + param_name
                        + "' is expected to contain only instances of '"
                        + class_name
                        + "'"
                    )

    def create(self, type: Any, build_depth: Any = BuildDepth.SINGLE) -> Any:
        """@see _persistence_facade::create()"""
        if build_depth < 0 and build_depth not in [
            BuildDepth.INFINITE,
            BuildDepth.SINGLE,
            BuildDepth.REQUIRED,
        ]:
            raise ValueError("_build depth not supported: build_depth")
        mapper = self.get_mapper(type)
        obj = mapper.create(type, build_depth)

        # attach the object to the transaction
        attached_object = self.get_transaction().attach(obj)

        return attached_object

    def get_first_OID(
        self,
        type: Any,
        criteria: Any = None,
        orderby: Any = None,
        paging_info: PagingInfo = None,
    ) -> Any:
        """@see _persistence_facade::get_first_oID()"""
        if pagingInfo == None:
            pagingInfo = PagingInfo(1, True)

        oids = self.get_OIDs(type, criteria, orderby, pagingInfo)
        if len(oids) > 0:
            return oids[0]

        else:
            return None

    def get_fully_qualified_type(self, type: Any) -> Any:
        """@see _persistence_facade::get_fully_qualified_type()"""
        if type in self.simple_to_fq_names:
            return self.simple_to_fq_names[type]

        if self.is_known_type(type):
            return type

        raise ValueError("_type '" + type + "' is unknown.")

    def get_known_types(self) -> Any:
        """@see _persistence_facade::get_known_types()"""
        return self.simple_to_fq_names.values()

    def get_last_created_OID(self, type: Any) -> Any:
        """@see _persistence_facade::get_last_created_oID()"""
        pass

    def get_mapper(self, type: Any) -> Any:
        """@see _persistence_facade::get_mapper()"""
        if self.is_known_type(type):
            mapper = self.mappers[type]
            return mapper
        else:
            raise ValueError("No persistence mapper found for type "+type)

    def set_mapper(self, type, mapper: PersistenceMapper):
        self.mappers[type] = mapper
    
    def set_mappers(self, mappers):
        self.mappers = mappers
        for fq_name, mapper in self.mappers.items():
            name = self.calculate_simple_type(fq_name)
            if not name in self.simple_to_fq_names:
                self.simple_to_fq_names[name] = fq_name
            else:
                del self.simple_to_fq_names
            
    def get_OIDs(
        self,
        type: Any,
        criteria: Any = None,
        orderby: Any = None,
        paging_info: PagingInfo = None,
    ) -> Any:
        """@see _persistence_facade::get_oI_ds()"""
        raise NotImplementedError("this method has not yet been implemented")

    def get_simple_type(self, type: Any) -> Any:
        """@see _persistence_facade::get_simple_type()"""
        simple_type = self.calculate_simple_type(type)
        # if there is a entry for the type name but not for the simple type name,
        # the type is ambiquous and we return the type name
        return (
            lambda: type
            if (type in self.__mappers and simple_type not in self.simple_to_fq_names)
            else simple_type
        )

    def get_transaction(self) -> Any:
        """@see _persistence_facade::get_transaction()"""
        pass

    def is_known_type(self, type: Any) -> Any:
        """@see _persistence_facade::is_known_type()"""
        return type in self.__mappers

    def load(self, oid: ObjectId, build_depth: Any = BuildDepth.SINGLE) -> Any:
        """@see _persistence_facade::load()"""
        if build_depth < 0 and not build_depth in [
            BuildDepth.INFINITE,
            BuildDepth.SINGLE,
        ]:
            raise ValueError("_build depth not supported: build_depth")

        # check if the object is already part of the transaction
        transaction = self.get_transaction()
        obj = transaction.get_loaded(oid)

        # if not cached or build depth requested, load
        if obj == None or build_depth != BuildDepth.SINGLE:
            mapper = self.get_mapper(oid.get_type())
            obj = mapper.load(oid, build_depth)

        return obj

    def load_first_object(
        type_or_types: Any,
        build_depth: Any = BuildDepth.SINGLE,
        criteria: Any = None,
        orderby: Any = None,
        paging_info: PagingInfo = None,
    ) -> Any:
        """@see _persistence_facade::load_first_object()"""
        pass

    def load_objects(
        self,
        type_or_types: Any,
        build_depth: Any = BuildDepth.SINGLE,
        criteria: Any = None,
        orderby: Any = None,
        paging_info: PagingInfo = None,
    ) -> Any:
        """@see _persistence_facade::load_objects()"""
        raise NotImplementedError("this method is not yet implemented")

    def set_mapper(self, type: Any, mapper: PersistenceMapper) -> Any:
        """@see _persistence_facade::set_mapper()"""
        self.__mappers[type] = mapper

    def set_mappers(self, mappers: Any) -> Any:
        """_set the _persistent_mapper instances.
           @param $mappers _associative array with the fully qualified mapped class
        names as keys and the mapper instances as values
        """
        self.__mappers = mappers
        for fq_name, mapper in mappers.items():
            # register simple type names
            name = self.calculate_simple_type(fq_name)
            if name not in self.__mappers:
                self.__mappers[name] = mapper
                if name not in self.simple_to_fq_names:
                    self.simple_to_fq_names[name] = fq_name

                else:
                    # if the simple type name already exists, we remove
                    # it in order to prevent collisions with the new type
                    del self.simple_to_fq_names[name]

            # set logging strategy
            mapper.set_log_strategy(self.log_strategy)

    def state_changed(self, event: StateChangeEvent) -> Any:
        """_listen to _state_change_events
        @param $event _state_change_event instance
        """
        old_state = event.get_old_value()
        new_state = event.get_new_value()
        # store the object id in the internal registry if the object was saved after creation
        if (
            old_state == PersistentObject.STATE_NEW
            and new_state == PersistentObject.STATE_CLEAN
        ):
            object = event.get_object()
            type = object.get_type()
            if not type in self.created_OIDs:
                self.created_OIDs[type] = []

            self.created_OIDs[type].append(object.get_oID())
