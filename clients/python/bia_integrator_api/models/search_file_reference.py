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


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class SearchFileReference(BaseModel):
    """
    SearchFileReference
    """
    uri_prefix: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    size_bounds_lte: Optional[StrictInt] = None
    size_bounds_gte: Optional[StrictInt] = None
    __properties = ["uri_prefix", "type", "name", "size_bounds_lte", "size_bounds_gte"]

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
    def from_json(cls, json_str: str) -> SearchFileReference:
        """Create an instance of SearchFileReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if uri_prefix (nullable) is None
        # and __fields_set__ contains the field
        if self.uri_prefix is None and "uri_prefix" in self.__fields_set__:
            _dict['uri_prefix'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if size_bounds_lte (nullable) is None
        # and __fields_set__ contains the field
        if self.size_bounds_lte is None and "size_bounds_lte" in self.__fields_set__:
            _dict['size_bounds_lte'] = None

        # set to None if size_bounds_gte (nullable) is None
        # and __fields_set__ contains the field
        if self.size_bounds_gte is None and "size_bounds_gte" in self.__fields_set__:
            _dict['size_bounds_gte'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchFileReference:
        """Create an instance of SearchFileReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchFileReference.parse_obj(obj)

        _obj = SearchFileReference.parse_obj({
            "uri_prefix": obj.get("uri_prefix"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "size_bounds_lte": obj.get("size_bounds_lte"),
            "size_bounds_gte": obj.get("size_bounds_gte")
        })
        return _obj


