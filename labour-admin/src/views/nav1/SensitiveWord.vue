<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <el-form-item label="输入敏感词数据">
        <el-input type="textarea" v-model="form.str"></el-input>
    </el-form-item>

    <el-form-item>
        <el-button type="primary"
        @click.native="onSubmit">立即创建
    </el-button>
        </el-form-item>
        </el-form>
        </template>

<script>
import { sensitiveWordAdd} from '@/api/api';
export default {
    data() {
        return {
            form: {
                str:JSON.stringify({
                    "data": [
                        {
                            "name": "劳动合同纠纷",
                            "value": 100,
                            "itemStyle": {
                                "normal": {
                                    "color": "black"
                                }
                            }
                        },   {
                            "name": "民间信贷纠纷",
                            "value": 1000,
                            "itemStyle": {
                                "normal": {
                                    "color": "green"
                                }
                            }
                        }
                    ]
                }),
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            let data = JSON.parse(this.form.str)
            this.addLatestData(this.form);
        },
        addLatestData(param){
            sensitiveWordAdd(param)
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