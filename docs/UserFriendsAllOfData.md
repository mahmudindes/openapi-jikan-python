# UserFriendsAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserMeta**](UserMeta.md) |  | [optional] 
**last_online** | **str** | Last Online Date ISO8601 format | [optional] 
**friends_since** | **str** | Friends Since Date ISO8601 format | [optional] 

## Example

```python
from jikan_openapi.models.user_friends_all_of_data import UserFriendsAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of UserFriendsAllOfData from a JSON string
user_friends_all_of_data_instance = UserFriendsAllOfData.from_json(json)
# print the JSON string representation of the object
print(UserFriendsAllOfData.to_json())

# convert the object into a dict
user_friends_all_of_data_dict = user_friends_all_of_data_instance.to_dict()
# create an instance of UserFriendsAllOfData from a dict
user_friends_all_of_data_form_dict = user_friends_all_of_data.from_dict(user_friends_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


