# AnimeUserupdates

Anime User Updates Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[AnimeUserupdatesAllOfData]**](AnimeUserupdatesAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_userupdates import AnimeUserupdates

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeUserupdates from a JSON string
anime_userupdates_instance = AnimeUserupdates.from_json(json)
# print the JSON string representation of the object
print(AnimeUserupdates.to_json())

# convert the object into a dict
anime_userupdates_dict = anime_userupdates_instance.to_dict()
# create an instance of AnimeUserupdates from a dict
anime_userupdates_form_dict = anime_userupdates.from_dict(anime_userupdates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


