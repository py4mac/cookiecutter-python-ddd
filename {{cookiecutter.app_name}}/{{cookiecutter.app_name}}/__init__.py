# pylint: disable=wrong-import-position
import {{cookiecutter.app_name}}.services  # noqa
from {{cookiecutter.app_name}}.utils.logging_utils import _configure_{{cookiecutter.app_name}}_loggers
from {{cookiecutter.app_name}}.version import VERSION as __version__  # noqa

_configure_{{cookiecutter.app_name}}_loggers(root_module_name=__name__)


create_experiment = {{cookiecutter.app_name}}.services.create_experiment
get_experiment_by_uuid = lgbsttracker.services.get_experiment_by_uuid

__all__ = [
    "create_experiment",
    "get_experiment_by_uuid",
]
