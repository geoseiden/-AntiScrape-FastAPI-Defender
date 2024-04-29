import requests

def trigger_behavioral_analysis():
    url = "http://localhost:8000/login"
    user_agent_string = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/100.0.4896.75 Safari/537.36"
    data = {
        "user_agent": user_agent_string,
        "email":""
    }
    response = requests.post(url, json=data)
    print(response.text)

def trigger_honeypot():
    url = "http://localhost:8000/login"
    user_agent_string = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    honeypot_field_value = "some_fake_email@example.com"  # Provide a value for the honeypot field
    data = {
        "user_agent": user_agent_string,
        "email": honeypot_field_value
    }
    response = requests.post(url, json=data)
    print(response.text)

while True:
        print("Select an action:")
        print("1. Trigger Behavioral Analysis")
        print("2. Trigger Honeypot")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            trigger_behavioral_analysis()
        elif choice == "2":
            trigger_honeypot()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
