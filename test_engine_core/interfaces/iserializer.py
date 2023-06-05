from abc import abstractmethod
from typing import Any

from test_engine_core.interfaces.iplugin import IPlugin
from test_engine_core.plugins.enums.serializer_plugin_type import SerializerPluginType


class ISerializer(IPlugin):
    """
    The ISerializer interface specifies methods for different supported serializers
    """

    @staticmethod
    @abstractmethod
    def deserialize_data(data_path: str) -> Any:
        pass  # pragma: no cover

    @staticmethod
    @abstractmethod
    def get_serializer_plugin_type() -> SerializerPluginType:
        pass  # pragma: no cover
