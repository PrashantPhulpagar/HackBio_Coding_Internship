def hamming_distance(str1, str2):
    length = max(len(str1), len(str2))
    str1 = str1.ljust(length, '_')  # Pad with underscores if needed
    str2 = str2.ljust(length, '_')
    
    return sum(1 for i in range(length) if str1[i] != str2[i])

# **Example Run:**
slack_username = "bio_prashant"
twitter_handle = "python_genomics"

distance = hamming_distance(slack_username, twitter_handle)
print("Hamming Distance:", distance)
