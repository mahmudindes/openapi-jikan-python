# Person

Person Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**website_url** | **str** | Person&#39;s website URL | [optional] 
**images** | [**PeopleImages**](PeopleImages.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**given_name** | **str** | Given Name | [optional] 
**family_name** | **str** | Family Name | [optional] 
**alternate_names** | **List[str]** | Other Names | [optional] 
**birthday** | **str** | Birthday Date ISO8601 | [optional] 
**favorites** | **int** | Number of users who have favorited this entry | [optional] 
**about** | **str** | Biography | [optional] 

## Example

```python
from jikan_openapi.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_form_dict = person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


