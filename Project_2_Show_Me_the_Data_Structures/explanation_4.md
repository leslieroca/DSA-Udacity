"Active Directory"

Explanation:

To solve the Active Directory problem I looped through the contained groups in the original group, calling the
"is_user_in_group" function recursively passing each contained group looking for the target user.


Complexity:
The run time complexity is O(n*m) where n is the number of groups and m the number of users in each group.

The space complexity is constant O(n) where n is the number of groups which is the maximum size of the recursion stack