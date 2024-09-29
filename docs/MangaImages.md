# MangaImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jpg** | [**AnimeImagesJpg**](AnimeImagesJpg.md) |  | [optional] 
**webp** | [**AnimeImagesWebp**](AnimeImagesWebp.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_images import MangaImages

# TODO update the JSON string below
json = "{}"
# create an instance of MangaImages from a JSON string
manga_images_instance = MangaImages.from_json(json)
# print the JSON string representation of the object
print(MangaImages.to_json())

# convert the object into a dict
manga_images_dict = manga_images_instance.to_dict()
# create an instance of MangaImages from a dict
manga_images_form_dict = manga_images.from_dict(manga_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


