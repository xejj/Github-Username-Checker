# 🔍 GitHub Username Checker

A high-performance Python script designed to find rare 4-character GitHub handles. It uses the GitHub API to verify availability and double-checks against the registration validator to filter out "ghost" usernames.

## 🚀 Features
* **Double Verification:** Checks both API status and registration availability.
* **Auto-Saving:** Automatically exports claimable names to `claimable_names.txt`.
* **Visual Feedback:** Color-coded terminal output for real-time monitoring.
* **Rate Limit Handling:** Built-in logic to pause when GitHub's API limit is reached.

## 🚦 Output Key
| Color | Meaning |
| :--- | :--- |
| 🟨 **Yellow** | **Restricted:** Recently deleted, deactivated, or flagged. (Cannot be claimed) |
| 🟥 **Red** | **Unavailable:** The account is active and the name is taken. |
| 🟩 **Green** | **Available!** The name is free to use and saved to your text file. |

---

## 🛠️ Setup & Requirements

### 1. Prerequisites
Ensure you have Python installed and the required library:
```bash
pip install requests termcolor
