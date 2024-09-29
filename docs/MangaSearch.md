# MangaSearch

Manga Search Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPlusPagination**](PaginationPlusPagination.md) |  | [optional] 
**data** | [**List[Manga]**](Manga.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_search import MangaSearch

# TODO update the JSON string below
json = "{}"
# create an instance of MangaSearch from a JSON string
manga_search_instance = MangaSearch.from_json(json)
# print the JSON string representation of the object
print(MangaSearch.to_json())

# convert the object into a dict
manga_search_dict = manga_search_instance.to_dict()
# create an instance of MangaSearch from a dict
manga_search_form_dict = manga_search.from_dict(manga_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


