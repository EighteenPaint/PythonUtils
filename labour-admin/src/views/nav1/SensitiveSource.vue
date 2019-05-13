<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <el-form-item label="涉军">
        <div v-for="(item) in form.shejun">
            <el-form-item :label="item.name">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="反宣">
        <div v-for="(item) in form.fandong">
            <el-form-item :label="item.name">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="涉众">
        <div v-for="(item) in form.shezhong">
            <el-form-item :label="item.name">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="敏感时间节点">
        <div v-for="(item) in form.shezhong">
            <el-form-item :label="item.name">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="其它">
        <div v-for="(item) in form.other">
            <el-form-item :label="item.name">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item>
        <el-button type="primary"
        @click.native="onSubmit">立即创建
    </el-button>
        </el-form-item>
        </el-form>
        </template>

<script>
import { sensitiveSourceGet,sensitiveSourceAdd} from '@/api/api';
export default {
    data() {
        return {
            form: {
                "shejun": [
                    {"name":"微博","value":6},
                    {"name":"客户端","value":10},
                    {"name":"网站","value":69},
                    {"name":"微信","value":10},
                    {"name":"新闻","value":10},
                    {"name":"视频","value":10},
                    {"name":"论坛","value":10},
                    {"name":"报刊","value":98},
                    {"name":"政务","value":10},
                    {"name":"外媒","value":69},
                    {"name":"博客","value":10},
                ],
                "fandong": [
                    {"name":"微博","value":6},
                    {"name":"客户端","value":10},
                    {"name":"网站","value":69},
                    {"name":"微信","value":10},
                    {"name":"新闻","value":10},
                    {"name":"视频","value":10},
                    {"name":"论坛","value":10},
                    {"name":"报刊","value":98},
                    {"name":"政务","value":10},
                    {"name":"外媒","value":69},
                    {"name":"博客","value":10},
                ],
                "shezhong":[
                    {"name":"微博","value":6},
                    {"name":"客户端","value":10},
                    {"name":"网站","value":69},
                    {"name":"微信","value":10},
                    {"name":"新闻","value":10},
                    {"name":"视频","value":10},
                    {"name":"论坛","value":10},
                    {"name":"报刊","value":98},
                    {"name":"政务","value":10},
                    {"name":"外媒","value":69},
                    {"name":"博客","value":10},
                ] ,
                "other":[
                    {"name":"微博","value":6},
                    {"name":"客户端","value":10},
                    {"name":"网站","value":69},
                    {"name":"微信","value":10},
                    {"name":"新闻","value":10},
                    {"name":"视频","value":10},
                    {"name":"论坛","value":10},
                    {"name":"报刊","value":98},
                    {"name":"政务","value":10},
                    {"name":"外媒","value":69},
                    {"name":"博客","value":10},
                ] ,
                "sentitiveTime":[
                    {"name":"微博","value":6},
                    {"name":"客户端","value":10},
                    {"name":"网站","value":69},
                    {"name":"微信","value":10},
                    {"name":"新闻","value":10},
                    {"name":"视频","value":10},
                    {"name":"论坛","value":10},
                    {"name":"报刊","value":98},
                    {"name":"政务","value":10},
                    {"name":"外媒","value":69},
                    {"name":"博客","value":10},
                ]
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            this.addLatestData(this.form);
        },
//        getLatestData(){
//            sensitiveSourceGet().then((res) => {
//                this.form.shejun = res.data.data.data.shejun;
//                this.form.fandong = res.data.data.data.fandong;
//            this.form.shezhong = res.data.data.data.shezhong;
//            this.form.other = res.data.data.data.other;
//        }).
//            catch((error) => {console.info(error)
//        }
//        )
//        },
        addLatestData(param){
            sensitiveSourceAdd(param)
                    .then((res) => {this.$message({
                message: '提交成功',
                type: 'success'
            });
            console.info(res);
            this.getLatestData()
        })
        .
            catch((error) => {this.$message({
                message: '提交失败',
                type: 'error'
            });console.log(error)
        })
            ;
        }
    },
    mounted() {
        this.getLatestData();
    }
}

</script>