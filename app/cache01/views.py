from flask import Blueprint, render_template

from app.ext import cache

cache_blue=Blueprint('cache',__name__,template_folder='templates')



'''
timeout  过期时间
key_prefix='view_%s'  缓存key的前缀
@cache.cached  不支持带参数
'''



@cache_blue.route('/1/')
@cache.cached(timeout=60,key_prefix='view_%s')
def test():
    print('222')
    return '22'


'''
@cache.memoize(timeout=60,make_name=,unless=None)
make_name  是一个函数  返回string类型 默认情况将函数名作为key缓存起来
@cache.memoize  支持带参数的函数    
'''
@cache_blue.route('/2/<name>')
@cache.memoize(timeout=60*60)
def test2(name):
    print(name)
    return '111'


@cache_blue.route('/3/')
def test3():
    msg='11111'
    return render_template('cache1.html',msg=msg)


