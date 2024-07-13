sql_injection_patterns = [
        r"(\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bCREATE\b|\bALTER\b|\bDROP\b|\bTRUNCATE\b)",
        r"(\bCOMMIT\b|\bROLLBACK\b|\bSAVEPOINT\b|\bWHERE\b|\bFROM\b|\bINTO\b|\bJOIN\b|\bON\b|\bAND\b|\bOR\b|\bNOT\b)",
        r"(\bIN\b|\bLIKE\b|\bEXISTS\b|\bBETWEEN\b|\bCOUNT\b|\bSUM\b|\bAVG\b|\bMIN\b|\bMAX\b)",
        r"(\bORDER BY\b|\bGROUP BY\b|\bHAVING\b|\bCASE\b|\bWHEN\b|\bTHEN\b|\bELSE\b|\bEND\b)",
        r"(\bUNION\b|\bUNION ALL\b|\bINTERSECT\b|\bEXCEPT\b|\bEXEC\b|\bEXECUTE\b|\bSP_\b|\bCALL\b)",
        r"(--|\/\*|\*\/|')"
    ]