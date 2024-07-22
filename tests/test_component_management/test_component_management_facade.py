import json
import os
from pathlib import PurePath
import shutil
from unittest import mock
from unittest.mock import MagicMock, patch
import zipfile
import pytest

from digitalpy.core.domain.domain.network_client import NetworkClient
from tests.testing_utilities.facade_utilities import (
    initialize_facade,
    initialize_test_environment,
)


@pytest.fixture
def client_mock():
    return MagicMock(spec=NetworkClient)


@pytest.fixture(scope="session", autouse=True)
def setup():
    mock.patch(
        "digitalpy.core.component_management.controllers.component_management_persistence_controller.DB_PATH",
        "sqlite:///tests/test_component_management/test_component_resources/test_data/component_management.db",
    ).start()

@pytest.fixture
def test_fs(zip_name: str):
    zip_path = PurePath("tests/test_component_management/test_component_resources/" + zip_name)
    content_path = PurePath("tests/test_component_management/test_component_resources/test_data")
    os.mkdir(content_path)
    with zipfile.ZipFile(zip_path, "r") as zipRef:
        zipRef.extractall(content_path)
    
    yield content_path

    shutil.rmtree(content_path)
    
@pytest.mark.parametrize("zip_name", ["test_discover_component.zip"])
def test_discover_components(client_mock, test_fs):
    mock.patch(
        "digitalpy.core.component_management.controllers.component_discovery_controller.COMPONENT_DOWNLOAD_PATH",
        PurePath(test_fs/"downloads"),
    ).start()

    request, response, _ = initialize_test_environment()

    component_management_facade = initialize_facade(
        "digitalpy.core.component_management.component_management_facade.ComponentManagement",
        request,
        response,
    )

    request.set_value("client", client_mock)

    component_management_facade.execute("GETComponentDiscovery")

    assert len(response.get_value("message")) == 1
    assert response.get_value("message")[0].name == "sample"



@patch(
    "digitalpy.core.component_management.controllers.component_pull_controller.requests.get"
)
@pytest.mark.parametrize("zip_name", ["test_pull_component.zip"])
def test_pull_component(mock_get, client_mock, test_fs):
    mock.patch(
        "digitalpy.core.component_management.controllers.component_pull_controller.COMPONENT_DOWNLOAD_PATH",
        PurePath(test_fs / "downloads"),
    ).start()

    zip_file_name = "example.zip"

    request, response, _ = initialize_test_environment()

    component_management_facade = initialize_facade(
        "digitalpy.core.component_management.component_management_facade.ComponentManagement",
        request,
        response,
    )

    mock_get.return_value.status_code = 200
    mock_get.return_value.iter_content.return_value = [b"examplezipcontent"]

    request.set_value("url", "http://example.com/" + zip_file_name)
    request.set_value("client", client_mock)

    component_management_facade.execute("GETPullComponent")

    save_path = response.get_value("message")[0]

    assert save_path.endswith(zip_file_name)

    assert os.path.exists(save_path)

    os.remove(save_path)

@pytest.mark.skip("This test works in isolation but for some reason a lock is being held on the log file. this prevents the test from cleaning up after itself therefore breaking others.")
@pytest.mark.parametrize("zip_name", ["test_install_component.zip"])
def test_install_component(client_mock, test_fs):
    mock.patch(
        "digitalpy.core.component_management.controllers.component_filesystem_controller.COMPONENT_DOWNLOAD_PATH",
        PurePath(test_fs / "downloads"),
    ).start()

    request, response, configuration = initialize_test_environment()

    configuration.set_value(
        "component_installation_path",
        PurePath(
            test_fs / "components"
        ),
        "ComponentManagement",
    )
    configuration.set_value(
        "component_import_root",
        "tests.test_component_management.test_component_resources.test_data.components",
        "ComponentManagement",
    )
    configuration.set_value(
        "component_blueprint_path",
        PurePath(
            test_fs / "blueprints"
        ),
        "ComponentManagement",
    )

    component_management_facade = initialize_facade(
        "digitalpy.core.component_management.component_management_facade.ComponentManagement",
        request,
        response,
    )

    request.set_value("client", client_mock)
    request.set_value("body", json.dumps({"name": "sample"}).encode("utf-8"))

    component_management_facade.execute("POSTComponent")

    component = response.get_value("message")[0]

    assert component.name == "sample"

    assert os.path.exists(
        PurePath(
            test_fs / "components/sample"
        )
    )


@pytest.mark.parametrize("zip_name", ["test_update_component.zip"])
@patch("digitalpy.core.component_management.controllers.component_management_persistence_controller_impl.Component_managementPersistenceControllerImpl.get_component")
def test_update_component(get_component_mock, client_mock, test_fs):
    mock.patch(
        "digitalpy.core.component_management.controllers.component_filesystem_controller.COMPONENT_DOWNLOAD_PATH",
        PurePath(test_fs / "downloads"),
    ).start()

    request, response, configuration = initialize_test_environment()

    configuration.set_value(
        "component_installation_path",
        PurePath(
            test_fs / "components"
        ),
        "ComponentManagement",
    )
    configuration.set_value(
        "component_import_root",
        "tests.test_component_management.test_component_resources.test_data.components",
        "ComponentManagement",
    )
    configuration.set_value(
        "component_blueprint_path",
        PurePath(
            test_fs / "blueprints"
        ),
        "ComponentManagement",
    )

    get_component_mock.return_value = [
        MagicMock(
            name="sample",
            oid=1,
            installation_path=test_fs / "components/sample",
        )
    ]

    request.set_value("client", client_mock)
    request.set_value(
        "body",
        json.dumps({"name": "sample"}).encode(
            "utf-8"
        ),
    )

    component_management_facade = initialize_facade(
        "digitalpy.core.component_management.component_management_facade.ComponentManagement",
        request,
        response,
    )

    component_management_facade.execute("PATCHComponent")

    