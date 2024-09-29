# UserImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jpg** | [**UserImagesJpg**](UserImagesJpg.md) |  | [optional] 
**webp** | [**UserImagesWebp**](UserImagesWebp.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_images import UserImages

# TODO update the JSON string below
json = "{}"
# create an instance of UserImages from a JSON string
user_images_instance = UserImages.from_json(json)
# print the JSON string representation of the object
print(UserImages.to_json())

# convert the object into a dict
user_images_dict = user_images_instance.to_dict()
# create an instance of UserImages from a dict
user_images_form_dict = user_images.from_dict(user_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


