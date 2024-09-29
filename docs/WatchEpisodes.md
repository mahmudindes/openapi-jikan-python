# WatchEpisodes

Watch Episodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[WatchEpisodesAllOfData]**](WatchEpisodesAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.watch_episodes import WatchEpisodes

# TODO update the JSON string below
json = "{}"
# create an instance of WatchEpisodes from a JSON string
watch_episodes_instance = WatchEpisodes.from_json(json)
# print the JSON string representation of the object
print(WatchEpisodes.to_json())

# convert the object into a dict
watch_episodes_dict = watch_episodes_instance.to_dict()
# create an instance of WatchEpisodes from a dict
watch_episodes_form_dict = watch_episodes.from_dict(watch_episodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


