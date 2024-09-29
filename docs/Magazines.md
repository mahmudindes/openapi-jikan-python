# Magazines

Magazine Collection Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[Magazine]**](Magazine.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.magazines import Magazines

# TODO update the JSON string below
json = "{}"
# create an instance of Magazines from a JSON string
magazines_instance = Magazines.from_json(json)
# print the JSON string representation of the object
print(Magazines.to_json())

# convert the object into a dict
magazines_dict = magazines_instance.to_dict()
# create an instance of Magazines from a dict
magazines_form_dict = magazines.from_dict(magazines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


