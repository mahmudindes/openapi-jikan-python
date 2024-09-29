# UserAbout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserAboutDataInner]**](UserAboutDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_about import UserAbout

# TODO update the JSON string below
json = "{}"
# create an instance of UserAbout from a JSON string
user_about_instance = UserAbout.from_json(json)
# print the JSON string representation of the object
print(UserAbout.to_json())

# convert the object into a dict
user_about_dict = user_about_instance.to_dict()
# create an instance of UserAbout from a dict
user_about_form_dict = user_about.from_dict(user_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


