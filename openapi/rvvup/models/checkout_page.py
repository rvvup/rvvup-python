from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.checkout import Checkout
    from ..models.pageable import Pageable


T = TypeVar("T", bound="CheckoutPage")


@_attrs_define
class CheckoutPage:
    """
    Attributes:
        pageable (Pageable):
        results (List['Checkout']):
        total (int):
    """

    pageable: "Pageable"
    results: List["Checkout"]
    total: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pageable = self.pageable.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageable": pageable,
                "results": results,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout import Checkout
        from ..models.pageable import Pageable

        d = src_dict.copy()
        pageable = Pageable.from_dict(d.pop("pageable"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = Checkout.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        checkout_page = cls(
            pageable=pageable,
            results=results,
            total=total,
        )

        checkout_page.additional_properties = d
        return checkout_page

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
