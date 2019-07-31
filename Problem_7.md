
#Problem 7: Request Routing in a Web Server with a Trie

In the main Router, I initialize my routes with a RouteTrie, adding a "/" root route and our default `not found` route handler. To add a handler or lookup a route, we simply call on the familiar functions of RouteTrie `insert` and `find` passing a list of paths already split by the backslash ("/").

The time complexity is O(n) , because ??????????

The space complexity is O(n), because of the list
