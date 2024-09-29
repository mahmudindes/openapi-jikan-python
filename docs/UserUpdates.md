# UserUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserUpdatesData**](UserUpdatesData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_updates import UserUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdates from a JSON string
user_updates_instance = UserUpdates.from_json(json)
# print the JSON string representation of the object
print(UserUpdates.to_json())

# convert the object into a dict
user_updates_dict = user_updates_instance.to_dict()
# create an instance of UserUpdates from a dict
user_updates_form_dict = user_updates.from_dict(user_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


