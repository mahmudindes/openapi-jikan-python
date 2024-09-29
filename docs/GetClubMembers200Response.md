# GetClubMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[ClubMemberDataInner]**](ClubMemberDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_club_members200_response import GetClubMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClubMembers200Response from a JSON string
get_club_members200_response_instance = GetClubMembers200Response.from_json(json)
# print the JSON string representation of the object
print(GetClubMembers200Response.to_json())

# convert the object into a dict
get_club_members200_response_dict = get_club_members200_response_instance.to_dict()
# create an instance of GetClubMembers200Response from a dict
get_club_members200_response_form_dict = get_club_members200_response.from_dict(get_club_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


