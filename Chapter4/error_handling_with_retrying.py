from retrying import retry
import requests
#일시적인 오류를 나타내는 상태 코드를 지정합니다.
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)


def main():
    """
    메인 처리입니다.
    """
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print("Success!")
    else:
        print('Error!')


#stop_max_attempt_number로 최대 재시도 횟수를 지정합니다.
#wait_exponential_multiplier로 특정한 시간 만큼 대기하고 재시도하게 합니다. 단위는 밀리초
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def fetch(url):
    """
    지정한 URL에 요청한 뒤 Response 객체를 반환합니다.
    일시적인 오류가 발생하면 최대 3번 재시도합니다.
    """
    print('Retrieving {0}...'.format(url))
    response = requests.get(url)
    print('Status: {0}'.format(response.status_code))
    if response.status_code not in TEMPORARY_ERROR_CODES:
        #오류가 없다면 response를 반환합니다.
        return response

    #오류가 있다면 예외를 발생시킵니다.
    raise Exception('Temporary Error: {0}'.format(response.status_code))


if __name__ == '__main__':
    main()