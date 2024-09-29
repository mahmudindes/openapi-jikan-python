# UserStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserProfileFullStatistics**](UserProfileFullStatistics.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_statistics import UserStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatistics from a JSON string
user_statistics_instance = UserStatistics.from_json(json)
# print the JSON string representation of the object
print(UserStatistics.to_json())

# convert the object into a dict
user_statistics_dict = user_statistics_instance.to_dict()
# create an instance of UserStatistics from a dict
user_statistics_form_dict = user_statistics.from_dict(user_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


