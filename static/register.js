function bindEmailCodeClick(){
    // id选择器
    $("#send-code").click(function(event){
        //  butten按钮实在form表单中的,有些浏览器会在点击button是默认提交表单
        //  在这里阻止其默认行为
        event.preventDefault();

        // 将当前button转换成jquery对象
        let that = $(this);

        // 1. 获取用户输入的邮箱
        let email = $("#reg-email").val();
        let emailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        //  测试邮箱是否合法
        if(!emailReg.test(email)){
            alert("请输入合法的邮箱！");
            return;
        }

        // 2. 倒计时的过程中，取消点击事件
        that.off('click');

        // 3. 倒计时
        let countdown = 6;
        // 修改button标签的文本,that是jqery的button对象
        that.text(countdown+"s");
        let timer = setInterval(function(){
            countdown -= 1;
            that.text(countdown+"s");
            if(countdown <= 0){
                that.text("获取验证码");
                // 删除定时器
                clearInterval(timer);
                // 重新绑定点击事件
                bindEmailCodeClick();
            }
        }, 1000);

        // 4. 发送ajax请求
        $.get({
            url: "/email/code",
            data: {"email": email},
            success: function (result){
                console.log(result);
            }
        });
    });
}

function bindRegisterEvent(){
    $("#submit-btn").click(function(event){
        event.preventDefault();

        let email = $("#reg-email").val();
        let code = $("#reg-code").val();
        let username = $("#reg-username").val();
        let password = $("#reg-password").val();
        let confirm_password = $("#reg-confirm-password").val();
        if(confirm_password != password){
            alert("两次密码输入不一致！");
            return;
        }
        // 发送ajax请求
        $.post({
            url: "/register",
            data: {email, code, username, password},
            success: function (resp){
                if(resp['result'] == true){
                    window.location = "/login";
                }else{
                    let message = resp['message'];
                    alert(message);
                }
            }
        })
    })
}

// 这个函数会在整个网页加载完成后
$(function(){
    bindEmailCodeClick();
    bindRegisterEvent();
})