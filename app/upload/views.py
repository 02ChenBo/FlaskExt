from flask import Blueprint, request, render_template, jsonify
from app.ext import images
from app.utils.image_utils import get_new_image_name

upload_blue = Blueprint('upload', __name__)
"""
必须是post请求  form-data

"""
"""
UploadSet
save
参数说明
1>文件对象
2>


"""


#
@upload_blue.route('/img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        files = request.files.getlist('files')
        urls = []
        for image in files:
            file_name = images.save(image, name=get_new_image_name(image.filename))
            url = images.url(file_name)
            urls.append(url)
        # 生成可以访问的路径
        # /static/upload/images/xxx.png
        return jsonify({'msg': 'success', 'status': 200, 'url': urls})
        # 文件上传对象  字典
    elif request.method == 'GET':
        return render_template('upload.html')





