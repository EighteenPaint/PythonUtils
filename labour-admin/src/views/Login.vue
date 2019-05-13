<template>
    <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px"
             class="demo-ruleForm login-container">
        <h3 class="title">欢迎使用</h3>
        <el-form-item prop="account">
            <el-input type="text" v-model="ruleForm2.account" auto-complete="off" placeholder="账号"></el-input>
        </el-form-item>
        <el-form-item prop="checkPass">
            <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off" placeholder="密码"></el-input>
        </el-form-item>
        <div>
            <!--输入框部分-->
        <!--<el-form-item prop="verifycode" class="vali-input">-->
            <!--<el-input v-model="ruleForm2.verifycode" placeholder="验证码" class="vali-code"></el-input>-->
        <!--</el-form-item>-->
            <!--验证码部分-->
            <!--<div class="identifybox">-->
                <!--<div @click="refreshCode">-->
                    <!--<v-code :identifyCode="identifyCode"></v-code>-->
                <!--</div>-->
                <!--<el-button @click="refreshCode" type='text' class="textbtn">看不清，换一张</el-button>-->
            <!--</div>-->
        </div>
<el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
<el-form-item style="width:100%;">
<el-button type="primary" style="width:100%;"
@click.native.prevent="handleSubmit2" :loading="logining">登录
</el-button>
        <!--<el-button @click.native.prevent="handleReset2">重置</el-button>-->
        </el-form-item>
        </el-form>
        </template>

<script>
import { requestLogin } from '../api/api';
import VCode from './validate/VCode';
//import NProgress from 'nprogress'
export default {
//    依赖的局部组件：验证码组件
    components: {
        VCode
    },
    data() {
        return {
            identifyCodes: '1234567890',
            identifyCode: "",
            logining: false,
            ruleForm2: {
                account: 'admin',
                checkPass: '123456',
                verifycode: ''
            },
            rules2: {
                account: [
                    {required: true, message: '请输入账号', trigger: 'blur'},
                    //{ validator: validaePass }
                ],
                checkPass: [
                    {required: true, message: '请输入密码', trigger: 'blur'},
                    //{ validator: validaePass2 }
                ],
//                verifycode: [{required: true, trigger: 'blur', validator: this.validateVerifycode}]
            },
            checked: true
        };
    },
    mounted(){
        this.identifyCode = '';
        this.makeCode(this.identifyCodes, 4);
    },
    methods: {
        // 验证码自定义验证规则
        validateVerifycode: function (rule, value, callback) {
            if (value === '') {
                callback(new Error('请输入验证码'))
            } else if (value !== this.identifyCode) {
                callback(new Error('验证码不正确!'))
                this.refreshCode()
            } else {
                callback()
            }
        },
        refreshCode: function () {
            this.identifyCode = '';
            this.makeCode(this.identifyCodes, 4)
        },
        makeCode: function (codes, length) {
            for (let i = 0; i < length; i++) {
                this.identifyCode += codes[this.randonNum(0, 4)]
            }
        },
        randonNum: function (min, max) {
            return Math.floor(Math.random() * (max - min) + min)
        },
        handleReset2() {
            this.$refs.ruleForm2.resetFields();
        },
        handleSubmit2(ev) {
            var _this = this;
            console.info(this)
            this.$refs.ruleForm2.validate((valid) => {
                if (valid) {
                    //_this.$router.replace('/table');
                    this.logining = true;
                    //NProgress.start();
                    var loginParams = {username: this.ruleForm2.account, password: this.ruleForm2.checkPass};
                    requestLogin(loginParams).then(data => {
                        this.logining = false;
                    //NProgress.done();
                    let { msg, code, user } = data;
                    if (code !== 200) {
                        this.$message({
                            message: msg,
                            type: 'error'
                        });
//                        this.refreshCode();
                    } else {
                        sessionStorage.setItem('user', JSON.stringify(user));
                        this.$router.push({path: '/table'});
                    }
                })
                    ;
                } else {
                    console.log('error submit!!');
            return false;
        }
        })
            ;
        }
    }
}

</script>

<style lang="scss" scoped>
.login-container {
    /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}

.title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
}

.remember {
    margin: 0px 0px 35px 0px;
}
.vali-input{
    display: inline-table;
    width: 203px;
    margin-right: 27px;
    margin-top: 0;
}
.identifybox{
    display: inline-table;
}


</style>