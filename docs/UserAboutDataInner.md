# UserAboutDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** | User About. NOTE: About information is customizable by users through BBCode on MyAnimeList. This means users can add multimedia content, different text sizes, etc. Due to this freeform, Jikan returns parsed HTML. Validate on your end! | [optional] 

## Example

```python
from jikan_openapi.models.user_about_data_inner import UserAboutDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserAboutDataInner from a JSON string
user_about_data_inner_instance = UserAboutDataInner.from_json(json)
# print the JSON string representation of the object
print(UserAboutDataInner.to_json())

# convert the object into a dict
user_about_data_inner_dict = user_about_data_inner_instance.to_dict()
# create an instance of UserAboutDataInner from a dict
user_about_data_inner_form_dict = user_about_data_inner.from_dict(user_about_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


