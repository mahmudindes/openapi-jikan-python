# UserProfileFullStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime** | [**UserProfileFullStatisticsAnime**](UserProfileFullStatisticsAnime.md) |  | [optional] 
**manga** | [**UserProfileFullStatisticsManga**](UserProfileFullStatisticsManga.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_profile_full_statistics import UserProfileFullStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileFullStatistics from a JSON string
user_profile_full_statistics_instance = UserProfileFullStatistics.from_json(json)
# print the JSON string representation of the object
print(UserProfileFullStatistics.to_json())

# convert the object into a dict
user_profile_full_statistics_dict = user_profile_full_statistics_instance.to_dict()
# create an instance of UserProfileFullStatistics from a dict
user_profile_full_statistics_form_dict = user_profile_full_statistics.from_dict(user_profile_full_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


