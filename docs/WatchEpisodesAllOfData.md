# WatchEpisodesAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**AnimeMeta**](AnimeMeta.md) |  | [optional] 
**episodes** | [**List[WatchEpisodesAllOfEpisodes]**](WatchEpisodesAllOfEpisodes.md) | Recent Episodes (max 2 listed) | [optional] 
**region_locked** | **bool** | Region Locked Episode | [optional] 

## Example

```python
from jikan_openapi.models.watch_episodes_all_of_data import WatchEpisodesAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of WatchEpisodesAllOfData from a JSON string
watch_episodes_all_of_data_instance = WatchEpisodesAllOfData.from_json(json)
# print the JSON string representation of the object
print(WatchEpisodesAllOfData.to_json())

# convert the object into a dict
watch_episodes_all_of_data_dict = watch_episodes_all_of_data_instance.to_dict()
# create an instance of WatchEpisodesAllOfData from a dict
watch_episodes_all_of_data_form_dict = watch_episodes_all_of_data.from_dict(watch_episodes_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


