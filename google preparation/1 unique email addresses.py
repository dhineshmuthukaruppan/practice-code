
from typing import List


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

# print('emails', emails)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_obj = {}
        for i in range(len(emails)):  
            email = emails[i]   

            domain_name = email.split('@')[1]; 
            localname_first_half = "".join(email.split('@')[0].split('+')[0].split('.')); 

            if localname_first_half + '@' + domain_name not in email_obj:
                email_obj[localname_first_half + '@' + domain_name] = 1
            else:
                email_obj[localname_first_half + '@' + domain_name]+=1; 

        count = 0; 
        for k,v in email_obj.items():
            count += 1;        

        return count
        

sol = Solution()

count = sol.numUniqueEmails(emails)   

print(count)  