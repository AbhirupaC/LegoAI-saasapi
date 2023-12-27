from src.rules.RulesABC import RulesABC

def run(df, config = []):
    ruleSummary = {}
    for rule in config["rules"]:
        inst = RulesABC(df, rule["ruleName"].lower(), rule["params"] )
        res = inst.getSummary()
        ruleSummary[rule["ruleAliasName"]] = res  
    return ruleSummary
