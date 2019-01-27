# blogging-app

### This application was created for a take home test from smallcloud technologies

the model of this app is:

###### Post
  * Title
  * author - linked by foreign key
  * description/post body
  * creation date
###### Author
  * name
  * bio
  
###### Site functionality:
* index - contains a list of the posts, as well as a list of the authors so that each can be individually viewed
* specific post - contains the information about the created post
* create page - contains a simple form that allows you to create a blog post
* edit page - contains the same form as the create page, however the fields are pre-filled with the posts current data
* author's bio - contains the information about the individual author
* it is styled with both an internal style-sheet and using various bootstrap classes

###### short-comings

* lack of familiarity with django and github means I may have uploaded too many files, however I did keep the .pyc files out
* I'm not a a good graphic designer, and so the site is functional, but not very pretty
