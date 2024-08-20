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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from bia_integrator_api.models.affiliation import Affiliation
from typing import Optional, Set
from typing_extensions import Self

class Contributor(BaseModel):
    """
    A person or group that contributed to the creation of a Document.
    """ # noqa: E501
    rorid: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    website: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    orcid: Optional[StrictStr] = None
    display_name: StrictStr = Field(description="Name as it should be displayed on the BioImage Archive.")
    affiliation: List[Affiliation] = Field(description="The organisation(s) a contributor is afiliated with.")
    contact_email: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["rorid", "address", "website", "orcid", "display_name", "affiliation", "contact_email", "role"]

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
        """Create an instance of Contributor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in affiliation (list)
        _items = []
        if self.affiliation:
            for _item_affiliation in self.affiliation:
                if _item_affiliation:
                    _items.append(_item_affiliation.to_dict())
            _dict['affiliation'] = _items
        # set to None if rorid (nullable) is None
        # and model_fields_set contains the field
        if self.rorid is None and "rorid" in self.model_fields_set:
            _dict['rorid'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if orcid (nullable) is None
        # and model_fields_set contains the field
        if self.orcid is None and "orcid" in self.model_fields_set:
            _dict['orcid'] = None

        # set to None if contact_email (nullable) is None
        # and model_fields_set contains the field
        if self.contact_email is None and "contact_email" in self.model_fields_set:
            _dict['contact_email'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Contributor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rorid": obj.get("rorid"),
            "address": obj.get("address"),
            "website": obj.get("website"),
            "orcid": obj.get("orcid"),
            "display_name": obj.get("display_name"),
            "affiliation": [Affiliation.from_dict(_item) for _item in obj["affiliation"]] if obj.get("affiliation") is not None else None,
            "contact_email": obj.get("contact_email"),
            "role": obj.get("role")
        })
        return _obj


