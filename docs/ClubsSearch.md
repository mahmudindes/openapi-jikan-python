# ClubsSearch

Clubs Search Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[Club]**](Club.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.clubs_search import ClubsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ClubsSearch from a JSON string
clubs_search_instance = ClubsSearch.from_json(json)
# print the JSON string representation of the object
print(ClubsSearch.to_json())

# convert the object into a dict
clubs_search_dict = clubs_search_instance.to_dict()
# create an instance of ClubsSearch from a dict
clubs_search_form_dict = clubs_search.from_dict(clubs_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


