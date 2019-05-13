import Login from './views/Login.vue'
import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import Main from './views/Main.vue'
import Table from './views/nav1/Table.vue'
import Form from './views/nav1/Form.vue'
import user from './views/nav1/user.vue'
import Page4 from './views/nav2/Page4.vue'
import Page5 from './views/nav2/Page5.vue'
import Page6 from './views/nav3/Page6.vue'
import echarts from './views/charts/echarts.vue'
import OccurTime from './views/nav1/OccurTime.vue'
import LatestQb from './views/nav1/LatestQb.vue'
import Duty from './views/nav1/Duty.vue'
import HBSituation from './views/nav1/HBSituation.vue'
import PoliceUse from './views/nav1/PoliceUse.vue'
import SensitiveArea from './views/nav1/SensitiveArea.vue'
import SensitiveInternet from './views/nav1/SensitiveInternet.vue'
import SensitiveSource from './views/nav1/SensitiveSource.vue'
import SensitiveWord from './views/nav1/SensitiveWord.vue'
import VideoAr from './views/nav1/VideoAr.vue'
let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    //{ path: '/main', component: Main },
    {
        path: '/',
        component: Home,
        name: '数据录入',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/main', component: Main, name: '主页', hidden: true },
            { path: '/table', component: Table, name: 'Table', hidden: true},
            { path: '/occurTime', component: OccurTime, name: '发生情况时刻数据' },
            { path: '/user', component: user, name: '列表' ,hidden: true},
            { path: '/latestQb', component: LatestQb, name: '最新情报录入' },
            { path: '/duty', component: Duty, name: '值班信息录入' },
            { path: '/hbsituation', component: HBSituation, name: '全省态势' },
            { path: '/policeuse', component: PoliceUse, name: '力量投入' },
            { path: '/sensitiveArea', component: SensitiveArea, name: '敏感区域部警情况' },
            { path: '/sensitiveInternet', component: SensitiveInternet, name: '敏感网络热度走势' },
            { path: '/SensitiveSource', component: SensitiveSource, name: '敏感媒体来源' },
            { path: '/SensitiveWord', component: SensitiveWord, name: '负面高频词汇' },
            { path: '/VideoAr', component: VideoAr, name: '负面高频词汇' },
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;