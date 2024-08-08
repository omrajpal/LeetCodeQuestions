class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = {}
        for i in range(len(cpdomains)):
            cpdomains[i] = cpdomains[i].split(" ")
            cpdomains[i][0] = int(cpdomains[i][0])

            cpdomains[i][1] = cpdomains[i][1].split(".")
            curr = ""
            for j in range(len(cpdomains[i][1])):
                curr = ".".join(cpdomains[i][1][j:])
                count[curr] = count.get(curr, 0) + cpdomains[i][0]
            
        return ["{} {}".format(visits, domain) for domain, visits in count.items()]

        