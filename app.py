import sys
import requests
import re

def args_correct():
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
        return False
    return True

def match_url(url):
    pattern = re.compile(r"(https?|ftp):\/\/([a-zA-Z0-9\-\.]+)(:[0-9]+)?(\/[^\s]*)?")
    
    if re.match(pattern, url):
        return True
    else:
        return False

def main():
    if not args_correct():
        print("Usage: python app.py <url> <print to file (Y, n, yes, no, true, false)>")
        return 1
        
    if not match_url(sys.argv[1]):
        print(f"Your entered URL appears to be in a wrong format!\nYour input: {sys.argv[1]}")
        return 1
        
    url = sys.argv[1]
    
    arg2 = ["n", "no", "false"]
    save_to_file = True
    
    if len(sys.argv) == 3 and sys.argv[2].lower() in arg2:
        save_to_file = False

    try:
        res = requests.get(url)
    except Exception:
        print(f"Error occured while fetching URL. Please double check that you entered the correct URL!\nYour input: {url}")
        return 1  
        
    print(f"{res.text}")
    
    if save_to_file == True:
        with open("output.html", "w+") as out:
            out.write(res.text)
            print("Saved output in output.html")

    return 0

if __name__ == "__main__":
    sys.exit(main())