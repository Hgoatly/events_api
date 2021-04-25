# events_api

- Events API assessment task for the Buzzhire Backend Assessment

## Frameworks Used:

This API was built using the Django Rest Framework [Django Rest Framework](https://www.django-rest-framework.org/). The Django Rest Framework uses SQLite as a built in database.

### Required Features:

It includes the following endpoints: 

1. GET /api/events/
- Which returns a list of events

2. GET /api/events/:id/
- Which returns a specific event. This can be reached by clicking on the URL field on an individual event. 

3. POST /api/events/
- The 'events' URL comes with a built in form to enable the user to post new events to the built in database.

### Additional Features

In addition to the required features for the task, this API has the following additional features:

1. DELETE: Events can be deleted from the database from the /api/events/:id/ endpoint via the delete button.

2. UPDATE: Event instances in the dtabase can be updated from the /api/events/:id/ via the form at the bottom of the page. 

3. COMMENTS: A 'comments' field has been added in order for the user to be able to add any extra relevant information to the event instance. It is an optional field.



