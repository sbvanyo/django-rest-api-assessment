# Update an existing genre

## Description
This ticket requests the implementation of a route that allows updating an existing genre.

## Request
- **Method:** PUT
- **Path:** /genres/{genreId}
- **Body**
  ```json
  {
    "description": "Updated Genre Description"
  }
  ```

## Response
- **Status Code:** 204 No Content