"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either pangram or not pangram as appropriate.

Example:
s = "We promptly judged antique ivory buckles for the next prize"
The string contains all letters in the English alphabet, so return pangram.

"""

def pangram(s:str):
    char_s = s.replace(" ", "")
    result = set()
    for char in char_s.lower():
        result.add(char)
    
    if len(result) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    s = "We promptly judged antique ivory buckles for the next prize"
    s2 = "We promptly judged antique ivory buckles for the prize"
    s3 = "WwmdRukNYPMFBxYFPVtZrzs FAktokrLtdPyVRWCyqSHaqjttuhYNXpwnzwoXDC AdKRP AWwEamzQlOT EweNHXGkYrgJJwzErXvkiYIGOK goZXDYecGz oPHaxcZZC Z ktcXTnPFeuPQgQqoJS LZtk nOA zXc QyDseEIHVueKlgZVcQhgc hNHCQJS NXqvz EIOrqfPcBaXHDmWCHKMufyLXBQPVROdnlWDICRO qUNaVNP I fJAoEK saAnGbE pXvQW nd bitUAdJoIkbhPkwiKVUxpgV NsDCpwztiCXliMHrOEicnEsVc uIiai hLRqwFVeeHQzXXqVgUmNcqc TdHCztGUXwnzFGIPdYNZhfFKPQuUI ynSWARRzzwlRlzL JxsljNx YGfagQnP g VMImbbBNiOjNqtFb ODtQK DxNIfqggIzXgP eGMS kcnelJ kOTAG tSwcSlyMp xVjLZigPdsR yilXJyDa SKGOj yWEROeKfnPE iSFZwHPj ZPwKdllGxEdtpKwTMcB Yuus JgyWdYHj snl HrFqRgVDgVPAh X PBRAkR EwpdMYrlgI QKUnRBfKLwV yXKKGbMkIRIYN dqzaYvIQM vt yvuaGntYHEgEJb TNoPvslu htYlZXayqTlcNclvSOoMyfiTWehzhs W wanyMaAYijgxubvDINMlqHblbjLSJCvCpfvqaWHy qwG lLciwkkuu o NoSTWbytadyGuTRznISvCQhFMtrdqveTmcc mcKNPGowUGBLPmONplkUwZeu N p apQLbHLFSIt vkOcFlSMYZdaZy PzfbRPLTHy gAFo PLRItTAOfuWITfyIzUBc F GEXzyMZHXRpnpxQ NV Cl PIBRgkNNKQTVgGkTNbojQqm VvomeAxXDppIWm I KqyX CTA nt JTSsOH M mKzfGwsT LjXPVYzcJFdVWqkFRNm"
    print(pangram(s))
    print(pangram(s2))
    print(pangram(s3))
