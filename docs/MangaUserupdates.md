# MangaUserupdates

Manga User Updates Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[MangaUserupdatesAllOfData]**](MangaUserupdatesAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_userupdates import MangaUserupdates

# TODO update the JSON string below
json = "{}"
# create an instance of MangaUserupdates from a JSON string
manga_userupdates_instance = MangaUserupdates.from_json(json)
# print the JSON string representation of the object
print(MangaUserupdates.to_json())

# convert the object into a dict
manga_userupdates_dict = manga_userupdates_instance.to_dict()
# create an instance of MangaUserupdates from a dict
manga_userupdates_form_dict = manga_userupdates.from_dict(manga_userupdates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


