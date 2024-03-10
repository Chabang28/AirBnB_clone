
All errors are printed in `STDERR`

Return:
Exit status is the # of errors, 0 on Success
"""
import sys
import requests
import os


def print_stdout(msg):
    """Print message in STDOUT
    """
    sys.stdout.buffer.write(msg.encode('utf-8'))


def print_stderr(msg):
    """Print message in STDERR
    """
    sys.stderr.buffer.write(msg.encode('utf-8'))


def is_empty(file):
    if os.path.getsize(file) == 0:
        raise OSError(f"File '{file}' is empty.")


def validate(file_path, type):
    """
    Start validation of files
    """
    headers = {'Content-Type': f"{type}; charset=utf-8"}
    data = open(file_path, "rb").read()
    url = "https://validator.w3.org/nu/?out=json"
    response = requests.post(url, headers=headers, data=data)

    if not response.status_code < 400:
        raise ConnectionError("Unable to connect to API endpoint.")

    result = []
    messages = response.json().get('messages', [])
    for message in messages:
        if message['type'] in ['error', 'info']:
            result.append(f"'{file_path}' => {message['message']}")
        else:
            result.append(f"[{file_path}:{message['lastLine']}] {message['message']}")
    return result


def analyse(file_path):
    """Start analyse of a file and print the result
    """
    nb_errors = 0
    try:
        result = None

        if file_path.endswith(".css"):
            is_empty(file_path)
            result = validate(file_path, "text/css")
        elif file_path.endswith((".html", ".htm")):
            is_empty(file_path)
            result = validate(file_path, "text/html")
        elif file_path.endswith(".svg"):
            is_empty(file_path)
            result = validate(file_path, "image/svg+xml")
        else:
            allowed_files = "'.css', '.html', '.htm' and '.svg'"
            raise OSError(
                f"File {file_path} does not have a valid file extension.\nOnly {allowed_files} are allowed."
            )

        if len(result) > 0:
            for msg in result:
                print_stderr(f"{msg}\n")
                nb_errors += 1
        else:
            print_stdout(f"'{file_path}' => OK\n")

    except Exception as e:
        print_stderr(f"'{e.__class__.__name__}' => {e}\n")
    return nb_errors


def files_loop():
    """Loop that analyses for each file from input arguments
    """
    nb_errors = 0
    for file_path in sys.argv[1:]:
        nb_errors += analyse(file_path)

    return nb_errors


if __name__ == "__main__":
    """Main
    """
    if len(sys.argv) < 2:
        print_stderr("usage: w3c_validator.py file1 file2 ...\n")
        exit(1)

    """execute tests, then exit. Exit status = # of errors (0 on success)
    """
    sys.exit(files_loop())

