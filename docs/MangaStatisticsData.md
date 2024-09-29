# MangaStatisticsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reading** | **int** | Number of users reading the resource | [optional] 
**completed** | **int** | Number of users who have completed the resource | [optional] 
**on_hold** | **int** | Number of users who have put the resource on hold | [optional] 
**dropped** | **int** | Number of users who have dropped the resource | [optional] 
**plan_to_read** | **int** | Number of users who have planned to read the resource | [optional] 
**total** | **int** | Total number of users who have the resource added to their lists | [optional] 
**scores** | [**List[AnimeStatisticsDataScoresInner]**](AnimeStatisticsDataScoresInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_statistics_data import MangaStatisticsData

# TODO update the JSON string below
json = "{}"
# create an instance of MangaStatisticsData from a JSON string
manga_statistics_data_instance = MangaStatisticsData.from_json(json)
# print the JSON string representation of the object
print(MangaStatisticsData.to_json())

# convert the object into a dict
manga_statistics_data_dict = manga_statistics_data_instance.to_dict()
# create an instance of MangaStatisticsData from a dict
manga_statistics_data_form_dict = manga_statistics_data.from_dict(manga_statistics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


