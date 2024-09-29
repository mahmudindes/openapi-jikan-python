# UsersTempDataInnerMangaStats

Manga Stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_read** | **float** | Number of days spent reading Manga | [optional] 
**mean_score** | **float** | Mean Score | [optional] 
**reading** | **int** | Manga Reading | [optional] 
**completed** | **int** | Manga Completed | [optional] 
**on_hold** | **int** | Manga On-Hold | [optional] 
**dropped** | **int** | Manga Dropped | [optional] 
**plan_to_read** | **int** | Manga Planned to Read | [optional] 
**total_entries** | **int** | Total Manga entries on User list | [optional] 
**reread** | **int** | Manga re-read | [optional] 
**chapters_read** | **int** | Number of Manga Chapters Read | [optional] 
**volumes_read** | **int** | Number of Manga Volumes Read | [optional] 

## Example

```python
from jikan_openapi.models.users_temp_data_inner_manga_stats import UsersTempDataInnerMangaStats

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTempDataInnerMangaStats from a JSON string
users_temp_data_inner_manga_stats_instance = UsersTempDataInnerMangaStats.from_json(json)
# print the JSON string representation of the object
print(UsersTempDataInnerMangaStats.to_json())

# convert the object into a dict
users_temp_data_inner_manga_stats_dict = users_temp_data_inner_manga_stats_instance.to_dict()
# create an instance of UsersTempDataInnerMangaStats from a dict
users_temp_data_inner_manga_stats_form_dict = users_temp_data_inner_manga_stats.from_dict(users_temp_data_inner_manga_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


