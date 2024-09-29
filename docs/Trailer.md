# Trailer

Youtube Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**youtube_id** | **str** | YouTube ID | [optional] 
**url** | **str** | YouTube URL | [optional] 
**embed_url** | **str** | Parsed Embed URL | [optional] 
**images** | [**TrailerImagesImages**](TrailerImagesImages.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.trailer import Trailer

# TODO update the JSON string below
json = "{}"
# create an instance of Trailer from a JSON string
trailer_instance = Trailer.from_json(json)
# print the JSON string representation of the object
print(Trailer.to_json())

# convert the object into a dict
trailer_dict = trailer_instance.to_dict()
# create an instance of Trailer from a dict
trailer_form_dict = trailer.from_dict(trailer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


