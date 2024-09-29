# PaginationPlus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPlusPagination**](PaginationPlusPagination.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.pagination_plus import PaginationPlus

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPlus from a JSON string
pagination_plus_instance = PaginationPlus.from_json(json)
# print the JSON string representation of the object
print(PaginationPlus.to_json())

# convert the object into a dict
pagination_plus_dict = pagination_plus_instance.to_dict()
# create an instance of PaginationPlus from a dict
pagination_plus_form_dict = pagination_plus.from_dict(pagination_plus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


