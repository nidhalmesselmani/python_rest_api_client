
import time
import requests

def create_session():
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json"
    })
    

    def api_calls(r, *args, **kwargs):
        calls_left = r.headers['X-Ratelimit-Remaining']
        print(calls_left)
        if calls_left == 1:
            print('limit close, sleeping')
            time.sleep(5)

    s.hooks["response"] = api_calls
    return s

def main():
    sess = create_session()

    resp = sess.get("https://jsonplaceholder.typicode.com/todos")



if __name__ == '__main__':
    main()