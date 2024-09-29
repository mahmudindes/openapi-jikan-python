# PaginationPlusPaginationItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from jikan_openapi.models.pagination_plus_pagination_items import PaginationPlusPaginationItems

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPlusPaginationItems from a JSON string
pagination_plus_pagination_items_instance = PaginationPlusPaginationItems.from_json(json)
# print the JSON string representation of the object
print(PaginationPlusPaginationItems.to_json())

# convert the object into a dict
pagination_plus_pagination_items_dict = pagination_plus_pagination_items_instance.to_dict()
# create an instance of PaginationPlusPaginationItems from a dict
pagination_plus_pagination_items_form_dict = pagination_plus_pagination_items.from_dict(pagination_plus_pagination_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


