# UsersTemp

Transform the resource into an array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsersTempDataInner]**](UsersTempDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.users_temp import UsersTemp

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTemp from a JSON string
users_temp_instance = UsersTemp.from_json(json)
# print the JSON string representation of the object
print(UsersTemp.to_json())

# convert the object into a dict
users_temp_dict = users_temp_instance.to_dict()
# create an instance of UsersTemp from a dict
users_temp_form_dict = users_temp.from_dict(users_temp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


