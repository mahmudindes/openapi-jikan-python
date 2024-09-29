# UserHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[History]**](History.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_history import UserHistory

# TODO update the JSON string below
json = "{}"
# create an instance of UserHistory from a JSON string
user_history_instance = UserHistory.from_json(json)
# print the JSON string representation of the object
print(UserHistory.to_json())

# convert the object into a dict
user_history_dict = user_history_instance.to_dict()
# create an instance of UserHistory from a dict
user_history_form_dict = user_history.from_dict(user_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


