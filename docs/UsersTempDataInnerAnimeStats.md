# UsersTempDataInnerAnimeStats

Anime Stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_watched** | **float** | Number of days spent watching Anime | [optional] 
**mean_score** | **float** | Mean Score | [optional] 
**watching** | **int** | Anime Watching | [optional] 
**completed** | **int** | Anime Completed | [optional] 
**on_hold** | **int** | Anime On-Hold | [optional] 
**dropped** | **int** | Anime Dropped | [optional] 
**plan_to_watch** | **int** | Anime Planned to Watch | [optional] 
**total_entries** | **int** | Total Anime entries on User list | [optional] 
**rewatched** | **int** | Anime re-watched | [optional] 
**episodes_watched** | **int** | Number of Anime Episodes Watched | [optional] 

## Example

```python
from jikan_openapi.models.users_temp_data_inner_anime_stats import UsersTempDataInnerAnimeStats

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTempDataInnerAnimeStats from a JSON string
users_temp_data_inner_anime_stats_instance = UsersTempDataInnerAnimeStats.from_json(json)
# print the JSON string representation of the object
print(UsersTempDataInnerAnimeStats.to_json())

# convert the object into a dict
users_temp_data_inner_anime_stats_dict = users_temp_data_inner_anime_stats_instance.to_dict()
# create an instance of UsersTempDataInnerAnimeStats from a dict
users_temp_data_inner_anime_stats_form_dict = users_temp_data_inner_anime_stats.from_dict(users_temp_data_inner_anime_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


