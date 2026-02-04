# 📘 User Guide: GitHub Username Hunter

This guide provides a deep dive into how the script functions, how to interpret the results, and how to maximize your chances of finding a rare handle.

---

## 🛠 Operation Workflow

The script follows a multi-stage validation process to ensure that "Available" usernames are actually claimable in real-time.

1. **Pattern Generation:** The script iterates through a pre-defined logic (e.g., CVCV patterns) to find pronounceable 4-character strings.
2. **API Handshake:** It sends a request to the GitHub API using your PAT to check for a `404 Not Found` status.
3. **Registration Validation:** If the API returns a 404, the script performs a secondary "Ghost Check" against GitHub's internal signup validator.
4. **Logging:** Validated names are appended to `claimable_names.txt` immediately to prevent data loss.

---

## 📈 Performance & Rate Limits

Your speed is determined by the type of authentication used. By using a **PAT (Classic)**, you are granted significantly higher bandwidth than a standard guest.

| Method | Rate Limit | Capacity |
| :--- | :--- | :--- |
| **Unauthenticated** | 60 requests / hour | Very Slow |
| **Personal Access Token** | 5,000 requests / hour | High Speed |
| **Search API** | 30 requests / minute | Specialized |



---

## ❓ Troubleshooting

### The script says "Available" but the website says "Taken"
This occurs when a username is in a **Reserved State**. This happens if:
* The name is a "System Word" (e.g., `info`, `support`, `meta`).
* The name was recently part of an organization or a trademarked entity.
* The name is blocked due to GitHub's internal safety filters.
* **Solution:** Ignore these; the script will mark them in Yellow if the secondary validator fails.

### I am getting a `403 Forbidden` error
This means you have either:
1. Hit your 5,000 requests-per-hour limit.
2. Your PAT has expired.
* **Solution:** The script will automatically pause for 403 errors. If it doesn't resume, regenerate your token in Developer Settings.

### The terminal is only showing Red
Don't panic! 4-character usernames are extremely competitive. 
* **Tip:** Try running the script at night or targeting patterns with numbers (e.g., `v2kx`) or rare letters (`x`, `z`, `q`, `j`).

---

## 🛑 How to Stop the Script
To safely exit the script at any time, press `Ctrl + C` in your terminal. All names already found in `claimable_names.txt` are automatically saved.
