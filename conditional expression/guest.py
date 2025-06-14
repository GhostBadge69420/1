user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)