# AnimeStatisticsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watching** | **int** | Number of users watching the resource | [optional] 
**completed** | **int** | Number of users who have completed the resource | [optional] 
**on_hold** | **int** | Number of users who have put the resource on hold | [optional] 
**dropped** | **int** | Number of users who have dropped the resource | [optional] 
**plan_to_watch** | **int** | Number of users who have planned to watch the resource | [optional] 
**total** | **int** | Total number of users who have the resource added to their lists | [optional] 
**scores** | [**List[AnimeStatisticsDataScoresInner]**](AnimeStatisticsDataScoresInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_statistics_data import AnimeStatisticsData

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeStatisticsData from a JSON string
anime_statistics_data_instance = AnimeStatisticsData.from_json(json)
# print the JSON string representation of the object
print(AnimeStatisticsData.to_json())

# convert the object into a dict
anime_statistics_data_dict = anime_statistics_data_instance.to_dict()
# create an instance of AnimeStatisticsData from a dict
anime_statistics_data_form_dict = anime_statistics_data.from_dict(anime_statistics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


