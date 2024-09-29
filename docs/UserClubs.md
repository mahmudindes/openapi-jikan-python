# UserClubs

User Clubs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[UserClubsAllOfData]**](UserClubsAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_clubs import UserClubs

# TODO update the JSON string below
json = "{}"
# create an instance of UserClubs from a JSON string
user_clubs_instance = UserClubs.from_json(json)
# print the JSON string representation of the object
print(UserClubs.to_json())

# convert the object into a dict
user_clubs_dict = user_clubs_instance.to_dict()
# create an instance of UserClubs from a dict
user_clubs_form_dict = user_clubs.from_dict(user_clubs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


