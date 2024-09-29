# RecommendationsAllOfEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**MangaImages**](MangaImages.md) |  | [optional] 
**title** | **str** | Entry title | [optional] 

## Example

```python
from jikan_openapi.models.recommendations_all_of_entry import RecommendationsAllOfEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationsAllOfEntry from a JSON string
recommendations_all_of_entry_instance = RecommendationsAllOfEntry.from_json(json)
# print the JSON string representation of the object
print(RecommendationsAllOfEntry.to_json())

# convert the object into a dict
recommendations_all_of_entry_dict = recommendations_all_of_entry_instance.to_dict()
# create an instance of RecommendationsAllOfEntry from a dict
recommendations_all_of_entry_form_dict = recommendations_all_of_entry.from_dict(recommendations_all_of_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


