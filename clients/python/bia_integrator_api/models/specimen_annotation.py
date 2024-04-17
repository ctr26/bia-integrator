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



from pydantic import BaseModel, Field, StrictStr
from bia_integrator_api.models.annotation_state import AnnotationState

class SpecimenAnnotation(BaseModel):
    """
    SpecimenAnnotation
    """
    author_email: StrictStr = Field(...)
    key: StrictStr = Field(...)
    value: StrictStr = Field(...)
    state: AnnotationState = Field(...)
    __properties = ["author_email", "key", "value", "state"]

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
    def from_json(cls, json_str: str) -> SpecimenAnnotation:
        """Create an instance of SpecimenAnnotation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpecimenAnnotation:
        """Create an instance of SpecimenAnnotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpecimenAnnotation.parse_obj(obj)

        _obj = SpecimenAnnotation.parse_obj({
            "author_email": obj.get("author_email"),
            "key": obj.get("key"),
            "value": obj.get("value"),
            "state": obj.get("state")
        })
        return _obj


