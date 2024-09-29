# AnimeSearch

Anime Collection Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPlusPagination**](PaginationPlusPagination.md) |  | [optional] 
**data** | [**List[Anime]**](Anime.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_search import AnimeSearch

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeSearch from a JSON string
anime_search_instance = AnimeSearch.from_json(json)
# print the JSON string representation of the object
print(AnimeSearch.to_json())

# convert the object into a dict
anime_search_dict = anime_search_instance.to_dict()
# create an instance of AnimeSearch from a dict
anime_search_form_dict = anime_search.from_dict(anime_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


