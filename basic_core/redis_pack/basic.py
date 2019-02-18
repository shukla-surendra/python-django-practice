import redis

r = redis.Redis(host='localhost', port=6379)
r.set('foo',"bar")
print(r.get ('foo'))
# storing dictionary in redis
user = {'name':"Surendra", "age":25, "designation":"Software Engineer"}
r.hmset('dictionary', user)
# print(r.hmget('dictionary')) # error in getting values
