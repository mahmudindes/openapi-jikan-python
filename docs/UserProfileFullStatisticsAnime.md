# UserProfileFullStatisticsAnime

Anime Statistics

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
from jikan_openapi.models.user_profile_full_statistics_anime import UserProfileFullStatisticsAnime

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileFullStatisticsAnime from a JSON string
user_profile_full_statistics_anime_instance = UserProfileFullStatisticsAnime.from_json(json)
# print the JSON string representation of the object
print(UserProfileFullStatisticsAnime.to_json())

# convert the object into a dict
user_profile_full_statistics_anime_dict = user_profile_full_statistics_anime_instance.to_dict()
# create an instance of UserProfileFullStatisticsAnime from a dict
user_profile_full_statistics_anime_form_dict = user_profile_full_statistics_anime.from_dict(user_profile_full_statistics_anime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


