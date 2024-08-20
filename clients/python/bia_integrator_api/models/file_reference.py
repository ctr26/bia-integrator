# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from bia_integrator_api.models.model_metadata import ModelMetadata
from typing import Optional, Set
from typing_extensions import Self

class FileReference(BaseModel):
    """
    FileReference
    """ # noqa: E501
    uuid: StrictStr = Field(description="Unique ID (across the BIA database) used to refer to and identify a document.")
    version: StrictInt = Field(description="Document version. This can't be optional to make sure we never persist objects without it")
    model: Optional[ModelMetadata]
    file_path: StrictStr = Field(description="The path (including the name) of the file.")
    format: StrictStr = Field(description="File format or type.")
    size_in_bytes: StrictInt = Field(description="Disc size in bytes.")
    uri: StrictStr = Field(description="URI from which the file can be accessed.")
    attribute: Dict[str, Any] = Field(description="Freeform key-value pairs from user provided metadata (e.g. filelist data) and experimental fields.")
    submission_dataset_uuid: StrictStr
    __properties: ClassVar[List[str]] = ["uuid", "version", "model", "file_path", "format", "size_in_bytes", "uri", "attribute", "submission_dataset_uuid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FileReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "version": obj.get("version"),
            "model": ModelMetadata.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "file_path": obj.get("file_path"),
            "format": obj.get("format"),
            "size_in_bytes": obj.get("size_in_bytes"),
            "uri": obj.get("uri"),
            "attribute": obj.get("attribute"),
            "submission_dataset_uuid": obj.get("submission_dataset_uuid")
        })
        return _obj


