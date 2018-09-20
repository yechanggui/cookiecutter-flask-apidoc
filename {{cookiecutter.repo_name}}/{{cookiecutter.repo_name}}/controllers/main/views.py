# coding: utf-8
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from {{cookiecutter.repo_name}}.extensions import cache
from {{cookiecutter.repo_name}}.forms import LoginForm
from {{cookiecutter.repo_name}}.models import User
from {{cookiecutter.repo_name}}.controllers.main import main



@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200


@main.route('/apidoc', methods=['POST', 'GET'])
def index():
    """
    @api {post} /api/v1.0/apidoc
    @apiVersion 1.0.0
    @apiName register_user
    @apiGroup APIDOC
    @apiParam {String}  mobile      (必须)    用户手机号
    @apiParam {String}  password    (必须)    用户密码
    @apiParam {String}  sms_code    (必须)    用户短信验证码
    @apiParamExample {json} Request-Example:
        {
            mobile: "13970512239",
            password: "123456",
            sms_code: "907896"
        }

    @apiSuccess (回参) {int} user_id  用户注册id
    @apiSuccess (回参) {String} name  用户昵称
    @apiSuccess (回参) {String} mobile  用户注册手机号
    @apiSuccess (回参) {String} avatar  用户头像地址
    @apiSuccess (回参) {String} create_time  用户创建时间
    @apiSuccessExample {json} Success-Response:
        {
            "errno":0,
            "errmsg":"注册成功！",
            "data": {
                "user_id": 1,
                "name": "lynnyq",
                "mobile": "13813888888",
                "avatar": "http://p3ifu3dwc.bkt.clouddn.com/FjuAwxmcCtiud_nOZ",
                "create_time": "2010-1-1 12:12:12"

            }
        }

    @apiErrorExample {json} Error-Response:
        {
            "errno":4001,
            "errmsg":"数据库查询错误！"
        }

    """
    return 'It is a api sample'
