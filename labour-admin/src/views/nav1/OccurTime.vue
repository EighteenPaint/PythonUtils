<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <el-form-item label="实际发生量">
        <div v-for="(item) in form.fact">
            <el-form-item :label="item.name+'点'">
                <el-input v-model="item.value"></el-input>
            </el-form-item>
        </div>
    </el-form-item>
    <el-form-item label="情报总量">
        <div v-for="(item) in form.total">
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
import { occurTimeTrendAdd,occurTimeTrendGet} from '@/api/api';
export default {
    data() {
        return {
            form: {
                fact: [
                    {"name": "2", "value": 0},
                    {"name": "4", "value": 5},
                    {"name": "6", "value": 18},
                    {"name": "8", "value": 10},
                    {"name": "10", "value": 50},
                    {"name": "12", "value": 10},
                    {"name": "14", "value": 58},
                    {"name": "16", "value": 89},
                    {"name": "18", "value": 10},
                    {"name": "20", "value": 158},
                    {"name": "22", "value": 10},
                    {"name": "24", "value": 10}
                ],
                total: [{"name": "2", "value": 0},
                    {"name": "4", "value": 5},
                    {"name": "6", "value": 18},
                    {"name": "8", "value": 10},
                    {"name": "10", "value": 50},
                    {"name": "12", "value": 10},
                    {"name": "14", "value": 58},
                    {"name": "16", "value": 89},
                    {"name": "18", "value": 10},
                    {"name": "20", "value": 158},
                    {"name": "22", "value": 10},
                    {"name": "24", "value": 10}]
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            console.info(this.form.fact)
            let parma = {};
            let fact = this.form.fact;
            let total = this.form.total;
            console.info(parma)
            this.addLatestData({fact, total});
        },
//        getLatestData(){
//            occurTimeTrendGet().then((res) => {
//                this.form.total = res.data.data.data.total;
//            this.form.fact = res.data.data.data.fact;
//        }).
//            catch((error) => {console.info(error)
//        }
//        )
//        },
        addLatestData(param){
            occurTimeTrendAdd(param)
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