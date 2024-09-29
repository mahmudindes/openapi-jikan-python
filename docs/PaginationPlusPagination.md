# PaginationPlusPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_visible_page** | **int** |  | [optional] 
**has_next_page** | **bool** |  | [optional] 
**items** | [**PaginationPlusPaginationItems**](PaginationPlusPaginationItems.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.pagination_plus_pagination import PaginationPlusPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPlusPagination from a JSON string
pagination_plus_pagination_instance = PaginationPlusPagination.from_json(json)
# print the JSON string representation of the object
print(PaginationPlusPagination.to_json())

# convert the object into a dict
pagination_plus_pagination_dict = pagination_plus_pagination_instance.to_dict()
# create an instance of PaginationPlusPagination from a dict
pagination_plus_pagination_form_dict = pagination_plus_pagination.from_dict(pagination_plus_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


