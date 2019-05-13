<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
        <div v-for="(item) in form.data">
            <el-form-item :label="item.name">
                <el-input v-model="item.value"></el-input>
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
import { policeUseGet,policeUseAdd} from '@/api/api';
export default {
    data() {
        return {
            form: {
                "data": [
                    {
                        "name": "民警",
                        "value": 100
                    },
                    {
                        "name": "武警",
                        "value": 20
                    },
                    {
                        "name": "特警",
                        "value": 20
                    },
                    {
                        "name": "便衣",
                        "value": 20
                    },
                    {
                        "name": "备勤",
                        "value": 20
                    },
                    {
                        "name":"警车",
                        "value":20
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
//            policeUseGet().then((res) => {
//                this.form.data = res.data.data.data;
//        }).
//            catch((error) => {console.info(error)
//        }
//        )
//        },
        addLatestData(param){
            policeUseAdd(param)
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