from django.shortcuts import render
import logging

logging = logging.getLogger('cloud.webconsole')


# 跳转到登录页面
def show_login(request):
    request.session['project_name'] = 'cloud'  # session 设置
    return render(request, "login.html")


# 用户登录
def login(request):
    logging.debug("--------------login view is invoke!")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = username
        # TODO 验证用户信息
        logging.debug("user_name:" + username + " -----------passwd:" + password)
    # context = {'username': username, 'password': password}
    return render(request, "index.html", {'menu_json_str': '123'})


# 注销
def log_out(request):
    if request.session['username'] != '':
        del request.session['username']
    return render(request, 'login.html')
