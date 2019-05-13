<template>
    <el-form ref="form" :model="form" label-width="100px" input-with="100px"
    @submit.prevent="onSubmit" style="margin:20px;width:60%;min-width:600px;">
    <el-form-item label="快闪总数:">
                <el-input v-model="form.ksAmount"></el-input>
    </el-form-item>
    <el-form-item label="已报备快闪:">
        <el-input v-model="form.ksRecord"></el-input>
    </el-form-item>
    <el-form-item label="已稳控快闪:">
        <el-input v-model="form.ksControl"></el-input>
    </el-form-item>
    <el-form-item label="其它:">
        <el-input v-model="form.ksOther"></el-input>
    </el-form-item>

    <el-form-item>
        <el-button type="primary"
        @click.native="onSubmit">立即创建
    </el-button>
        </el-form-item>
        </el-form>
        </template>

<script>
import { hbSituationGet,hbSituationAdd} from '@/api/api';
export default {
    data() {
        return {
            form: {
                "ksAmount": 232,
                "ksRecord": 187,
                "ksControl": 45,
                "ksOther": 50
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            this.addLatestData(this.form);
        },
//        getLatestData(){
//            hbSituationGet().then((res) => {
//                this.form = res.data.data.data;
//        }).
//            catch((error) => {console.info(error)
//        }
//        )
//        },
        addLatestData(param){
            hbSituationAdd(param)
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