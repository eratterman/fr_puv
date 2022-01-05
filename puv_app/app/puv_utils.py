import datetime
import time
import redis


class Redis(object):
    """
    first need to start a redis server locally
    serving redis using 127.0.0.1:6379
    """
    def __init__(self, server='127.0.0.1', port='6379'):
        self.server = server
        self.port = port
        self.red = redis.Redis(host=self.server, port=self.port)

    def get_keys(self, pattern='*'):
        return self.red.keys(pattern=pattern)

    def get_type(self, key):
        return self.red.type(key)

    def get_val(self, key, **kwargs):
        key_type = kwargs.get('key_type', '')
        name = kwargs.get('name', '')
        offset = kwargs.get('offset', 1)
        beg_range = kwargs.get('start', '')
        end_range = kwargs.get('end', '')
        if key_type == 'str':
            return self.red.get(key)
        elif key_type == 'list':
            return self.red.lrange(key, 0, self.red.llen(key) + 1)
        elif key_type == 'bit':
            return self.red.getbit(name, offset)
        elif key_type == 'range':
            return self.red.getrange(key, beg_range, end_range)
        elif key_type == 'hash':
            return self.red.hget(name, key)
        else:
            print(f'type {key_type} is not supported')
            return None

    def set_val(self, key, val):
        return self.red.set(key, val)

    def del_key(self, key):
        return self.red.delete(key)

    def flush(self, asynchronous=False):
        return self.red.flushall(asynchronous=asynchronous)

    def __repr__(self):
        return f'<redis object: {self.server} on {self.port}>'


if __name__ == '__main__':
    bt = time.perf_counter()

    red = Redis(server='127.0.0.1', port='6379')
    print(red.get_keys())
    # print(red.get_type('_kombu.binding.celery'))
    # # print(red.get_val('_kombu.binding.celery', key_type='str'))
    # print(red.get_val('celery', key_type='list'))
    # print(red.del_key('my_key'))
    print(red)
    date = datetime.datetime.timedelta(days=2)

    et = time.perf_counter()
    print(round(et - bt, 2))
