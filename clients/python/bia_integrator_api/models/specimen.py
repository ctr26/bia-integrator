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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, constr
from bia_integrator_api.models.model_metadata import ModelMetadata
from bia_integrator_api.models.specimen_annotation import SpecimenAnnotation

class Specimen(BaseModel):
    """
    Specimen
    """
    context: Optional[constr(strict=True, min_length=1)] = Field('https://raw.githubusercontent.com/BioImage-Archive/bia-integrator/main/api/src/models/jsonld/1.0/SpecimenContext.jsonld', alias="@context")
    attributes: Optional[Dict[str, Any]] = Field(None, description="         When annotations are applied, the ones that have a key different than an object attribute (so they don't overwrite it) get saved here.     ")
    annotations_applied: Optional[StrictBool] = Field(False, description="         This acts as a dirty flag, with the purpose of telling apart objects that had some fields overwritten by applying annotations (so should be rejected when writing), and those that didn't.     ")
    annotations: Optional[conlist(SpecimenAnnotation)] = None
    uuid: StrictStr = Field(...)
    version: StrictInt = Field(...)
    model: Optional[ModelMetadata] = None
    biosample_uuid: StrictStr = Field(...)
    title: StrictStr = Field(...)
    sample_preparation_protocol: StrictStr = Field(...)
    growth_protocol: StrictStr = Field(...)
    __properties = ["@context", "attributes", "annotations_applied", "annotations", "uuid", "version", "model", "biosample_uuid", "title", "sample_preparation_protocol", "growth_protocol"]

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
    def from_json(cls, json_str: str) -> Specimen:
        """Create an instance of Specimen from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # set to None if model (nullable) is None
        # and __fields_set__ contains the field
        if self.model is None and "model" in self.__fields_set__:
            _dict['model'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Specimen:
        """Create an instance of Specimen from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Specimen.parse_obj(obj)

        _obj = Specimen.parse_obj({
            "context": obj.get("@context") if obj.get("@context") is not None else 'https://raw.githubusercontent.com/BioImage-Archive/bia-integrator/main/api/src/models/jsonld/1.0/SpecimenContext.jsonld',
            "attributes": obj.get("attributes"),
            "annotations_applied": obj.get("annotations_applied") if obj.get("annotations_applied") is not None else False,
            "annotations": [SpecimenAnnotation.from_dict(_item) for _item in obj.get("annotations")] if obj.get("annotations") is not None else None,
            "uuid": obj.get("uuid"),
            "version": obj.get("version"),
            "model": ModelMetadata.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "biosample_uuid": obj.get("biosample_uuid"),
            "title": obj.get("title"),
            "sample_preparation_protocol": obj.get("sample_preparation_protocol"),
            "growth_protocol": obj.get("growth_protocol")
        })
        return _obj


