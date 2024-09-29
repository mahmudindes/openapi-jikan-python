# PaginationPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_visible_page** | **int** |  | [optional] 
**has_next_page** | **bool** |  | [optional] 

## Example

```python
from jikan_openapi.models.pagination_pagination import PaginationPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPagination from a JSON string
pagination_pagination_instance = PaginationPagination.from_json(json)
# print the JSON string representation of the object
print(PaginationPagination.to_json())

# convert the object into a dict
pagination_pagination_dict = pagination_pagination_instance.to_dict()
# create an instance of PaginationPagination from a dict
pagination_pagination_form_dict = pagination_pagination.from_dict(pagination_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


