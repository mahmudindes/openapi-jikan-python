# UserById

User Meta By ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | MyAnimeList URL | [optional] 
**username** | **str** | MyAnimeList Username | [optional] 

## Example

```python
from jikan_openapi.models.user_by_id import UserById

# TODO update the JSON string below
json = "{}"
# create an instance of UserById from a JSON string
user_by_id_instance = UserById.from_json(json)
# print the JSON string representation of the object
print(UserById.to_json())

# convert the object into a dict
user_by_id_dict = user_by_id_instance.to_dict()
# create an instance of UserById from a dict
user_by_id_form_dict = user_by_id.from_dict(user_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


