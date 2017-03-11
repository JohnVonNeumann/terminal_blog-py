# terminal_blog-py

* Just went through list comprehension, which is something I've been lacking personal understanding in for a while now so it was good to be able to have an explanation of how to do it. I'm gonna have to give it a crack in some of my selenium test and see if I can get it to read from some text files or something in order to find all instances and do mass tests recursively.

* So when you declare a new class, you pass it the param (object) right? Well I looked up why we do that, and it seems like in Py3 it can be omitted but in Py2 it's not wise too. It basically tells our program that we wish to inherit all Object methods from standard lib. So as long as the parent class inherits from object, you are sweet. It is said to be good practice to just continue to keep it in there regardless of what is going on. But perhaps you can pass object to the parent then for all other you obviously just inherit the parent, not object.

* It's funny that you can learn something ages ago then it takes months until the idea's actually click in your head properly. So in regards to the Database file created, It is an onject that inherits from object but we don't spawn numerous instances of it, therefore we will never go near it with the self method. Hence why we add the @staticmethod tag.

* I think I was potentially getting tired of the way I was building this stuff yesterday, I wasn't really challenging myself with it, so today I've refreshed and I will be seeing what we are doing in each video before building it myself then checking if I've done it correctly. Like in my ML stuff.

* Debated over implementig uuid1 or uuid4 for my application and after some doc reading and a forum post (http://stackoverflow.com/questions/1785503/when-should-i-use-uuid-uuid1-vs-uuid-uuid4-in-python#1785592) it seems 1 is fine to go with unless there is a specific reason not too.

* So turns out I was wrong about uuid1 vs uuid4, we should use uuid4 for this particular application because with uuid1 you take in info about the host and time, therefore, you would be getting very similar ID's. Although to be fair, 1 has a marginal chance of collision so it really wouldn't matter.

* My implementation of the blog_id is incorrect, so I want persistent blog_id's so that if say, Joe Bloggs has a blog, he always has the same blog_id, that way, searches can be run against the blog_id and all posts can be returned, I think I can do this with uuid, so perhaps i create a uuid using author name as the hash seed, ill give it a crack.

* Fixed up the blog_id search and created a persistent blog_id that is built from author param input on the build of a new post class instance. And it works!