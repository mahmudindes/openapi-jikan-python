# PeopleSearch

People Search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPlusPagination**](PaginationPlusPagination.md) |  | [optional] 
**data** | [**List[PeopleSearchAllOfData]**](PeopleSearchAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.people_search import PeopleSearch

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSearch from a JSON string
people_search_instance = PeopleSearch.from_json(json)
# print the JSON string representation of the object
print(PeopleSearch.to_json())

# convert the object into a dict
people_search_dict = people_search_instance.to_dict()
# create an instance of PeopleSearch from a dict
people_search_form_dict = people_search.from_dict(people_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


