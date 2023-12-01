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


from typing import Any, Optional
from pydantic import BaseModel, Field
from bia_integrator_api.models.rendering_info import RenderingInfo

class BIAImageRepresentationOutput(BaseModel):
    """
    A particular representation of a BIAImage. Examples:  * A single HTTP accessible file. * Multiple HTTP accessible files, representing different channels, planes and time points. * An S3 accessible OME-Zarr. * A thumbnail.
    """
    size: Optional[Any] = Field(...)
    uri: Optional[Any] = None
    type: Optional[Any] = None
    dimensions: Optional[Any] = None
    attributes: Optional[Any] = None
    rendering: Optional[RenderingInfo] = None
    __properties = ["size", "uri", "type", "dimensions", "attributes", "rendering"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BIAImageRepresentationOutput:
        """Create an instance of BIAImageRepresentationOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of rendering
        if self.rendering:
            _dict['rendering'] = self.rendering.to_dict()
        # set to None if size (nullable) is None
        # and __fields_set__ contains the field
        if self.size is None and "size" in self.__fields_set__:
            _dict['size'] = None

        # set to None if uri (nullable) is None
        # and __fields_set__ contains the field
        if self.uri is None and "uri" in self.__fields_set__:
            _dict['uri'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if dimensions (nullable) is None
        # and __fields_set__ contains the field
        if self.dimensions is None and "dimensions" in self.__fields_set__:
            _dict['dimensions'] = None

        # set to None if attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.attributes is None and "attributes" in self.__fields_set__:
            _dict['attributes'] = None

        # set to None if rendering (nullable) is None
        # and __fields_set__ contains the field
        if self.rendering is None and "rendering" in self.__fields_set__:
            _dict['rendering'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BIAImageRepresentationOutput:
        """Create an instance of BIAImageRepresentationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BIAImageRepresentationOutput.parse_obj(obj)

        _obj = BIAImageRepresentationOutput.parse_obj({
            "size": obj.get("size"),
            "uri": obj.get("uri"),
            "type": obj.get("type"),
            "dimensions": obj.get("dimensions"),
            "attributes": obj.get("attributes"),
            "rendering": RenderingInfo.from_dict(obj.get("rendering")) if obj.get("rendering") is not None else None
        })
        return _obj


