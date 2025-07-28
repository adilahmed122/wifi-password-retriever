# ✅ Step 1: নতুন ফোল্ডার তৈরি করে তাতে ঢোকো
mkdir wifi-password-retriever
cd wifi-password-retriever

# ✅ Step 2: স্ক্রিপ্ট ফাইল তৈরি করো (তোমার কোড এখানে থাকবে)
touch wifi_passwords.py
code wifi_passwords.py
# অথবা নিচে আমি তোমার কোডও দিতে পারি একসাথে

# ✅ Step 3: requirements.txt তৈরি করো
echo "pyfiglet" > requirements.txt
echo "tabulate" >> requirements.txt

# ✅ Step 4: README.md তৈরি করো
echo "# Wi-Fi Password Retriever" > README.md
echo "Retrieve saved Wi-Fi passwords using netsh (Windows only)." >> README.md

# ✅ Step 5: Git ইনিশিয়ালাইজ করো
git init

# ✅ Step 6: Remote Repo যুক্ত করো (তোমার ইউজারনেম সহ)
git remote add origin https://github.com/adilahmed12/wifi-password-retriever.git

# ✅ Step 7: সব ফাইল অ্যাড করো
git add .

# ✅ Step 8: কমিট করো
git commit -m "Initial commit"

# ✅ Step 9: GitHub এ push করো
git push -u origin master
