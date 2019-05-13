<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <div v-for="(item) in form.data">
        <el-form-item label="名称">
            <el-input v-model="item.name"></el-input>
        </el-form-item>
        <el-form-item label="职位">
            <el-input v-model="item.job"></el-input>
        </el-form-item>
        <el-form-item label="图片路径">
            <el-input v-model="item.img"></el-input>
        </el-form-item>
    </div>
    <el-form-item>
        <el-button type="primary"
        @click.native="onSubmit">立即创建
    </el-button>
        </el-form-item>
        </el-form>
        </template>

<script>
import { dutyGet,dutyAdd} from '@/api/api';
export default {
    data() {
        return {
            form: {
                "data": [
                    {
                        "name": "XX",
                        "job": "带班局领导1",
                        "img": "01.jpg"
                    },
                    {
                        "name": "XX",
                        "job": "带班局领导2",
                        "img": "01.jpg"
                    }
                ]
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            this.addLatestData(this.form.data);
        },
//        getLatestData(){
//            dutyGet().then((res) => {
//                this.form.data = res.data.data.data;
//        }).
//            catch((error) => {console.info(error)
//        }
//        )
//        },
        addLatestData(param){
            dutyAdd(param)
                    .then((res) => {this.$message({
                message: '提交成功',
                type: 'success'
            });
            console.info(res);
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