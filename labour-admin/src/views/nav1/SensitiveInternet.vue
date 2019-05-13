<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <el-form-item label="涉军">
        <div v-for="(item) in form.shejun">
            <el-form-item :label="item.name+'点'">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="反动">
        <div v-for="(item) in form.fandong">
            <el-form-item :label="item.name+'点'">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="涉众">
        <div v-for="(item) in form.shezhong">
            <el-form-item :label="item.name+'点'">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="其它">
        <div v-for="(item) in form.other">
            <el-form-item :label="item.name+'点'">
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
import { sensitiveInternetAdd,sensitiveInternetGet} from '@/api/api';
export default {
    data() {
        return {
            form: {
                "shejun": [
                    {"name":"2","value":6},
                    {"name":"4","value":10},
                    {"name":"6","value":69},
                    {"name":"8","value":10},
                    {"name":"10","value":10},
                    {"name":"12","value":10},
                    {"name":"14","value":10},
                    {"name":"16","value":98},
                    {"name":"18","value":10},
                    {"name":"20","value":69},
                    {"name":"22","value":10},
                    {"name":"24","value":10}
                ],
                "fandong": [
                    {"name":"2","value":0},
                    {"name":"4","value":10},
                    {"name":"6","value":87},
                    {"name":"8","value":10},
                    {"name":"10","value":10},
                    {"name":"12","value":10},
                    {"name":"14","value":60},
                    {"name":"16","value":10},
                    {"name":"18","value":100},
                    {"name":"20","value":10},
                    {"name":"22","value":10},
                    {"name":"24","value":10}
                ],
                "shezhong": [
                    {"name":"2","value":10},
                    {"name":"4","value":10},
                    {"name":"6","value":10},
                    {"name":"8","value":10},
                    {"name":"10","value":20},
                    {"name":"12","value":10},
                    {"name":"14","value":10},
                    {"name":"16","value":15},
                    {"name":"18","value":10},
                    {"name":"20","value":10},
                    {"name":"22","value":10},
                    {"name":"24","value":10}
                ],
                "other": [
                    {"name":"2","value":10},
                    {"name":"4","value":10},
                    {"name":"6","value":10},
                    {"name":"8","value":10},
                    {"name":"10","value":10},
                    {"name":"12","value":10},
                    {"name":"14","value":10},
                    {"name":"16","value":80},
                    {"name":"18","value":10},
                    {"name":"20","value":10},
                    {"name":"22","value":10},
                    {"name":"24","value":10}
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
//            sensitiveInternetGet().then((res) => {
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
            sensitiveInternetAdd(param)
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