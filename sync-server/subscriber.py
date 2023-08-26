# subscriber.py
import redis
import time

# Redis URL을 redis_url = "redis://redis:6379"를 사용해야 하는 이유

# Redis URL을 http://localhost:6379를 사용하면 컨테이너 내부에서 Redis 서버에 연결하려고 시도합니다. Docker Compose를 사용하면 각 서비스는 고유한 네트워크 이름 공간 내에서 실행되므로, "localhost"는 컨테이너 자체를 가리킵니다. 따라서 컨테이너 내에서 실행되는 코드가 "localhost"의 6379 포트로 연결하려고 하면, 해당 컨테이너 내에서 실행되는 Redis 인스턴스를 찾으려고 시도하게 됩니다. 해당 컨테이너 내부에는 Redis 서버가 없으므로 연결은 실패합니다.

# Docker Compose 파일에서 서비스 이름을 사용하면 해당 서비스의 컨테이너로의 연결을 설정할 수 있습니다. 위에서 제공한 Docker Compose 파일 예제에서는 Redis 서비스의 이름이 "redis"이므로, 연결 문자열을 다음과 같이 변경해야 합니다:

# redis_url = "redis://redis:6379/0"

# 위 코드는 Redis 서비스의 이름을 "redis"로 사용하며, 동일한 Docker Compose 네트워크 내에서는 해당 서비스의 컨테이너로의 연결을 설정합니다. 이렇게 하면 컨테이너 내부에서 실행되는 코드가 Redis 서비스의 컨테이너로 올바르게 연결됩니다.
r = redis.Redis(host="redis", port=6379, db=0)

p = r.pubsub()

p.subscribe("my-channel-1")

while True:
    message = p.get_message()
    if message:
        # Python에서 print 함수를 사용할 때 flush=True를 설정하면, 출력 버퍼가 즉시 비워지고 출력된 문자열이 표준 출력 스트림에 즉시 보내집니다. 그렇지 않으면, 출력된 문자열은 버퍼링되어 나중에 스트림에 보내지거나, 프로그램이 종료될 때 또는 버퍼가 꽉 찰 때 비워질 수 있습니다. Docker 컨테이너 내에서 실행되는 Python 스크립트는 터미널이 아닌 다른 출력 스트림에 연결되기 때문에, 출력이 버퍼링되어 즉시 표시되지 않을 수 있습니다. flush=True를 사용하면, 출력된 문자열이 즉시 스트림에 보내져 Docker 로그로 캡처되므로 로그가 터미널에 즉시 표시됩니다. 간단히 말해서, flush=True는 출력을 즉시 보내야 할 때 유용합니다. 특히 실시간 로깅이 필요한 상황, 예를 들어 Docker와 같은 컨테이너 환경에서 실행되는 경우에 해당합니다.
        print(f"received messeage : {message}", flush=True)
    time.sleep(0.01)
