<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <el-form-item label="最新情报录入:">
                <el-input v-model="form.content"></el-input>
    </el-form-item>
        <el-form-item label="发生时间">
        <el-date-picker type="datetime" placeholder="选择时间" v-model="form.time" style="width: 100%;"></el-date-picker>
            </el-form-item>
        <el-form-item label="数据来源:">
        <el-input v-model="form.source"></el-input>
            </el-form-item>

    <el-form-item>
        <el-button type="primary"
        @click.native="onSubmit">立即创建
    </el-button>
        </el-form-item>
        </el-form>
        </template>

<script>
import { timeLineAdd} from '@/api/api';
export default {
    data() {
        return {
            form: {
                content:"请输入最新情报",
                source:"大情报",
                time:new Date()
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            this.addLatestData(this.form);
        },
        addLatestData(param){
            timeLineAdd(param)
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
}

</script>