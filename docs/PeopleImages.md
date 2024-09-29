# PeopleImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jpg** | [**UserImagesJpg**](UserImagesJpg.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.people_images import PeopleImages

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleImages from a JSON string
people_images_instance = PeopleImages.from_json(json)
# print the JSON string representation of the object
print(PeopleImages.to_json())

# convert the object into a dict
people_images_dict = people_images_instance.to_dict()
# create an instance of PeopleImages from a dict
people_images_form_dict = people_images.from_dict(people_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


