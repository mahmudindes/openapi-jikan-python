# UserProfileFullStatisticsManga

Manga Statistics

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
from jikan_openapi.models.user_profile_full_statistics_manga import UserProfileFullStatisticsManga

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileFullStatisticsManga from a JSON string
user_profile_full_statistics_manga_instance = UserProfileFullStatisticsManga.from_json(json)
# print the JSON string representation of the object
print(UserProfileFullStatisticsManga.to_json())

# convert the object into a dict
user_profile_full_statistics_manga_dict = user_profile_full_statistics_manga_instance.to_dict()
# create an instance of UserProfileFullStatisticsManga from a dict
user_profile_full_statistics_manga_form_dict = user_profile_full_statistics_manga.from_dict(user_profile_full_statistics_manga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


