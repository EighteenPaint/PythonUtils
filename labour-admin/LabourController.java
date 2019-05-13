package com.labour.rest;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.labour.bean.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoOperations;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by chenbin@tieserv.com on 2019/4/27 0027.
 */
@RestController
public class LabourController {
    private static final Logger log = LoggerFactory.getLogger(LabourController.class);
    public static final ObjectMapper mapper = new ObjectMapper();
    private static final String DOUBLE_PIE_C = "double_pie";
    private static final String OCCUR_TIME_C = "occur_time";
    private static final String POLICE_USE_C = "police_use";
    private static final String SENSITIVE_AREA_C = "sensitive_area";
    private static final String SENSITIVE_INTERNET_C = "sensitive_internet";
    private static final String SENSITIVE_SOURCE_C = "sensitive_source";
    private static final String SENSITIVE_WORD_C = "sensitive_word";
    private static final String VIDEO_AR_C = "video_ar";
    private static final String TIME_LINE_C = "time_line";
    private static final String HB_SITUATION = "hb_situation";
    private static final String DUTY_C = "duty";
    private static final String EXCHANGE = "labour";
    private static final String ROUTE_KEY = "latest.info";
    @Autowired
    MongoOperations mongoOperations;
    @Autowired
    RabbitTemplate rabbitTemplate;

    private String saveMongo(InsertObject insertObject,String collection) throws JsonProcessingException {
            String json = mapper.writeValueAsString(insertObject);
            log.info(json);
            mongoOperations.insert(json, collection);
            return json;
    }

    /**
     * 查询最新的一个
     * @param collections
     * @return
     */
    private Map queryMongo(String collections){
        Query query = new Query();
        Sort sort = new Sort(Sort.Direction.DESC, "date");
        query.with(sort).limit(1);
        List<LinkedHashMap> results = mongoOperations.find(query, LinkedHashMap.class, collections);
        return results.get(0);
    }
    /**
     * 双饼图
     *
     * @param request
     * @return
     */
    @PostMapping("/doublePie/add")
    public int doublePieAdd(@RequestBody Object request) {
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
         saveMongo(insertObject,DOUBLE_PIE_C);
        } catch (Exception e) {
            log.error("/doublePie/add:{}", e);
            return 500;
        }
        return 200;
    }

    @GetMapping("/doublePie/get")
    public Map doublePieGet() {
        return queryMongo(DOUBLE_PIE_C);
    }

    /**
     * 发生情况时刻走势图
     */
    @PostMapping("/occurTimeTrend/add")
    public int occurTimeTrendAdd(@RequestBody Object request) {
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,OCCUR_TIME_C);
        } catch (Exception e) {
            log.error("/occurTimeTrend/add:{}", e);
            return 500;
        }
        return 200;
    }

    @GetMapping("/occurTimeTrend/get")
    public Map occurTimeTrendGet() {
      return queryMongo(OCCUR_TIME_C);
    }

    /**
     * 最新情报-时间线
     * @param request
     * @return
     */
    @PostMapping("/timeline/add")
    public int timeLineAdd(@RequestBody Object request) {
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            String content = saveMongo(insertObject,TIME_LINE_C);
            rabbitTemplate.convertAndSend(EXCHANGE,ROUTE_KEY,content);
        } catch (Exception e) {
            log.error("/timeline/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/timeline/get")
    public List<LinkedHashMap> timelineGet(@RequestParam(required = false,defaultValue = "10") int size) {
        Query query = new Query();
        Sort sort = new Sort(Sort.Direction.DESC, "date");
        query.with(sort).limit(size);
        List<LinkedHashMap> results = mongoOperations.find(query, LinkedHashMap.class, TIME_LINE_C);
        return results;
    }
    /**
     * 警力分配
     */
    @PostMapping("/policeUse/add")
    public int policeUseAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,POLICE_USE_C);
        } catch (Exception e) {
            log.error("/policeUse/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/policeUse/get")
    public Map policeUseGet(){
        return queryMongo(POLICE_USE_C);
    }
    /**
     * 敏感区域警力分配
     */
    @PostMapping("/sensitiveArea/add")
    public int sensitiveAreaAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,SENSITIVE_AREA_C);
        } catch (Exception e) {
            log.error("/sensitiveArea/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/sensitiveArea/get")
    public Map sensitiveAreaGet(){
        return queryMongo(SENSITIVE_AREA_C);
    }
    /**
     * 敏感网络热度趋势
     */
    @PostMapping("/sensitiveInternet/add")
    public int sensitiveInternetAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,SENSITIVE_INTERNET_C);
        } catch (Exception e) {
            log.error("/sensitiveInternet/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/sensitiveInternet/get")
    public Map sensitiveInternetGet(){
        return queryMongo(SENSITIVE_INTERNET_C);
    }
    /**
     * 敏感来源统计
     */
    @PostMapping("/sensitiveSource/add")
    public int sensitiveSourceAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,SENSITIVE_SOURCE_C);
        } catch (Exception e) {
            log.error("/sensitiveSource/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/sensitiveSource/get")
    public Map sensitiveSourceGet(){
        return queryMongo(SENSITIVE_SOURCE_C);
    }
    /**
     * 敏感词云
     */
    @PostMapping("/sensitiveWord/add")
    public int sensitiveWordAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,SENSITIVE_WORD_C);
        } catch (Exception e) {
            log.error("/sensitiveWord/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/sensitiveWord/get")
    public Map sensitiveWordGet(){
        return queryMongo(SENSITIVE_WORD_C);
    }
    /**
     * 视频点位在线比例
     */
    @PostMapping("/videoAr/add")
    public int videoArAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,VIDEO_AR_C);
        } catch (Exception e) {
            log.error("/videoAr/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/videoAr/get")
    public Map videoArGet(){
        return queryMongo(VIDEO_AR_C);
    }
    /**
     * 全省态势
     */
    @PostMapping("/hbSituation/add")
    public int hbSituationAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,HB_SITUATION);
        } catch (Exception e) {
            log.error("/hbSituation/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/hbSituation/get")
    public Map hbSituationGet(){
        return queryMongo(HB_SITUATION);
    }
    /**
     * 值班信息
     */
    @PostMapping("/duty/add")
    public int dutyAdd(@RequestBody Object request){
        InsertObject insertObject = new InsertObject(request, new Date());
        try {
            saveMongo(insertObject,DUTY_C);
        } catch (Exception e) {
            log.error("/hbSituation/add:{}", e);
            return 500;
        }
        return 200;
    }
    @GetMapping("/duty/get")
    public Map dutyGet(){
        return queryMongo(DUTY_C);
    }
}
