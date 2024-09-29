# AnimeImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jpg** | [**AnimeImagesJpg**](AnimeImagesJpg.md) |  | [optional] 
**webp** | [**AnimeImagesWebp**](AnimeImagesWebp.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_images import AnimeImages

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeImages from a JSON string
anime_images_instance = AnimeImages.from_json(json)
# print the JSON string representation of the object
print(AnimeImages.to_json())

# convert the object into a dict
anime_images_dict = anime_images_instance.to_dict()
# create an instance of AnimeImages from a dict
anime_images_form_dict = anime_images.from_dict(anime_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


