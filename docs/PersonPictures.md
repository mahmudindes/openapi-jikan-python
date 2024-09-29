# PersonPictures

Character Pictures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PeopleImages]**](PeopleImages.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_pictures import PersonPictures

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPictures from a JSON string
person_pictures_instance = PersonPictures.from_json(json)
# print the JSON string representation of the object
print(PersonPictures.to_json())

# convert the object into a dict
person_pictures_dict = person_pictures_instance.to_dict()
# create an instance of PersonPictures from a dict
person_pictures_form_dict = person_pictures.from_dict(person_pictures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


