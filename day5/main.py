
def load_rules():
    returnvalue = []
    with open("rules.txt", 'r', encoding='utf-8') as rules:
        for rule in rules:
            returnvalue.append(rule.strip().split("|"))
    return returnvalue

def load_proposals():
    returnvalue = []
    with open("data.txt", 'r', encoding='utf-8') as proposals:
        for proposal in proposals:
            returnvalue.append(proposal.strip())
    return returnvalue

def isValid(proposal, rules):
    for rule in rules:
        a = proposal.find(rule[0])
        b = proposal.find(rule[1])
        if a >= 0 and b >= 0:
            if a >= b:
                failed_rules.append(rule)
                return False
    return True

failed_rules = []
proposals = load_proposals()
rules = load_rules()
valid_sum = 0
proposals_to_fix = []
fixed_sum = 0

for proposal in proposals:
    if isValid(proposal, rules):
        prop = proposal.split(',')
        prop_length = len(prop)
        index = int(prop_length / 2) + (prop_length % 2) - 1
        valid_sum = valid_sum + int(prop[index])
    else:
        proposals_to_fix.append(proposal.strip().split(','))
    
print(f"Sum of valid middle-pages: {valid_sum}")

for p in proposals_to_fix:
    while not isValid(",".join(map(str, p)), rules):
        for x in range(0,len(p)):
            for y in range(0,len(p)):
                if x != y:
                    for rule in failed_rules:
                        if p[x] == rule[0] and p[y] == rule[1]:
                            if x > y:
                                z = p[y]
                                p[y] = p[x]
                                p[x] = z
    prop_length = len(p)
    index = int(prop_length / 2) + (prop_length % 2) - 1
    fixed_sum = fixed_sum + int(p[index])

print(f"Sum of fixed proposals: {fixed_sum}")