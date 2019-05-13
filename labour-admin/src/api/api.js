import axios from 'axios';

let base = '';
let service = "http://127.0.0.1:8181";
export const requestLogin = params => {
    return axios.post(`${base}/login`, params).then(res => res.data);
};

export const getUserList = params => {
    return axios.get(`${base}/user/list`, {params: params});
};

export const getUserListPage = params => {
    return axios.get(`${base}/user/listpage`, {params: params});
};

export const removeUser = params => {
    return axios.get(`${base}/user/remove`, {params: params});
};

export const batchRemoveUser = params => {
    return axios.get(`${base}/user/batchremove`, {params: params});
};

export const editUser = params => {
    return axios.get(`${base}/user/edit`, {params: params});
};

export const addUser = params => {
    return axios.get(`${base}/user/add`, {params: params});
};

export const occurTimeTrendGet = params => {
    return axios.get(`${service}/occurTimeTrend/get`, {params: params});
}
export const occurTimeTrendAdd = data => {
    return axios.post(`${service}/occurTimeTrend/add`, {data:data});
}
//最新情报，无查询
//export const timeLineGet = params => {
//    return axios.get(`${service}/timeline/get`, {params: params});
//}
export const timeLineAdd = data => {
    return axios.post(`${service}/timeline/add`, {data:data});
}
//警力
export const policeUseGet = params => {
    return axios.get(`${service}/policeUseAdd/get`, {params: params});
}
export const policeUseAdd = data => {
    return axios.post(`${service}/policeUseAdd/add`, {data:data});
}
//敏感区域
export const sensitiveAreaGet = params => {
    return axios.get(`${service}/sensitiveArea/get`, {params: params});
}
export const sensitiveAreaAdd = data => {
    return axios.post(`${service}/sensitiveArea/add`, {data:data});
}
//敏感网络热度
export const sensitiveInternetGet = params => {
    return axios.get(`${service}/sensitiveInternet/get`, {params: params});
}
export const sensitiveInternetAdd = data => {
    return axios.post(`${service}/sensitiveInternet/add`, {data:data});
}
//敏感来源
export const sensitiveSourceGet = params => {
    return axios.get(`${service}/sensitiveSource/get`, {params: params});
}
export const sensitiveSourceAdd = data => {
    return axios.post(`${service}/sensitiveSource/add`, {data:data});
}
//敏感词云
export const sensitiveWordGet = params => {
    return axios.get(`${service}/sensitiveWord/get`, {params: params});
}
export const sensitiveWordAdd = data => {
    return axios.post(`${service}/sensitiveWord/add`, {data:data});
}
//视频在线比例
export const videoArGet = params => {
    return axios.get(`${service}/videoAr/get`, {params: params});
}
export const videoArAdd = data => {
    return axios.post(`${service}/videoAr/add`, {data:data});
}
//全省态势
export const hbSituationGet = params => {
    return axios.get(`${service}/hbSituation/get`, {params: params});
}
export const hbSituationAdd = data => {
    return axios.post(`${service}/hbSituation/add`, {data:data});
}
//值班信息
export const dutyGet = params => {
    return axios.get(`${service}/duty/get`, {params: params});
}
export const dutyAdd = data => {
    return axios.post(`${service}/duty/add`, {data:data});
}