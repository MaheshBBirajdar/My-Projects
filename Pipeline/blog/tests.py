from django.test import TestCase

# Create your tests here.

'''
create API in django
1. The database should contain three tables named 
    a)User, b) Post and c) Like.
2. The User table should store user information such as  ID, name, email, password, and
other relevant details.

3. The Post/Blog table should store post/blog information such as  ID, title, description,
content, creation date, and other relevant details.

4. The Like table should store information about the likes of each post/blog, such as  ID,
post ID, user ID, and other relevant details.

5. The following CRUD APIs should be implemented for all three tables:
    a)  Create API: To add new user/post/like to the corresponding table.
    b) Read API: To retrieve a specific user/post/like from the corresponding table.
    c) Update API: To update the details of a specific user/post/like in the corresponding table.
    d) Delete API: To delete a specific user/post/like from the corresponding table.

6. The GET all post/blog API should also return the number of likes for each post/blog.

7. All APIs must adhere to the following rules:
    a) Access to the PUT/DELETE APIs for the Post table should be restricted to the owner of the post/blog.
    b) Any user can access the GET API for a post if it is public. For private posts, only the owner should be able to access them.
    c) There should be only one API endpoint for any given query. Retrieval of both the post and its likes should be completed within a single query.

'''