# Self-Assess Your Django Competencies

## 🐟 Tuna Piano API

This API enables developers to create applications that provide song recommendations based on genre. It manages non-user specific data, including artists, their songs, and the associated genre for each song.

Let's make millions! 💰 💰 💰

### Setup

1. Clone the template repository.
2. Navigate to the created directory using `cd`.
3. Activate the Pipenv environment with `pipenv shell`.
4. Install the dependencies using `pipenv install`.
5. Open the project in Visual Studio Code.
6. Ensure that the correct interpreter is selected.
7. Implement the code.

### MVP Routes by Entity

These are all the available routes for this API. Each route has an associated ticket containing the following information:
- Route description.
- Request structure:
    - HTTP method.
    - Route path.
    - JSON body (if applicable).
- Response structure:
    - JSON body (if applicable).
    - Status code.

#### 🎶 Songs

- [Create a Song](./documentation/issue-tickets/Create-Song.md)
- [Delete a Song](./documentation/issue-tickets/Delete-Song.md)
- [Update a Song](./documentation/issue-tickets/Update-Song.md)
- [View a List of all the Songs](./documentation/issue-tickets/List-Songs.md)
- [Details view of a single Song and its associated genres and artist details](./documentation/issue-tickets/Details-Song.md)

#### 👩🏾‍🎤 Artists

- [Create an Artist](./documentation/issue-tickets/Create-an-Artist.md)
- [Delete an Artist](./documentation/issue-tickets/Delete-an-Artist.md)
- [Update an Artist](./documentation/issue-tickets/Update-an-Artist.md)
- [View a List of all the Artists](./documentation/issue-tickets/List-Artists.md)
- [Details view of a single Artist and the songs associated with them](./documentation/issue-tickets/Details-Artist.md)

#### 🎸 Genres

- [Create a Genre](./documentation/issue-tickets/Create-Genre.md)
- [Delete a Genre](./documentation/issue-tickets/Delete-Genre.md)
- [Update a Genre](./documentation/issue-tickets/Update-Genre.md)
- [View a List of all the Genres](./documentation/issue-tickets/List-Genres.md)
- [Details view of a single Genre and the songs associated with it](./documentation/issue-tickets/Details-Genre.md)

### Stretch Goals

These are examples of stretch goals that you can tackle once you have been MVP approved for the above features!

- Plan and Build the Frontend for the MVP routes
- [Popular genres: Retrieve a list of genres based on the number of associated songs](./documentation/issue-tickets/Popular-genres.md)
- [Related artists: Retrieve artists with similar genres](./documentation/issue-tickets/Related-artists.md)
- [Search songs by genre](./documentation/issue-tickets/Search-songs-by-genre.md)
- [Search artists by genre](./documentation/issue-tickets/Search-artists.md)
- Search all entities by (name/title/description)

## Data Design

![ERD Picture](https://github.com/TrinityChristiana/django-api-assessment/assets/31781724/a39bab27-bc1e-4a42-9ecc-ab96130bb509)
- [Link to ERD Docs](https://dbdocs.io/trinitycterry/Tuna-Piano-API?view=relationships)

To include the specific instructions for seeking help, you can update the "Seeking Help and Clarification" section as follows:

## Seeking Help and Clarification

If you encounter challenges or need clarification during the assessment, follow these steps:

1. Create a new discussion ticket in the [GitHub Discussions](https://github.com/orgs/nss-evening-web-development/discussions) repository, providing all the necessary details about your issue or question.
2. Include a clear and concise description of the problem, along with any relevant code snippets, error messages, or logs.
3. Specify the context of the problem, including the route or feature you are working on and any relevant dependencies.
4. Once you have created the discussion ticket, post a link to it in the Help Thread within your cohort's designated communication channel (e.g., Slack).
5. Be patient and allow time for the instructional team to review and respond to your ticket. They will provide guidance or clarification to help you move forward.

By following these steps, you can ensure that your questions and issues are properly documented and brought to the attention of the instructional team. This process helps streamline communication and allows the team to provide timely and targeted assistance to support your progress during the assessment.

## Best Practices for Code Organization and Implementation

Consider the following tips and best practices to ensure an organized and well-structured codebase:

- Follow the principles of separation of concerns and modularity, organizing code into logical components and modules.
- Adopt a consistent coding style and naming conventions to enhance readability and maintainability.
- Implement reusable functions or utility modules to avoid code duplication.
- Comment code sections that might require additional explanation or clarification.
- Properly document the API endpoints, including their purpose, expected inputs, and outputs.
