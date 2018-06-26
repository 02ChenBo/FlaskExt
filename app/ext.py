from flask import Flask
from flask_caching import Cache
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import  SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, patch_request_class, IMAGES

db=SQLAlchemy()
migrate=Migrate()
def init_ext(app:Flask):
    init_db_config(app)
    # 初始化缓存配置
    inin_cache_config(app)
    # 初始化用户管理模块
    init_login_config(app)
    # 初始化文件上传配置
    init_upload_config(app)

def init_db_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskext'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 配置秘钥
    app.config['SECRET_KEY']='123456'
    db.init_app(app)
    migrate.init_app(app, db)

cache=Cache()
# 缓存配置
def inin_cache_config(app):
    cache.init_app(app,config={
        'CACHE_DEFAULT_TIMEOUT':60,
        'CACHE_TYPE':'redis',
        'CACHE_REDIS_HOST':'127.0.0.1',
        'CACHE_REDIS_PORT':6379,
        # 'CACHE_REDIS_PASSWORD':'123456',
        # 连接数据库的编号
        'CACHE_REDIS_DB':1,
        # 缓存的前缀
        'CACHE_KEY_PREFIX':'view_',
    })



# 用户模块插件   登录注册
login_manager=LoginManager()
def init_login_config(app):
    # 当用户点击某个需要登录才能访问的界面的时候
    # 如果没有登录就会自动跳转相应的视图函数   必须配
    login_manager.login_view='login'
    login_manager.login_message='必须登录才能访问'
    login_manager.init_app(app)

'''
文件上传配置
参数：
name :保存文件的子目录  默认是files
extensions 允许上传文件的类型
default_dest 设置文件上传的根路径
'''
images=UploadSet(name='images',extensions=IMAGES,default_dest=None)
import  os
'''
配置
1>配置上传文件的根目录
'''
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT_PATH=os.path.join(BASE_DIR,'static/upload')
def init_upload_config(app):
    # 配置上传根目录
    app.config['UPLOADS_DEFAULT_DEST']=UPLOAD_ROOT_PATH
    # 生成文件的访问url地址
    app.config['UPLOADS_DEFAULT_URL']='/static/upload/'
    '''
    app Flask对象
    uploads_sets  文件上传核心类 UploadSet
    '''
    configure_uploads(app=app,upload_sets=images)
    patch_request_class(app=app,size=32*1024*1024)
