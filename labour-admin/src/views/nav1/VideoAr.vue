<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
        <div v-for="(item) in form.data">
            <el-form-item :label="item.name">
                <el-input v-model="item.y"></el-input>
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
import { videoArAdd,videoArGet} from '@/api/api';
export default {
    data() {
        return {
            form: {
                "data": [
                    {
                        "name": "视频",
                        "y": 100
                    },
                    {
                        "name": "高点AR",
                        "y": 50,
                        "sliced": true,
                        "selected": true
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
//            videoArGet().then((res) => {
//                this.form.data = res.data.data.data;
//        }).
//            catch((error) => {console.info(error)
//        }
//        )
//        },
        addLatestData(param){
            videoArAdd(param)
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