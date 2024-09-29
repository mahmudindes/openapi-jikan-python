# UserFriends

User Friends

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[UserFriendsAllOfData]**](UserFriendsAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_friends import UserFriends

# TODO update the JSON string below
json = "{}"
# create an instance of UserFriends from a JSON string
user_friends_instance = UserFriends.from_json(json)
# print the JSON string representation of the object
print(UserFriends.to_json())

# convert the object into a dict
user_friends_dict = user_friends_instance.to_dict()
# create an instance of UserFriends from a dict
user_friends_form_dict = user_friends.from_dict(user_friends_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


