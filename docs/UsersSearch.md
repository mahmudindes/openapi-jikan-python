# UsersSearch

User Results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[UsersSearchAllOfData]**](UsersSearchAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.users_search import UsersSearch

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSearch from a JSON string
users_search_instance = UsersSearch.from_json(json)
# print the JSON string representation of the object
print(UsersSearch.to_json())

# convert the object into a dict
users_search_dict = users_search_instance.to_dict()
# create an instance of UsersSearch from a dict
users_search_form_dict = users_search.from_dict(users_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


