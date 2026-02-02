# Remove Duplicates from a List (Preserve Order)
def remove_dups_str(strs):
   result = []
   for  str in strs:
        if str not in result:
           result.append(str)
   return result

def remove_dups_int(ints):
   result = []
   seen = set()
   for  i in ints:
        if i not in seen:
           seen.add(i)
           result.append(i)
   return result
print(remove_dups_str(["ai", "gpt", "grok", "china", "deep", "ai", "ai"]))
print(remove_dups_int([1, 2, 3, 4, 5, 1, 2]))