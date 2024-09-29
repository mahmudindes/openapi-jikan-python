# AnimeStatistics

Anime Statistics Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnimeStatisticsData**](AnimeStatisticsData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_statistics import AnimeStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeStatistics from a JSON string
anime_statistics_instance = AnimeStatistics.from_json(json)
# print the JSON string representation of the object
print(AnimeStatistics.to_json())

# convert the object into a dict
anime_statistics_dict = anime_statistics_instance.to_dict()
# create an instance of AnimeStatistics from a dict
anime_statistics_form_dict = anime_statistics.from_dict(anime_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


