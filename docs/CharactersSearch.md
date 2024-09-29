# CharactersSearch

Characters Search Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPlusPagination**](PaginationPlusPagination.md) |  | [optional] 
**data** | [**List[Character]**](Character.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.characters_search import CharactersSearch

# TODO update the JSON string below
json = "{}"
# create an instance of CharactersSearch from a JSON string
characters_search_instance = CharactersSearch.from_json(json)
# print the JSON string representation of the object
print(CharactersSearch.to_json())

# convert the object into a dict
characters_search_dict = characters_search_instance.to_dict()
# create an instance of CharactersSearch from a dict
characters_search_form_dict = characters_search.from_dict(characters_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


