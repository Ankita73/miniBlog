# miniBlog

Blog using Django Rest on Nginx HTTP server.

User can create, edit, delete posts.
Also, one can comment and reply on the posts.

All end points can be tried by Postman

USER API
User Registration 
	POST http://127.0.0.1:8000/users/register/
	Request body:
	{
		"username" 	: "",
		"email" 	: "",
		"email2" 	: "",
		"password" 	: "",
		"first_name": "",
		"last_name" : ""
	}

Login and Authentication
	POST http://127.0.0.1:8000/users/login/
	POST http://127.0.0.1:8000/user/auth/token/
	Request body:
	{
		"username" : "",
		"password" : ""
	}


Blog Post API
Create
	POST http://127.0.0.1:8000/blog/create/
	headers : Authorization : JWT <token obtained for that user>
	Request body: 
	{
		"blogTitle"		: "",
		"blogContent"	: "",
		"bloggedDate"	: "",
	}

List
	GET http://127.0.0.1:8000/blog/

Edit
	PUT http://127.0.0.1:8000/blog/<blogid>/edit/
	headers : Authorization : JWT <token obtained for that user>
	Request body:
	{
		"blogTitle": "",
		"blogContent": "",
		"bloggedDate": "",
	}

Delete 
	DELETE http://127.0.0.1:8000/blog/4/delete/


Comments API
Create 
	POST http://127.0.0.1:8000/comments/create/?type=blog&blogId=<blogId>
Reply to a comment:
	POST http://127.0.0.1:8000/comments/create/?type=blog&blogId=<blogId>&parent_obj=<commentid>
Get a Comment
	GET http://127.0.0.1:8000/comments/<commentId>/
Delete a Comment
	DELETE http://127.0.0.1:8000/comments/<commentId>/



